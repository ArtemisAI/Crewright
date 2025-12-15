import asyncio
import logging
import os
import json
import time
import threading
import uuid
from flask import Flask, request, jsonify
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContext, BrowserContextConfig

load_dotenv()

app = Flask(__name__)

# Configuration loading
BROWSER_USE_HOST = os.getenv('BROWSER_USE_HOST', '0.0.0.0')
BROWSER_USE_PORT = int(os.getenv('BROWSER_USE_PORT', '4999'))
BROWSER_USE_MAX_WORKERS = int(os.getenv('BROWSER_USE_MAX_WORKERS', '1'))
BROWSER_WINDOW_WIDTH = int(os.getenv('BROWSER_WINDOW_WIDTH', '540'))
BROWSER_WINDOW_HEIGHT = int(os.getenv('BROWSER_WINDOW_HEIGHT', '768'))
BROWSER_USE_HEADLESS = os.getenv('BROWSER_USE_HEADLESS', 'true').lower() == 'true'

# Task storage to keep track of tasks
tasks = {}

# Initialize a thread pool executor for running tasks in the background
executor = ThreadPoolExecutor(max_workers=BROWSER_USE_MAX_WORKERS)

sensitive_data = {
    'x_name': os.getenv('BROWSER_USE_USERNAME', ''),
    'x_password': os.getenv('BROWSER_USE_PASSWORD', '')
}

# Function to process the task in the background
def process_task(task_id, objective):
    logger.info(f"Starting Browser-Use agent with objective: {objective}\n")

    async def run_browser_use(objective):
        try:
            browser = Browser(
                config=BrowserConfig(
                    headless=BROWSER_USE_HEADLESS,
                )
            )
            
            # Setup LLM with optional base_url for compatibility
            llm_kwargs = {
                'model': os.environ['MODEL_NAME'],
                'api_key': os.environ['OPENAI_API_KEY']
            }
            if os.getenv('OPENAI_API_BASE'):
                llm_kwargs['base_url'] = os.getenv('OPENAI_API_BASE')

            agent = Agent(
                task=objective,
                browser_context=BrowserContext(
                    browser=browser,
                    config=BrowserContextConfig(
                        browser_window_size={'width': BROWSER_WINDOW_WIDTH, 'height': BROWSER_WINDOW_HEIGHT},
                        viewport_expansion=BROWSER_WINDOW_HEIGHT
                    ),
                ),
                llm=ChatOpenAI(**llm_kwargs),
                sensitive_data=sensitive_data,
                use_vision=False,
            )
            results = await agent.run()
        except Exception as e:
            logger.error(f"Error in agent.run(): {e}", exc_info=True)
            results = {}
        finally:
            await browser.close()
        return results

    # Ensure we are in a new event loop
    loop = asyncio.new_event_loop()
    try:
        asyncio.set_event_loop(loop)
        results = loop.run_until_complete(run_browser_use(objective))
        logger.info("Browser-Use agent finished.")
        results = results.final_result()
    except Exception as e:
        logger.error(f"Error in agent.run(): {e}", exc_info=True)
    finally:
        loop.close()

    # Update the task status and results    
    tasks[task_id] = {
        "status": "completed",
        "message": f"Objective completed: {objective}",
        "results": results
    }
    logger.info("Browser-Use agent finished.")

@app.route('/probe', methods=['GET'])
def probe():
    return "browser_use_service is alive", 200

@app.route('/submit', methods=['POST'])
def submit():
    objective = request.json.get("browser_use_objective")
    if not objective:
        return jsonify({"status": "error", "message": "No objective provided."}), 400

    # Generate a unique task ID
    task_id = str(uuid.uuid4())

    # Initialize the task with "processing" status
    tasks[task_id] = {"status": "processing"}

    # Submit the task to the thread pool executor
    executor.submit(process_task, task_id, objective)

    # Return the task ID immediately
    return jsonify({"status": "processing", "task_id": task_id}), 202

@app.route('/query/<task_id>', methods=['GET'])
def query(task_id):
    if task_id not in tasks:
        return jsonify({"status": "error", "message": "Task ID not found."}), 404

    task = tasks[task_id]
    if task["status"] == "processing":
        return jsonify({"status": "processing"}), 202
    elif task["status"] == "completed":
        logger.info(f"Task is completed: {task}")
        return jsonify(task), 200

if __name__ == '__main__':
    logger.info(f"Starting server on {BROWSER_USE_HOST}:{BROWSER_USE_PORT}")
    app.run(debug=True, host=BROWSER_USE_HOST, port=BROWSER_USE_PORT)
