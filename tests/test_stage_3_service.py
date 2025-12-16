import requests
import sys
import time
import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("BROWSER_USE_HOST", "localhost")
PORT = os.getenv("BROWSER_USE_PORT", "4999")

# Adjust host if 0.0.0.0
if HOST == "0.0.0.0":
    HOST = "localhost"

URL = f"http://{HOST}:{PORT}"

def run_test():
    print(f"Stage 3: Service Health Verification at {URL}")
    
    max_retries = 5
    for i in range(max_retries):
        try:
            print(f"Attempt {i+1}...")
            # Often Flask apps have no root route, but usually 404 is a sign of life, or we check a specific endpoint.
            # The service likely has /submit or /query. 
            # I'll try to just connect. If I get connection refused, it's down.
            # If I get 404 or 405, it's UP (just hitting wrong endpoint).
            response = requests.get(URL, timeout=5)
            print(f"Response: {response.status_code}")
            print(f"SUCCESS: Service is reachable")
            return
        except requests.exceptions.ConnectionError:
            print("Connection refused, waiting...")
            time.sleep(2)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    
    print("FAILURE: Service not reachable after retries")
    sys.exit(1)

if __name__ == "__main__":
    run_test()
