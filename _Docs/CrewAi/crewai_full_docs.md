# CrewAI Full Documentation



# Source: https://docs.crewai.com/en/introduction

Skip to main content

[CrewAI home page![light logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)![dark logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)](/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl K

Search...

Navigation

Get Started

Introduction

[Home](/)[Documentation](/en/introduction)[AOP](/en/enterprise/introduction)[API Reference](/en/api-reference/introduction)[Examples](/en/examples/example)[Changelog](/en/changelog)

  * [Website](https://crewai.com)
  * [Forum](https://community.crewai.com)
  * [Blog](https://blog.crewai.com)
  * [CrewGPT](https://chatgpt.com/g/g-qqTuUWsBY-crewai-assistant)



##### Get Started

  * [Introduction](/en/introduction)
  * [Installation](/en/installation)
  * [Quickstart](/en/quickstart)



##### Guides

  * Strategy

  * Agents

  * Crews

  * Flows

  * Advanced




##### Core Concepts

  * [Agents](/en/concepts/agents)
  * [Tasks](/en/concepts/tasks)
  * [Crews](/en/concepts/crews)
  * [Flows](/en/concepts/flows)
  * [Knowledge](/en/concepts/knowledge)
  * [LLMs](/en/concepts/llms)
  * [Processes](/en/concepts/processes)
  * [Collaboration](/en/concepts/collaboration)
  * [Training](/en/concepts/training)
  * [Memory](/en/concepts/memory)
  * [Reasoning](/en/concepts/reasoning)
  * [Planning](/en/concepts/planning)
  * [Testing](/en/concepts/testing)
  * [CLI](/en/concepts/cli)
  * [Tools](/en/concepts/tools)
  * [Event Listeners](/en/concepts/event-listener)



##### MCP Integration

  * [MCP Servers as Tools in CrewAI](/en/mcp/overview)
  * [MCP DSL Integration](/en/mcp/dsl-integration)
  * [Stdio Transport](/en/mcp/stdio)
  * [SSE Transport](/en/mcp/sse)
  * [Streamable HTTP Transport](/en/mcp/streamable-http)
  * [Connecting to Multiple MCP Servers](/en/mcp/multiple-servers)
  * [MCP Security Considerations](/en/mcp/security)



##### Tools

  * [Tools Overview](/en/tools/overview)
  * File & Document

  * Web Scraping & Browsing

  * Search & Research

  * Database & Data

  * AI & Machine Learning

  * Cloud & Storage

  * Integrations

  * Automation




##### Observability

  * [CrewAI Tracing](/en/observability/tracing)
  * [Overview](/en/observability/overview)
  * [Arize Phoenix](/en/observability/arize-phoenix)
  * [Braintrust](/en/observability/braintrust)
  * [Datadog Integration](/en/observability/datadog)
  * [LangDB Integration](/en/observability/langdb)
  * [Langfuse Integration](/en/observability/langfuse)
  * [Langtrace Integration](/en/observability/langtrace)
  * [Maxim Integration](/en/observability/maxim)
  * [MLflow Integration](/en/observability/mlflow)
  * [Neatlogs Integration](/en/observability/neatlogs)
  * [OpenLIT Integration](/en/observability/openlit)
  * [Opik Integration](/en/observability/opik)
  * [Patronus AI Evaluation](/en/observability/patronus-evaluation)
  * [Portkey Integration](/en/observability/portkey)
  * [Weave Integration](/en/observability/weave)
  * [TrueFoundry Integration](/en/observability/truefoundry)



##### Learn

  * [Overview](/en/learn/overview)
  * [Strategic LLM Selection Guide](/en/learn/llm-selection-guide)
  * [Conditional Tasks](/en/learn/conditional-tasks)
  * [Coding Agents](/en/learn/coding-agents)
  * [Create Custom Tools](/en/learn/create-custom-tools)
  * [Custom LLM Implementation](/en/learn/custom-llm)
  * [Custom Manager Agent](/en/learn/custom-manager-agent)
  * [Customize Agents](/en/learn/customizing-agents)
  * [Image Generation with DALL-E](/en/learn/dalle-image-generation)
  * [Force Tool Output as Result](/en/learn/force-tool-output-as-result)
  * [Hierarchical Process](/en/learn/hierarchical-process)
  * [Human Input on Execution](/en/learn/human-input-on-execution)
  * [Human-in-the-Loop (HITL) Workflows](/en/learn/human-in-the-loop)
  * [Kickoff Crew Asynchronously](/en/learn/kickoff-async)
  * [Kickoff Crew for Each](/en/learn/kickoff-for-each)
  * [Connect to any LLM](/en/learn/llm-connections)
  * [Using Multimodal Agents](/en/learn/multimodal-agents)
  * [Replay Tasks from Latest Crew Kickoff](/en/learn/replay-tasks-from-latest-crew-kickoff)
  * [Sequential Processes](/en/learn/sequential-process)
  * [Using Annotations in crew.py](/en/learn/using-annotations)
  * [Execution Hooks Overview](/en/learn/execution-hooks)
  * [LLM Call Hooks](/en/learn/llm-hooks)
  * [Tool Call Hooks](/en/learn/tool-hooks)



##### Telemetry

  * [Telemetry](/en/telemetry)



Get Started

# Introduction

Copy page

Build AI agent teams that work together to tackle complex tasks

Copy page

# 

​

What is CrewAI?

**CrewAI is a lean, lightning-fast Python framework built entirely from scratch—completely independent of LangChain or other agent frameworks.** CrewAI empowers developers with both high-level simplicity and precise low-level control, ideal for creating autonomous AI agents tailored to any scenario:

  * **[CrewAI Crews](/en/guides/crews/first-crew)** : Optimize for autonomy and collaborative intelligence, enabling you to create AI teams where each agent has specific roles, tools, and goals.
  * **[CrewAI Flows](/en/guides/flows/first-flow)** : Enable granular, event-driven control, single LLM calls for precise task orchestration and supports Crews natively.

With over 100,000 developers certified through our community courses, CrewAI is rapidly becoming the standard for enterprise-ready AI automation.

## 

​

How Crews Work

Just like a company has departments (Sales, Engineering, Marketing) working together under leadership to achieve business goals, CrewAI helps you create an organization of AI agents with specialized roles collaborating to accomplish complex tasks.

![CrewAI Framework Overview](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=514fd0b06e4128e62f10728d44601975)

CrewAI Framework Overview

Component| Description| Key Features  
---|---|---  
**Crew**|  The top-level organization| • Manages AI agent teams  
• Oversees workflows  
• Ensures collaboration  
• Delivers outcomes  
**AI Agents**|  Specialized team members| • Have specific roles (researcher, writer)  
• Use designated tools  
• Can delegate tasks  
• Make autonomous decisions  
**Process**|  Workflow management system| • Defines collaboration patterns  
• Controls task assignments  
• Manages interactions  
• Ensures efficient execution  
**Tasks**|  Individual assignments| • Have clear objectives  
• Use specific tools  
• Feed into larger process  
• Produce actionable results  
  
### 

​

How It All Works Together

  1. The **Crew** organizes the overall operation
  2. **AI Agents** work on their specialized tasks
  3. The **Process** ensures smooth collaboration
  4. **Tasks** get completed to achieve the goal



## 

​

Key Features

## Role-Based Agents

Create specialized agents with defined roles, expertise, and goals - from researchers to analysts to writers

## Flexible Tools

Equip agents with custom tools and APIs to interact with external services and data sources

## Intelligent Collaboration

Agents work together, sharing insights and coordinating tasks to achieve complex objectives

## Task Management

Define sequential or parallel workflows, with agents automatically handling task dependencies

## 

​

How Flows Work

While Crews excel at autonomous collaboration, Flows provide structured automations, offering granular control over workflow execution. Flows ensure tasks are executed reliably, securely, and efficiently, handling conditional logic, loops, and dynamic state management with precision. Flows integrate seamlessly with Crews, enabling you to balance high autonomy with exacting control.

![CrewAI Framework Overview](https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=82ea168de2f004553dcea21410cd7d8a)

CrewAI Framework Overview

Component| Description| Key Features  
---|---|---  
**Flow**|  Structured workflow orchestration| • Manages execution paths  
• Handles state transitions  
• Controls task sequencing  
• Ensures reliable execution  
**Events**|  Triggers for workflow actions| • Initiate specific processes  
• Enable dynamic responses  
• Support conditional branching  
• Allow for real-time adaptation  
**States**|  Workflow execution contexts| • Maintain execution data  
• Enable persistence  
• Support resumability  
• Ensure execution integrity  
**Crew Support**|  Enhances workflow automation| • Injects pockets of agency when needed  
• Complements structured workflows  
• Balances automation with intelligence  
• Enables adaptive decision-making  
  
### 

​

Key Capabilities

## Event-Driven Orchestration

Define precise execution paths responding dynamically to events

## Fine-Grained Control

Manage workflow states and conditional execution securely and efficiently

## Native Crew Integration

Effortlessly combine with Crews for enhanced autonomy and intelligence

## Deterministic Execution

Ensure predictable outcomes with explicit control flow and error handling

## 

​

When to Use Crews vs. Flows

Understanding when to use [Crews](/en/guides/crews/first-crew) versus [Flows](/en/guides/flows/first-flow) is key to maximizing the potential of CrewAI in your applications.

Use Case| Recommended Approach| Why?  
---|---|---  
**Open-ended research**| [Crews](/en/guides/crews/first-crew)| When tasks require creative thinking, exploration, and adaptation  
**Content generation**| [Crews](/en/guides/crews/first-crew)| For collaborative creation of articles, reports, or marketing materials  
**Decision workflows**| [Flows](/en/guides/flows/first-flow)| When you need predictable, auditable decision paths with precise control  
**API orchestration**| [Flows](/en/guides/flows/first-flow)| For reliable integration with multiple external services in a specific sequence  
**Hybrid applications**|  Combined approach| Use [Flows](/en/guides/flows/first-flow) to orchestrate overall process with [Crews](/en/guides/crews/first-crew) handling complex subtasks  
  
### 

​

Decision Framework

  * **Choose[Crews](/en/guides/crews/first-crew) when:** You need autonomous problem-solving, creative collaboration, or exploratory tasks
  * **Choose[Flows](/en/guides/flows/first-flow) when:** You require deterministic outcomes, auditability, or precise control over execution
  * **Combine both when:** Your application needs both structured processes and pockets of autonomous intelligence



## 

​

Why Choose CrewAI?

  * 🧠 **Autonomous Operation** : Agents make intelligent decisions based on their roles and available tools
  * 📝 **Natural Interaction** : Agents communicate and collaborate like human team members
  * 🛠️ **Extensible Design** : Easy to add new tools, roles, and capabilities
  * 🚀 **Production Ready** : Built for reliability and scalability in real-world applications
  * 🔒 **Security-Focused** : Designed with enterprise security requirements in mind
  * 💰 **Cost-Efficient** : Optimized to minimize token usage and API calls



## 

​

Ready to Start Building?

## [Build Your First CrewStep-by-step tutorial to create a collaborative AI team that works together to solve complex problems.](/en/guides/crews/first-crew)## [Build Your First FlowLearn how to create structured, event-driven workflows with precise control over execution.](/en/guides/flows/first-flow)

## [Install CrewAIGet started with CrewAI in your development environment.](/en/installation)## [Quick StartFollow our quickstart guide to create your first CrewAI agent and get hands-on experience.](en/quickstart)## [Join the CommunityConnect with other developers, get help, and share your CrewAI experiences.](https://community.crewai.com)

Was this page helpful?

YesNo

[InstallationNext](/en/installation)

Ctrl+I

[website](https://crewai.com)[x](https://x.com/crewAIInc)[github](https://github.com/crewAIInc/crewAI)[linkedin](https://www.linkedin.com/company/crewai-inc)[youtube](https://youtube.com/@crewAIInc)[reddit](https://www.reddit.com/r/crewAIInc/)

[Powered by Mintlify](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=crewai)

Assistant

Responses are generated using AI and may contain mistakes.

![CrewAI Framework Overview](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=92b76be34b84b36771e0a8eed8976966)

![CrewAI Framework Overview](https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=7900e4cdad93fd37bbcd2f1f2f38b40b)


---

# Source: https://docs.crewai.com/en/installation

Skip to main content

[CrewAI home page![light logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)![dark logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)](/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl K

Search...

Navigation

Get Started

Installation

[Home](/)[Documentation](/en/introduction)[AOP](/en/enterprise/introduction)[API Reference](/en/api-reference/introduction)[Examples](/en/examples/example)[Changelog](/en/changelog)

  * [Website](https://crewai.com)
  * [Forum](https://community.crewai.com)
  * [Blog](https://blog.crewai.com)
  * [CrewGPT](https://chatgpt.com/g/g-qqTuUWsBY-crewai-assistant)



##### Get Started

  * [Introduction](/en/introduction)
  * [Installation](/en/installation)
  * [Quickstart](/en/quickstart)



##### Guides

  * Strategy

  * Agents

  * Crews

  * Flows

  * Advanced




##### Core Concepts

  * [Agents](/en/concepts/agents)
  * [Tasks](/en/concepts/tasks)
  * [Crews](/en/concepts/crews)
  * [Flows](/en/concepts/flows)
  * [Knowledge](/en/concepts/knowledge)
  * [LLMs](/en/concepts/llms)
  * [Processes](/en/concepts/processes)
  * [Collaboration](/en/concepts/collaboration)
  * [Training](/en/concepts/training)
  * [Memory](/en/concepts/memory)
  * [Reasoning](/en/concepts/reasoning)
  * [Planning](/en/concepts/planning)
  * [Testing](/en/concepts/testing)
  * [CLI](/en/concepts/cli)
  * [Tools](/en/concepts/tools)
  * [Event Listeners](/en/concepts/event-listener)



##### MCP Integration

  * [MCP Servers as Tools in CrewAI](/en/mcp/overview)
  * [MCP DSL Integration](/en/mcp/dsl-integration)
  * [Stdio Transport](/en/mcp/stdio)
  * [SSE Transport](/en/mcp/sse)
  * [Streamable HTTP Transport](/en/mcp/streamable-http)
  * [Connecting to Multiple MCP Servers](/en/mcp/multiple-servers)
  * [MCP Security Considerations](/en/mcp/security)



##### Tools

  * [Tools Overview](/en/tools/overview)
  * File & Document

  * Web Scraping & Browsing

  * Search & Research

  * Database & Data

  * AI & Machine Learning

  * Cloud & Storage

  * Integrations

  * Automation




##### Observability

  * [CrewAI Tracing](/en/observability/tracing)
  * [Overview](/en/observability/overview)
  * [Arize Phoenix](/en/observability/arize-phoenix)
  * [Braintrust](/en/observability/braintrust)
  * [Datadog Integration](/en/observability/datadog)
  * [LangDB Integration](/en/observability/langdb)
  * [Langfuse Integration](/en/observability/langfuse)
  * [Langtrace Integration](/en/observability/langtrace)
  * [Maxim Integration](/en/observability/maxim)
  * [MLflow Integration](/en/observability/mlflow)
  * [Neatlogs Integration](/en/observability/neatlogs)
  * [OpenLIT Integration](/en/observability/openlit)
  * [Opik Integration](/en/observability/opik)
  * [Patronus AI Evaluation](/en/observability/patronus-evaluation)
  * [Portkey Integration](/en/observability/portkey)
  * [Weave Integration](/en/observability/weave)
  * [TrueFoundry Integration](/en/observability/truefoundry)



##### Learn

  * [Overview](/en/learn/overview)
  * [Strategic LLM Selection Guide](/en/learn/llm-selection-guide)
  * [Conditional Tasks](/en/learn/conditional-tasks)
  * [Coding Agents](/en/learn/coding-agents)
  * [Create Custom Tools](/en/learn/create-custom-tools)
  * [Custom LLM Implementation](/en/learn/custom-llm)
  * [Custom Manager Agent](/en/learn/custom-manager-agent)
  * [Customize Agents](/en/learn/customizing-agents)
  * [Image Generation with DALL-E](/en/learn/dalle-image-generation)
  * [Force Tool Output as Result](/en/learn/force-tool-output-as-result)
  * [Hierarchical Process](/en/learn/hierarchical-process)
  * [Human Input on Execution](/en/learn/human-input-on-execution)
  * [Human-in-the-Loop (HITL) Workflows](/en/learn/human-in-the-loop)
  * [Kickoff Crew Asynchronously](/en/learn/kickoff-async)
  * [Kickoff Crew for Each](/en/learn/kickoff-for-each)
  * [Connect to any LLM](/en/learn/llm-connections)
  * [Using Multimodal Agents](/en/learn/multimodal-agents)
  * [Replay Tasks from Latest Crew Kickoff](/en/learn/replay-tasks-from-latest-crew-kickoff)
  * [Sequential Processes](/en/learn/sequential-process)
  * [Using Annotations in crew.py](/en/learn/using-annotations)
  * [Execution Hooks Overview](/en/learn/execution-hooks)
  * [LLM Call Hooks](/en/learn/llm-hooks)
  * [Tool Call Hooks](/en/learn/tool-hooks)



##### Telemetry

  * [Telemetry](/en/telemetry)



Get Started

# Installation

Copy page

Get started with CrewAI - Install, configure, and build your first AI crew

Copy page

## 

​

Video Tutorial

Watch this video tutorial for a step-by-step demonstration of the installation process:

## 

​

Text Tutorial

**Python Version Requirements** CrewAI requires `Python >=3.10 and <3.14`. Here’s how to check your version:

Copy

Ask AI
    
    
    python3 --version
    

If you need to update Python, visit [python.org/downloads](https://python.org/downloads)

**OpenAI SDK Requirement** CrewAI 0.175.0 requires `openai >= 1.13.3`. If you manage dependencies yourself, ensure your environment satisfies this constraint to avoid import/runtime issues.

CrewAI uses the `uv` as its dependency management and package handling tool. It simplifies project setup and execution, offering a seamless experience. If you haven’t installed `uv` yet, follow **step 1** to quickly get it set up on your system, else you can skip to **step 2**.

1

Install uv

  * **On macOS/Linux:** Use `curl` to download the script and execute it with `sh`:

Copy

Ask AI
        
        curl -LsSf https://astral.sh/uv/install.sh | sh
        

If your system doesn’t have `curl`, you can use `wget`:

Copy

Ask AI
        
        wget -qO- https://astral.sh/uv/install.sh | sh
        

  * **On Windows:** Use `irm` to download the script and `iex` to execute it:

Copy

Ask AI
        
        powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
        

If you run into any issues, refer to [UV’s installation guide](https://docs.astral.sh/uv/getting-started/installation/) for more information.



2

Install CrewAI 🚀

  * Run the following command to install `crewai` CLI:

Copy

Ask AI
        
        uv tool install crewai
        

If you encounter a `PATH` warning, run this command to update your shell:

Copy

Ask AI
        
        uv tool update-shell
        

If you encounter the `chroma-hnswlib==0.7.6` build error (`fatal error C1083: Cannot open include file: 'float.h'`) on Windows, install [Visual Studio Build Tools](https://visualstudio.microsoft.com/downloads/) with _Desktop development with C++_.

  * To verify that `crewai` is installed, run:

Copy

Ask AI
        
        uv tool list
        

  * You should see something like:

Copy

Ask AI
        
        crewai v0.102.0
        - crewai
        

  * If you need to update `crewai`, run:

Copy

Ask AI
        
        uv tool install crewai --upgrade
        




Installation successful! You’re ready to create your first crew! 🎉

# 

​

Creating a CrewAI Project

We recommend using the `YAML` template scaffolding for a structured approach to defining agents and tasks. Here’s how to get started:

1

Generate Project Scaffolding

  * Run the `crewai` CLI command:

Copy

Ask AI
        
        crewai create crew <your_project_name>
        

  * This creates a new project with the following structure:

Copy

Ask AI
        
        my_project/
        ├── .gitignore
        ├── knowledge/
        ├── pyproject.toml
        ├── README.md
        ├── .env
        └── src/
            └── my_project/
                ├── __init__.py
                ├── main.py
                ├── crew.py
                ├── tools/
                │   ├── custom_tool.py
                │   └── __init__.py
                └── config/
                    ├── agents.yaml
                    └── tasks.yaml
        




2

Customize Your Project

  * Your project will contain these essential files:

File| Purpose  
---|---  
`agents.yaml`| Define your AI agents and their roles  
`tasks.yaml`| Set up agent tasks and workflows  
`.env`| Store API keys and environment variables  
`main.py`| Project entry point and execution flow  
`crew.py`| Crew orchestration and coordination  
`tools/`| Directory for custom agent tools  
`knowledge/`| Directory for knowledge base  
  
  * Start by editing `agents.yaml` and `tasks.yaml` to define your crew’s behavior.
  * Keep sensitive information like API keys in `.env`.



3

Run your Crew

  * Before you run your crew, make sure to run: 

Copy

Ask AI
        
        crewai install
        

  * If you need to install additional packages, use: 

Copy

Ask AI
        
        uv add <package-name>
        

  * To run your crew, execute the following command in the root of your project: 

Copy

Ask AI
        
        crewai run
        




## 

​

Enterprise Installation Options

For teams and organizations, CrewAI offers enterprise deployment options that eliminate setup complexity:

### 

​

CrewAI AOP (SaaS)

  * Zero installation required - just sign up for free at [app.crewai.com](https://app.crewai.com)
  * Automatic updates and maintenance
  * Managed infrastructure and scaling
  * Build Crews with no Code



### 

​

CrewAI Factory (Self-hosted)

  * Containerized deployment for your infrastructure
  * Supports any hyperscaler including on prem deployments
  * Integration with your existing security systems

## [Explore Enterprise OptionsLearn about CrewAI’s enterprise offerings and schedule a demo](https://crewai.com/enterprise)

## 

​

Next Steps

## [Build Your First AgentFollow our quickstart guide to create your first CrewAI agent and get hands-on experience.](/en/quickstart)## [Join the CommunityConnect with other developers, get help, and share your CrewAI experiences.](https://community.crewai.com)

Was this page helpful?

YesNo

[IntroductionPrevious](/en/introduction)[QuickstartNext](/en/quickstart)

Ctrl+I

[website](https://crewai.com)[x](https://x.com/crewAIInc)[github](https://github.com/crewAIInc/crewAI)[linkedin](https://www.linkedin.com/company/crewai-inc)[youtube](https://youtube.com/@crewAIInc)[reddit](https://www.reddit.com/r/crewAIInc/)

[Powered by Mintlify](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=crewai)

Assistant

Responses are generated using AI and may contain mistakes.


---

# Source: https://docs.crewai.com/en/quickstart

Skip to main content

[CrewAI home page![light logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)![dark logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)](/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl K

Search...

Navigation

Get Started

Quickstart

[Home](/)[Documentation](/en/introduction)[AOP](/en/enterprise/introduction)[API Reference](/en/api-reference/introduction)[Examples](/en/examples/example)[Changelog](/en/changelog)

  * [Website](https://crewai.com)
  * [Forum](https://community.crewai.com)
  * [Blog](https://blog.crewai.com)
  * [CrewGPT](https://chatgpt.com/g/g-qqTuUWsBY-crewai-assistant)



##### Get Started

  * [Introduction](/en/introduction)
  * [Installation](/en/installation)
  * [Quickstart](/en/quickstart)



##### Guides

  * Strategy

  * Agents

  * Crews

  * Flows

  * Advanced




##### Core Concepts

  * [Agents](/en/concepts/agents)
  * [Tasks](/en/concepts/tasks)
  * [Crews](/en/concepts/crews)
  * [Flows](/en/concepts/flows)
  * [Knowledge](/en/concepts/knowledge)
  * [LLMs](/en/concepts/llms)
  * [Processes](/en/concepts/processes)
  * [Collaboration](/en/concepts/collaboration)
  * [Training](/en/concepts/training)
  * [Memory](/en/concepts/memory)
  * [Reasoning](/en/concepts/reasoning)
  * [Planning](/en/concepts/planning)
  * [Testing](/en/concepts/testing)
  * [CLI](/en/concepts/cli)
  * [Tools](/en/concepts/tools)
  * [Event Listeners](/en/concepts/event-listener)



##### MCP Integration

  * [MCP Servers as Tools in CrewAI](/en/mcp/overview)
  * [MCP DSL Integration](/en/mcp/dsl-integration)
  * [Stdio Transport](/en/mcp/stdio)
  * [SSE Transport](/en/mcp/sse)
  * [Streamable HTTP Transport](/en/mcp/streamable-http)
  * [Connecting to Multiple MCP Servers](/en/mcp/multiple-servers)
  * [MCP Security Considerations](/en/mcp/security)



##### Tools

  * [Tools Overview](/en/tools/overview)
  * File & Document

  * Web Scraping & Browsing

  * Search & Research

  * Database & Data

  * AI & Machine Learning

  * Cloud & Storage

  * Integrations

  * Automation




##### Observability

  * [CrewAI Tracing](/en/observability/tracing)
  * [Overview](/en/observability/overview)
  * [Arize Phoenix](/en/observability/arize-phoenix)
  * [Braintrust](/en/observability/braintrust)
  * [Datadog Integration](/en/observability/datadog)
  * [LangDB Integration](/en/observability/langdb)
  * [Langfuse Integration](/en/observability/langfuse)
  * [Langtrace Integration](/en/observability/langtrace)
  * [Maxim Integration](/en/observability/maxim)
  * [MLflow Integration](/en/observability/mlflow)
  * [Neatlogs Integration](/en/observability/neatlogs)
  * [OpenLIT Integration](/en/observability/openlit)
  * [Opik Integration](/en/observability/opik)
  * [Patronus AI Evaluation](/en/observability/patronus-evaluation)
  * [Portkey Integration](/en/observability/portkey)
  * [Weave Integration](/en/observability/weave)
  * [TrueFoundry Integration](/en/observability/truefoundry)



##### Learn

  * [Overview](/en/learn/overview)
  * [Strategic LLM Selection Guide](/en/learn/llm-selection-guide)
  * [Conditional Tasks](/en/learn/conditional-tasks)
  * [Coding Agents](/en/learn/coding-agents)
  * [Create Custom Tools](/en/learn/create-custom-tools)
  * [Custom LLM Implementation](/en/learn/custom-llm)
  * [Custom Manager Agent](/en/learn/custom-manager-agent)
  * [Customize Agents](/en/learn/customizing-agents)
  * [Image Generation with DALL-E](/en/learn/dalle-image-generation)
  * [Force Tool Output as Result](/en/learn/force-tool-output-as-result)
  * [Hierarchical Process](/en/learn/hierarchical-process)
  * [Human Input on Execution](/en/learn/human-input-on-execution)
  * [Human-in-the-Loop (HITL) Workflows](/en/learn/human-in-the-loop)
  * [Kickoff Crew Asynchronously](/en/learn/kickoff-async)
  * [Kickoff Crew for Each](/en/learn/kickoff-for-each)
  * [Connect to any LLM](/en/learn/llm-connections)
  * [Using Multimodal Agents](/en/learn/multimodal-agents)
  * [Replay Tasks from Latest Crew Kickoff](/en/learn/replay-tasks-from-latest-crew-kickoff)
  * [Sequential Processes](/en/learn/sequential-process)
  * [Using Annotations in crew.py](/en/learn/using-annotations)
  * [Execution Hooks Overview](/en/learn/execution-hooks)
  * [LLM Call Hooks](/en/learn/llm-hooks)
  * [Tool Call Hooks](/en/learn/tool-hooks)



##### Telemetry

  * [Telemetry](/en/telemetry)



Get Started

# Quickstart

Copy page

Build your first AI agent with CrewAI in under 5 minutes.

Copy page

## 

​

Build your first CrewAI Agent

Let’s create a simple crew that will help us `research` and `report` on the `latest AI developments` for a given topic or subject. Before we proceed, make sure you have finished installing CrewAI. If you haven’t installed them yet, you can do so by following the [installation guide](/en/installation). Follow the steps below to get Crewing! 🚣‍♂️

1

Create your crew

Create a new crew project by running the following command in your terminal. This will create a new directory called `latest-ai-development` with the basic structure for your crew.

Terminal

Copy

Ask AI
    
    
    crewai create crew latest-ai-development
    

2

Navigate to your new crew project

Terminal

Copy

Ask AI
    
    
    cd latest_ai_development
    

3

Modify your `agents.yaml` file

You can also modify the agents as needed to fit your use case or copy and paste as is to your project. Any variable interpolated in your `agents.yaml` and `tasks.yaml` files like `{topic}` will be replaced by the value of the variable in the `main.py` file.

agents.yaml

Copy

Ask AI
    
    
    # src/latest_ai_development/config/agents.yaml
    researcher:
      role: >
        {topic} Senior Data Researcher
      goal: >
        Uncover cutting-edge developments in {topic}
      backstory: >
        You're a seasoned researcher with a knack for uncovering the latest
        developments in {topic}. Known for your ability to find the most relevant
        information and present it in a clear and concise manner.
    
    reporting_analyst:
      role: >
        {topic} Reporting Analyst
      goal: >
        Create detailed reports based on {topic} data analysis and research findings
      backstory: >
        You're a meticulous analyst with a keen eye for detail. You're known for
        your ability to turn complex data into clear and concise reports, making
        it easy for others to understand and act on the information you provide.
    

4

Modify your `tasks.yaml` file

tasks.yaml

Copy

Ask AI
    
    
    # src/latest_ai_development/config/tasks.yaml
    research_task:
      description: >
        Conduct a thorough research about {topic}
        Make sure you find any interesting and relevant information given
        the current year is 2025.
      expected_output: >
        A list with 10 bullet points of the most relevant information about {topic}
      agent: researcher
    
    reporting_task:
      description: >
        Review the context you got and expand each topic into a full section for a report.
        Make sure the report is detailed and contains any and all relevant information.
      expected_output: >
        A fully fledge reports with the mains topics, each with a full section of information.
        Formatted as markdown without '```'
      agent: reporting_analyst
      output_file: report.md
    

5

Modify your `crew.py` file

crew.py

Copy

Ask AI
    
    
    # src/latest_ai_development/crew.py
    from crewai import Agent, Crew, Process, Task
    from crewai.project import CrewBase, agent, crew, task
    from crewai_tools import SerperDevTool
    from crewai.agents.agent_builder.base_agent import BaseAgent
    from typing import List
    
    @CrewBase
    class LatestAiDevelopmentCrew():
      """LatestAiDevelopment crew"""
    
      agents: List[BaseAgent]
      tasks: List[Task]
    
      @agent
      def researcher(self) -> Agent:
        return Agent(
          config=self.agents_config['researcher'], # type: ignore[index]
          verbose=True,
          tools=[SerperDevTool()]
        )
    
      @agent
      def reporting_analyst(self) -> Agent:
        return Agent(
          config=self.agents_config['reporting_analyst'], # type: ignore[index]
          verbose=True
        )
    
      @task
      def research_task(self) -> Task:
        return Task(
          config=self.tasks_config['research_task'], # type: ignore[index]
        )
    
      @task
      def reporting_task(self) -> Task:
        return Task(
          config=self.tasks_config['reporting_task'], # type: ignore[index]
          output_file='output/report.md' # This is the file that will be contain the final report.
        )
    
      @crew
      def crew(self) -> Crew:
        """Creates the LatestAiDevelopment crew"""
        return Crew(
          agents=self.agents, # Automatically created by the @agent decorator
          tasks=self.tasks, # Automatically created by the @task decorator
          process=Process.sequential,
          verbose=True,
        )
    

6

[Optional] Add before and after crew functions

crew.py

Copy

Ask AI
    
    
    # src/latest_ai_development/crew.py
    from crewai import Agent, Crew, Process, Task
    from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff
    from crewai_tools import SerperDevTool
    
    @CrewBase
    class LatestAiDevelopmentCrew():
      """LatestAiDevelopment crew"""
    
      @before_kickoff
      def before_kickoff_function(self, inputs):
        print(f"Before kickoff function with inputs: {inputs}")
        return inputs # You can return the inputs or modify them as needed
    
      @after_kickoff
      def after_kickoff_function(self, result):
        print(f"After kickoff function with result: {result}")
        return result # You can return the result or modify it as needed
    
      # ... remaining code
    

7

Feel free to pass custom inputs to your crew

For example, you can pass the `topic` input to your crew to customize the research and reporting.

main.py

Copy

Ask AI
    
    
    #!/usr/bin/env python
    # src/latest_ai_development/main.py
    import sys
    from latest_ai_development.crew import LatestAiDevelopmentCrew
    
    def run():
      """
      Run the crew.
      """
      inputs = {
        'topic': 'AI Agents'
      }
      LatestAiDevelopmentCrew().crew().kickoff(inputs=inputs)
    

8

Set your environment variables

Before running your crew, make sure you have the following keys set as environment variables in your `.env` file:

  * A [Serper.dev](https://serper.dev/) API key: `SERPER_API_KEY=YOUR_KEY_HERE`
  * The configuration for your choice of model, such as an API key. See the [LLM setup guide](/en/concepts/llms#setting-up-your-llm) to learn how to configure models from any provider.



9

Lock and install the dependencies

  * Lock the dependencies and install them by using the CLI command: 

Terminal

Copy

Ask AI
        
        crewai install
        

  * If you have additional packages that you want to install, you can do so by running: 

Terminal

Copy

Ask AI
        
        uv add <package-name>
        




10

Run your crew

  * To run your crew, execute the following command in the root of your project: 

Terminal

Copy

Ask AI
        
        crewai run
        




11

Enterprise Alternative: Create in Crew Studio

For CrewAI AOP users, you can create the same crew without writing code:

  1. Log in to your CrewAI AOP account (create a free account at [app.crewai.com](https://app.crewai.com))
  2. Open Crew Studio
  3. Type what is the automation you’re trying to build
  4. Create your tasks visually and connect them in sequence
  5. Configure your inputs and click “Download Code” or “Deploy” ![Crew Studio Quickstart](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=c4f5428b111816273b3b53d9cef14fad)

## [Try CrewAI AOPStart your free account at CrewAI AOP](https://app.crewai.com)

12

View your final report

You should see the output in the console and the `report.md` file should be created in the root of your project with the final report.Here’s an example of what the report should look like:

output/report.md

Copy

Ask AI
    
    
    # Comprehensive Report on the Rise and Impact of AI Agents in 2025
    
    ## 1. Introduction to AI Agents
    In 2025, Artificial Intelligence (AI) agents are at the forefront of innovation across various industries. As intelligent systems that can perform tasks typically requiring human cognition, AI agents are paving the way for significant advancements in operational efficiency, decision-making, and overall productivity within sectors like Human Resources (HR) and Finance. This report aims to detail the rise of AI agents, their frameworks, applications, and potential implications on the workforce.
    
    ## 2. Benefits of AI Agents
    AI agents bring numerous advantages that are transforming traditional work environments. Key benefits include:
    
    - **Task Automation**: AI agents can carry out repetitive tasks such as data entry, scheduling, and payroll processing without human intervention, greatly reducing the time and resources spent on these activities.
    - **Improved Efficiency**: By quickly processing large datasets and performing analyses that would take humans significantly longer, AI agents enhance operational efficiency. This allows teams to focus on strategic tasks that require higher-level thinking.
    - **Enhanced Decision-Making**: AI agents can analyze trends and patterns in data, provide insights, and even suggest actions, helping stakeholders make informed decisions based on factual data rather than intuition alone.
    
    ## 3. Popular AI Agent Frameworks
    Several frameworks have emerged to facilitate the development of AI agents, each with its own unique features and capabilities. Some of the most popular frameworks include:
    
    - **Autogen**: A framework designed to streamline the development of AI agents through automation of code generation.
    - **Semantic Kernel**: Focuses on natural language processing and understanding, enabling agents to comprehend user intentions better.
    - **Promptflow**: Provides tools for developers to create conversational agents that can navigate complex interactions seamlessly.
    - **Langchain**: Specializes in leveraging various APIs to ensure agents can access and utilize external data effectively.
    - **CrewAI**: Aimed at collaborative environments, CrewAI strengthens teamwork by facilitating communication through AI-driven insights.
    - **MemGPT**: Combines memory-optimized architectures with generative capabilities, allowing for more personalized interactions with users.
    
    These frameworks empower developers to build versatile and intelligent agents that can engage users, perform advanced analytics, and execute various tasks aligned with organizational goals.
    
    ## 4. AI Agents in Human Resources
    AI agents are revolutionizing HR practices by automating and optimizing key functions:
    
    - **Recruiting**: AI agents can screen resumes, schedule interviews, and even conduct initial assessments, thus accelerating the hiring process while minimizing biases.
    - **Succession Planning**: AI systems analyze employee performance data and potential, helping organizations identify future leaders and plan appropriate training.
    - **Employee Engagement**: Chatbots powered by AI can facilitate feedback loops between employees and management, promoting an open culture and addressing concerns promptly.
    
    As AI continues to evolve, HR departments leveraging these agents can realize substantial improvements in both efficiency and employee satisfaction.
    
    ## 5. AI Agents in Finance
    The finance sector is seeing extensive integration of AI agents that enhance financial practices:
    
    - **Expense Tracking**: Automated systems manage and monitor expenses, flagging anomalies and offering recommendations based on spending patterns.
    - **Risk Assessment**: AI models assess credit risk and uncover potential fraud by analyzing transaction data and behavioral patterns.
    - **Investment Decisions**: AI agents provide stock predictions and analytics based on historical data and current market conditions, empowering investors with informative insights.
    
    The incorporation of AI agents into finance is fostering a more responsive and risk-aware financial landscape.
    
    ## 6. Market Trends and Investments
    The growth of AI agents has attracted significant investment, especially amidst the rising popularity of chatbots and generative AI technologies. Companies and entrepreneurs are eager to explore the potential of these systems, recognizing their ability to streamline operations and improve customer engagement.
    
    Conversely, corporations like Microsoft are taking strides to integrate AI agents into their product offerings, with enhancements to their Copilot 365 applications. This strategic move emphasizes the importance of AI literacy in the modern workplace and indicates the stabilizing of AI agents as essential business tools.
    
    ## 7. Future Predictions and Implications
    Experts predict that AI agents will transform essential aspects of work life. As we look toward the future, several anticipated changes include:
    
    - Enhanced integration of AI agents across all business functions, creating interconnected systems that leverage data from various departmental silos for comprehensive decision-making.
    - Continued advancement of AI technologies, resulting in smarter, more adaptable agents capable of learning and evolving from user interactions.
    - Increased regulatory scrutiny to ensure ethical use, especially concerning data privacy and employee surveillance as AI agents become more prevalent.
    
    To stay competitive and harness the full potential of AI agents, organizations must remain vigilant about latest developments in AI technology and consider continuous learning and adaptation in their strategic planning.
    
    ## 8. Conclusion
    The emergence of AI agents is undeniably reshaping the workplace landscape in 5. With their ability to automate tasks, enhance efficiency, and improve decision-making, AI agents are critical in driving operational success. Organizations must embrace and adapt to AI developments to thrive in an increasingly digital business environment.
    

Congratulations!You have successfully set up your crew project and are ready to start building your own agentic workflows!

### 

​

Note on Consistency in Naming

The names you use in your YAML files (`agents.yaml` and `tasks.yaml`) should match the method names in your Python code. For example, you can reference the agent for specific tasks from `tasks.yaml` file. This naming consistency allows CrewAI to automatically link your configurations with your code; otherwise, your task won’t recognize the reference properly.

#### 

​

Example References

Note how we use the same name for the agent in the `agents.yaml` (`email_summarizer`) file as the method name in the `crew.py` (`email_summarizer`) file.

agents.yaml

Copy

Ask AI
    
    
    email_summarizer:
        role: >
          Email Summarizer
        goal: >
          Summarize emails into a concise and clear summary
        backstory: >
          You will create a 5 bullet point summary of the report
        llm: provider/model-id  # Add your choice of model here
    

Note how we use the same name for the task in the `tasks.yaml` (`email_summarizer_task`) file as the method name in the `crew.py` (`email_summarizer_task`) file.

tasks.yaml

Copy

Ask AI
    
    
    email_summarizer_task:
        description: >
          Summarize the email into a 5 bullet point summary
        expected_output: >
          A 5 bullet point summary of the email
        agent: email_summarizer
        context:
          - reporting_task
          - research_task
    

## 

​

Deploying Your Crew

The easiest way to deploy your crew to production is through [CrewAI AOP](http://app.crewai.com). Watch this video tutorial for a step-by-step demonstration of deploying your crew to [CrewAI AOP](http://app.crewai.com) using the CLI.

## [Deploy on EnterpriseGet started with CrewAI AOP and deploy your crew in a production environment with just a few clicks.](http://app.crewai.com)## [Join the CommunityJoin our open source community to discuss ideas, share your projects, and connect with other CrewAI developers.](https://community.crewai.com)

Was this page helpful?

YesNo

[InstallationPrevious](/en/installation)[Evaluating Use Cases for CrewAINext](/en/guides/concepts/evaluating-use-cases)

Ctrl+I

[website](https://crewai.com)[x](https://x.com/crewAIInc)[github](https://github.com/crewAIInc/crewAI)[linkedin](https://www.linkedin.com/company/crewai-inc)[youtube](https://youtube.com/@crewAIInc)[reddit](https://www.reddit.com/r/crewAIInc/)

[Powered by Mintlify](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=crewai)

Assistant

Responses are generated using AI and may contain mistakes.

![Crew Studio Quickstart](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=ae6f0c18ef3679b5466177710fbc4a94)


---

# Source: https://docs.crewai.com/en/concepts/agents

Skip to main content

[CrewAI home page![light logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)![dark logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)](/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl K

Search...

Navigation

Core Concepts

Agents

[Home](/)[Documentation](/en/introduction)[AOP](/en/enterprise/introduction)[API Reference](/en/api-reference/introduction)[Examples](/en/examples/example)[Changelog](/en/changelog)

  * [Website](https://crewai.com)
  * [Forum](https://community.crewai.com)
  * [Blog](https://blog.crewai.com)
  * [CrewGPT](https://chatgpt.com/g/g-qqTuUWsBY-crewai-assistant)



##### Get Started

  * [Introduction](/en/introduction)
  * [Installation](/en/installation)
  * [Quickstart](/en/quickstart)



##### Guides

  * Strategy

  * Agents

  * Crews

  * Flows

  * Advanced




##### Core Concepts

  * [Agents](/en/concepts/agents)
  * [Tasks](/en/concepts/tasks)
  * [Crews](/en/concepts/crews)
  * [Flows](/en/concepts/flows)
  * [Knowledge](/en/concepts/knowledge)
  * [LLMs](/en/concepts/llms)
  * [Processes](/en/concepts/processes)
  * [Collaboration](/en/concepts/collaboration)
  * [Training](/en/concepts/training)
  * [Memory](/en/concepts/memory)
  * [Reasoning](/en/concepts/reasoning)
  * [Planning](/en/concepts/planning)
  * [Testing](/en/concepts/testing)
  * [CLI](/en/concepts/cli)
  * [Tools](/en/concepts/tools)
  * [Event Listeners](/en/concepts/event-listener)



##### MCP Integration

  * [MCP Servers as Tools in CrewAI](/en/mcp/overview)
  * [MCP DSL Integration](/en/mcp/dsl-integration)
  * [Stdio Transport](/en/mcp/stdio)
  * [SSE Transport](/en/mcp/sse)
  * [Streamable HTTP Transport](/en/mcp/streamable-http)
  * [Connecting to Multiple MCP Servers](/en/mcp/multiple-servers)
  * [MCP Security Considerations](/en/mcp/security)



##### Tools

  * [Tools Overview](/en/tools/overview)
  * File & Document

  * Web Scraping & Browsing

  * Search & Research

  * Database & Data

  * AI & Machine Learning

  * Cloud & Storage

  * Integrations

  * Automation




##### Observability

  * [CrewAI Tracing](/en/observability/tracing)
  * [Overview](/en/observability/overview)
  * [Arize Phoenix](/en/observability/arize-phoenix)
  * [Braintrust](/en/observability/braintrust)
  * [Datadog Integration](/en/observability/datadog)
  * [LangDB Integration](/en/observability/langdb)
  * [Langfuse Integration](/en/observability/langfuse)
  * [Langtrace Integration](/en/observability/langtrace)
  * [Maxim Integration](/en/observability/maxim)
  * [MLflow Integration](/en/observability/mlflow)
  * [Neatlogs Integration](/en/observability/neatlogs)
  * [OpenLIT Integration](/en/observability/openlit)
  * [Opik Integration](/en/observability/opik)
  * [Patronus AI Evaluation](/en/observability/patronus-evaluation)
  * [Portkey Integration](/en/observability/portkey)
  * [Weave Integration](/en/observability/weave)
  * [TrueFoundry Integration](/en/observability/truefoundry)



##### Learn

  * [Overview](/en/learn/overview)
  * [Strategic LLM Selection Guide](/en/learn/llm-selection-guide)
  * [Conditional Tasks](/en/learn/conditional-tasks)
  * [Coding Agents](/en/learn/coding-agents)
  * [Create Custom Tools](/en/learn/create-custom-tools)
  * [Custom LLM Implementation](/en/learn/custom-llm)
  * [Custom Manager Agent](/en/learn/custom-manager-agent)
  * [Customize Agents](/en/learn/customizing-agents)
  * [Image Generation with DALL-E](/en/learn/dalle-image-generation)
  * [Force Tool Output as Result](/en/learn/force-tool-output-as-result)
  * [Hierarchical Process](/en/learn/hierarchical-process)
  * [Human Input on Execution](/en/learn/human-input-on-execution)
  * [Human-in-the-Loop (HITL) Workflows](/en/learn/human-in-the-loop)
  * [Kickoff Crew Asynchronously](/en/learn/kickoff-async)
  * [Kickoff Crew for Each](/en/learn/kickoff-for-each)
  * [Connect to any LLM](/en/learn/llm-connections)
  * [Using Multimodal Agents](/en/learn/multimodal-agents)
  * [Replay Tasks from Latest Crew Kickoff](/en/learn/replay-tasks-from-latest-crew-kickoff)
  * [Sequential Processes](/en/learn/sequential-process)
  * [Using Annotations in crew.py](/en/learn/using-annotations)
  * [Execution Hooks Overview](/en/learn/execution-hooks)
  * [LLM Call Hooks](/en/learn/llm-hooks)
  * [Tool Call Hooks](/en/learn/tool-hooks)



##### Telemetry

  * [Telemetry](/en/telemetry)



Core Concepts

# Agents

Copy page

Detailed guide on creating and managing agents within the CrewAI framework.

Copy page

## 

​

Overview of an Agent

In the CrewAI framework, an `Agent` is an autonomous unit that can:

  * Perform specific tasks
  * Make decisions based on its role and goal
  * Use tools to accomplish objectives
  * Communicate and collaborate with other agents
  * Maintain memory of interactions
  * Delegate tasks when allowed



Think of an agent as a specialized team member with specific skills, expertise, and responsibilities. For example, a `Researcher` agent might excel at gathering and analyzing information, while a `Writer` agent might be better at creating content.

CrewAI AOP includes a Visual Agent Builder that simplifies agent creation and configuration without writing code. Design your agents visually and test them in real-time.![Visual Agent Builder Screenshot](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=c4f5428b111816273b3b53d9cef14fad)The Visual Agent Builder enables:

  * Intuitive agent configuration with form-based interfaces
  * Real-time testing and validation
  * Template library with pre-configured agent types
  * Easy customization of agent attributes and behaviors



## 

​

Agent Attributes

Attribute| Parameter| Type| Description  
---|---|---|---  
**Role**| `role`| `str`| Defines the agent’s function and expertise within the crew.  
**Goal**| `goal`| `str`| The individual objective that guides the agent’s decision-making.  
**Backstory**| `backstory`| `str`| Provides context and personality to the agent, enriching interactions.  
**LLM** _(optional)_| `llm`| `Union[str, LLM, Any]`| Language model that powers the agent. Defaults to the model specified in `OPENAI_MODEL_NAME` or “gpt-4”.  
**Tools** _(optional)_| `tools`| `List[BaseTool]`| Capabilities or functions available to the agent. Defaults to an empty list.  
**Function Calling LLM** _(optional)_| `function_calling_llm`| `Optional[Any]`| Language model for tool calling, overrides crew’s LLM if specified.  
**Max Iterations** _(optional)_| `max_iter`| `int`| Maximum iterations before the agent must provide its best answer. Default is 20.  
**Max RPM** _(optional)_| `max_rpm`| `Optional[int]`| Maximum requests per minute to avoid rate limits.  
**Max Execution Time** _(optional)_| `max_execution_time`| `Optional[int]`| Maximum time (in seconds) for task execution.  
**Verbose** _(optional)_| `verbose`| `bool`| Enable detailed execution logs for debugging. Default is False.  
**Allow Delegation** _(optional)_| `allow_delegation`| `bool`| Allow the agent to delegate tasks to other agents. Default is False.  
**Step Callback** _(optional)_| `step_callback`| `Optional[Any]`| Function called after each agent step, overrides crew callback.  
**Cache** _(optional)_| `cache`| `bool`| Enable caching for tool usage. Default is True.  
**System Template** _(optional)_| `system_template`| `Optional[str]`| Custom system prompt template for the agent.  
**Prompt Template** _(optional)_| `prompt_template`| `Optional[str]`| Custom prompt template for the agent.  
**Response Template** _(optional)_| `response_template`| `Optional[str]`| Custom response template for the agent.  
**Allow Code Execution** _(optional)_| `allow_code_execution`| `Optional[bool]`| Enable code execution for the agent. Default is False.  
**Max Retry Limit** _(optional)_| `max_retry_limit`| `int`| Maximum number of retries when an error occurs. Default is 2.  
**Respect Context Window** _(optional)_| `respect_context_window`| `bool`| Keep messages under context window size by summarizing. Default is True.  
**Code Execution Mode** _(optional)_| `code_execution_mode`| `Literal["safe", "unsafe"]`| Mode for code execution: ‘safe’ (using Docker) or ‘unsafe’ (direct). Default is ‘safe’.  
**Multimodal** _(optional)_| `multimodal`| `bool`| Whether the agent supports multimodal capabilities. Default is False.  
**Inject Date** _(optional)_| `inject_date`| `bool`| Whether to automatically inject the current date into tasks. Default is False.  
**Date Format** _(optional)_| `date_format`| `str`| Format string for date when inject_date is enabled. Default is “%Y-%m-%d” (ISO format).  
**Reasoning** _(optional)_| `reasoning`| `bool`| Whether the agent should reflect and create a plan before executing a task. Default is False.  
**Max Reasoning Attempts** _(optional)_| `max_reasoning_attempts`| `Optional[int]`| Maximum number of reasoning attempts before executing the task. If None, will try until ready.  
**Embedder** _(optional)_| `embedder`| `Optional[Dict[str, Any]]`| Configuration for the embedder used by the agent.  
**Knowledge Sources** _(optional)_| `knowledge_sources`| `Optional[List[BaseKnowledgeSource]]`| Knowledge sources available to the agent.  
**Use System Prompt** _(optional)_| `use_system_prompt`| `Optional[bool]`| Whether to use system prompt (for o1 model support). Default is True.  
  
## 

​

Creating Agents

There are two ways to create agents in CrewAI: using **YAML configuration (recommended)** or defining them **directly in code**.

### 

​

YAML Configuration (Recommended)

Using YAML configuration provides a cleaner, more maintainable way to define agents. We strongly recommend using this approach in your CrewAI projects. After creating your CrewAI project as outlined in the [Installation](/en/installation) section, navigate to the `src/latest_ai_development/config/agents.yaml` file and modify the template to match your requirements.

Variables in your YAML files (like `{topic}`) will be replaced with values from your inputs when running the crew:

Code

Copy

Ask AI
    
    
    crew.kickoff(inputs={'topic': 'AI Agents'})
    

Here’s an example of how to configure agents using YAML:

agents.yaml

Copy

Ask AI
    
    
    # src/latest_ai_development/config/agents.yaml
    researcher:
      role: >
        {topic} Senior Data Researcher
      goal: >
        Uncover cutting-edge developments in {topic}
      backstory: >
        You're a seasoned researcher with a knack for uncovering the latest
        developments in {topic}. Known for your ability to find the most relevant
        information and present it in a clear and concise manner.
    
    reporting_analyst:
      role: >
        {topic} Reporting Analyst
      goal: >
        Create detailed reports based on {topic} data analysis and research findings
      backstory: >
        You're a meticulous analyst with a keen eye for detail. You're known for
        your ability to turn complex data into clear and concise reports, making
        it easy for others to understand and act on the information you provide.
    

To use this YAML configuration in your code, create a crew class that inherits from `CrewBase`:

Code

Copy

Ask AI
    
    
    # src/latest_ai_development/crew.py
    from crewai import Agent, Crew, Process
    from crewai.project import CrewBase, agent, crew
    from crewai_tools import SerperDevTool
    
    @CrewBase
    class LatestAiDevelopmentCrew():
      """LatestAiDevelopment crew"""
    
      agents_config = "config/agents.yaml"
    
      @agent
      def researcher(self) -> Agent:
        return Agent(
          config=self.agents_config['researcher'], # type: ignore[index]
          verbose=True,
          tools=[SerperDevTool()]
        )
    
      @agent
      def reporting_analyst(self) -> Agent:
        return Agent(
          config=self.agents_config['reporting_analyst'], # type: ignore[index]
          verbose=True
        )
    

The names you use in your YAML files (`agents.yaml`) should match the method names in your Python code.

### 

​

Direct Code Definition

You can create agents directly in code by instantiating the `Agent` class. Here’s a comprehensive example showing all available parameters:

Code

Copy

Ask AI
    
    
    from crewai import Agent
    from crewai_tools import SerperDevTool
    
    # Create an agent with all available parameters
    agent = Agent(
        role="Senior Data Scientist",
        goal="Analyze and interpret complex datasets to provide actionable insights",
        backstory="With over 10 years of experience in data science and machine learning, "
                  "you excel at finding patterns in complex datasets.",
        llm="gpt-4",  # Default: OPENAI_MODEL_NAME or "gpt-4"
        function_calling_llm=None,  # Optional: Separate LLM for tool calling
        verbose=False,  # Default: False
        allow_delegation=False,  # Default: False
        max_iter=20,  # Default: 20 iterations
        max_rpm=None,  # Optional: Rate limit for API calls
        max_execution_time=None,  # Optional: Maximum execution time in seconds
        max_retry_limit=2,  # Default: 2 retries on error
        allow_code_execution=False,  # Default: False
        code_execution_mode="safe",  # Default: "safe" (options: "safe", "unsafe")
        respect_context_window=True,  # Default: True
        use_system_prompt=True,  # Default: True
        multimodal=False,  # Default: False
        inject_date=False,  # Default: False
        date_format="%Y-%m-%d",  # Default: ISO format
        reasoning=False,  # Default: False
        max_reasoning_attempts=None,  # Default: None
        tools=[SerperDevTool()],  # Optional: List of tools
        knowledge_sources=None,  # Optional: List of knowledge sources
        embedder=None,  # Optional: Custom embedder configuration
        system_template=None,  # Optional: Custom system prompt template
        prompt_template=None,  # Optional: Custom prompt template
        response_template=None,  # Optional: Custom response template
        step_callback=None,  # Optional: Callback function for monitoring
    )
    

Let’s break down some key parameter combinations for common use cases:

#### 

​

Basic Research Agent

Code

Copy

Ask AI
    
    
    research_agent = Agent(
        role="Research Analyst",
        goal="Find and summarize information about specific topics",
        backstory="You are an experienced researcher with attention to detail",
        tools=[SerperDevTool()],
        verbose=True  # Enable logging for debugging
    )
    

#### 

​

Code Development Agent

Code

Copy

Ask AI
    
    
    dev_agent = Agent(
        role="Senior Python Developer",
        goal="Write and debug Python code",
        backstory="Expert Python developer with 10 years of experience",
        allow_code_execution=True,
        code_execution_mode="safe",  # Uses Docker for safety
        max_execution_time=300,  # 5-minute timeout
        max_retry_limit=3  # More retries for complex code tasks
    )
    

#### 

​

Long-Running Analysis Agent

Code

Copy

Ask AI
    
    
    analysis_agent = Agent(
        role="Data Analyst",
        goal="Perform deep analysis of large datasets",
        backstory="Specialized in big data analysis and pattern recognition",
        memory=True,
        respect_context_window=True,
        max_rpm=10,  # Limit API calls
        function_calling_llm="gpt-4o-mini"  # Cheaper model for tool calls
    )
    

#### 

​

Custom Template Agent

Code

Copy

Ask AI
    
    
    custom_agent = Agent(
        role="Customer Service Representative",
        goal="Assist customers with their inquiries",
        backstory="Experienced in customer support with a focus on satisfaction",
        system_template="""<|start_header_id|>system<|end_header_id|>
                            {{ .System }}<|eot_id|>""",
        prompt_template="""<|start_header_id|>user<|end_header_id|>
                            {{ .Prompt }}<|eot_id|>""",
        response_template="""<|start_header_id|>assistant<|end_header_id|>
                            {{ .Response }}<|eot_id|>""",
    )
    

#### 

​

Date-Aware Agent with Reasoning

Code

Copy

Ask AI
    
    
    strategic_agent = Agent(
        role="Market Analyst",
        goal="Track market movements with precise date references and strategic planning",
        backstory="Expert in time-sensitive financial analysis and strategic reporting",
        inject_date=True,  # Automatically inject current date into tasks
        date_format="%B %d, %Y",  # Format as "May 21, 2025"
        reasoning=True,  # Enable strategic planning
        max_reasoning_attempts=2,  # Limit planning iterations
        verbose=True
    )
    

#### 

​

Reasoning Agent

Code

Copy

Ask AI
    
    
    reasoning_agent = Agent(
        role="Strategic Planner",
        goal="Analyze complex problems and create detailed execution plans",
        backstory="Expert strategic planner who methodically breaks down complex challenges",
        reasoning=True,  # Enable reasoning and planning
        max_reasoning_attempts=3,  # Limit reasoning attempts
        max_iter=30,  # Allow more iterations for complex planning
        verbose=True
    )
    

#### 

​

Multimodal Agent

Code

Copy

Ask AI
    
    
    multimodal_agent = Agent(
        role="Visual Content Analyst",
        goal="Analyze and process both text and visual content",
        backstory="Specialized in multimodal analysis combining text and image understanding",
        multimodal=True,  # Enable multimodal capabilities
        verbose=True
    )
    

### 

​

Parameter Details

#### 

​

Critical Parameters

  * `role`, `goal`, and `backstory` are required and shape the agent’s behavior
  * `llm` determines the language model used (default: OpenAI’s GPT-4)



#### 

​

Memory and Context

  * `memory`: Enable to maintain conversation history
  * `respect_context_window`: Prevents token limit issues
  * `knowledge_sources`: Add domain-specific knowledge bases



#### 

​

Execution Control

  * `max_iter`: Maximum attempts before giving best answer
  * `max_execution_time`: Timeout in seconds
  * `max_rpm`: Rate limiting for API calls
  * `max_retry_limit`: Retries on error



#### 

​

Code Execution

  * `allow_code_execution`: Must be True to run code
  * `code_execution_mode`: 
    * `"safe"`: Uses Docker (recommended for production)
    * `"unsafe"`: Direct execution (use only in trusted environments)



This runs a default Docker image. If you want to configure the docker image, the checkout the Code Interpreter Tool in the tools section. Add the code interpreter tool as a tool in the agent as a tool parameter.

#### 

​

Advanced Features

  * `multimodal`: Enable multimodal capabilities for processing text and visual content
  * `reasoning`: Enable agent to reflect and create plans before executing tasks
  * `inject_date`: Automatically inject current date into task descriptions



#### 

​

Templates

  * `system_template`: Defines agent’s core behavior
  * `prompt_template`: Structures input format
  * `response_template`: Formats agent responses



When using custom templates, ensure that both `system_template` and `prompt_template` are defined. The `response_template` is optional but recommended for consistent output formatting.

When using custom templates, you can use variables like `{role}`, `{goal}`, and `{backstory}` in your templates. These will be automatically populated during execution.

## 

​

Agent Tools

Agents can be equipped with various tools to enhance their capabilities. CrewAI supports tools from:

  * [CrewAI Toolkit](https://github.com/joaomdmoura/crewai-tools)
  * [LangChain Tools](https://python.langchain.com/docs/integrations/tools)

Here’s how to add tools to an agent:

Code

Copy

Ask AI
    
    
    from crewai import Agent
    from crewai_tools import SerperDevTool, WikipediaTools
    
    # Create tools
    search_tool = SerperDevTool()
    wiki_tool = WikipediaTools()
    
    # Add tools to agent
    researcher = Agent(
        role="AI Technology Researcher",
        goal="Research the latest AI developments",
        tools=[search_tool, wiki_tool],
        verbose=True
    )
    

## 

​

Agent Memory and Context

Agents can maintain memory of their interactions and use context from previous tasks. This is particularly useful for complex workflows where information needs to be retained across multiple tasks.

Code

Copy

Ask AI
    
    
    from crewai import Agent
    
    analyst = Agent(
        role="Data Analyst",
        goal="Analyze and remember complex data patterns",
        memory=True,  # Enable memory
        verbose=True
    )
    

When `memory` is enabled, the agent will maintain context across multiple interactions, improving its ability to handle complex, multi-step tasks.

## 

​

Context Window Management

CrewAI includes sophisticated automatic context window management to handle situations where conversations exceed the language model’s token limits. This powerful feature is controlled by the `respect_context_window` parameter.

### 

​

How Context Window Management Works

When an agent’s conversation history grows too large for the LLM’s context window, CrewAI automatically detects this situation and can either:

  1. **Automatically summarize content** (when `respect_context_window=True`)
  2. **Stop execution with an error** (when `respect_context_window=False`)



### 

​

Automatic Context Handling (`respect_context_window=True`)

This is the **default and recommended setting** for most use cases. When enabled, CrewAI will:

Code

Copy

Ask AI
    
    
    # Agent with automatic context management (default)
    smart_agent = Agent(
        role="Research Analyst",
        goal="Analyze large documents and datasets",
        backstory="Expert at processing extensive information",
        respect_context_window=True,  # 🔑 Default: auto-handle context limits
        verbose=True
    )
    

**What happens when context limits are exceeded:**

  * ⚠️ **Warning message** : `"Context length exceeded. Summarizing content to fit the model context window."`
  * 🔄 **Automatic summarization** : CrewAI intelligently summarizes the conversation history
  * ✅ **Continued execution** : Task execution continues seamlessly with the summarized context
  * 📝 **Preserved information** : Key information is retained while reducing token count



### 

​

Strict Context Limits (`respect_context_window=False`)

When you need precise control and prefer execution to stop rather than lose any information:

Code

Copy

Ask AI
    
    
    # Agent with strict context limits
    strict_agent = Agent(
        role="Legal Document Reviewer",
        goal="Provide precise legal analysis without information loss",
        backstory="Legal expert requiring complete context for accurate analysis",
        respect_context_window=False,  # ❌ Stop execution on context limit
        verbose=True
    )
    

**What happens when context limits are exceeded:**

  * ❌ **Error message** : `"Context length exceeded. Consider using smaller text or RAG tools from crewai_tools."`
  * 🛑 **Execution stops** : Task execution halts immediately
  * 🔧 **Manual intervention required** : You need to modify your approach



### 

​

Choosing the Right Setting

#### 

​

Use `respect_context_window=True` (Default) when:

  * **Processing large documents** that might exceed context limits
  * **Long-running conversations** where some summarization is acceptable
  * **Research tasks** where general context is more important than exact details
  * **Prototyping and development** where you want robust execution



Code

Copy

Ask AI
    
    
    # Perfect for document processing
    document_processor = Agent(
        role="Document Analyst",
        goal="Extract insights from large research papers",
        backstory="Expert at analyzing extensive documentation",
        respect_context_window=True,  # Handle large documents gracefully
        max_iter=50,  # Allow more iterations for complex analysis
        verbose=True
    )
    

#### 

​

Use `respect_context_window=False` when:

  * **Precision is critical** and information loss is unacceptable
  * **Legal or medical tasks** requiring complete context
  * **Code review** where missing details could introduce bugs
  * **Financial analysis** where accuracy is paramount



Code

Copy

Ask AI
    
    
    # Perfect for precision tasks
    precision_agent = Agent(
        role="Code Security Auditor",
        goal="Identify security vulnerabilities in code",
        backstory="Security expert requiring complete code context",
        respect_context_window=False,  # Prefer failure over incomplete analysis
        max_retry_limit=1,  # Fail fast on context issues
        verbose=True
    )
    

### 

​

Alternative Approaches for Large Data

When dealing with very large datasets, consider these strategies:

#### 

​

1\. Use RAG Tools

Code

Copy

Ask AI
    
    
    from crewai_tools import RagTool
    
    # Create RAG tool for large document processing
    rag_tool = RagTool()
    
    rag_agent = Agent(
        role="Research Assistant",
        goal="Query large knowledge bases efficiently",
        backstory="Expert at using RAG tools for information retrieval",
        tools=[rag_tool],  # Use RAG instead of large context windows
        respect_context_window=True,
        verbose=True
    )
    

#### 

​

2\. Use Knowledge Sources

Code

Copy

Ask AI
    
    
    # Use knowledge sources instead of large prompts
    knowledge_agent = Agent(
        role="Knowledge Expert",
        goal="Answer questions using curated knowledge",
        backstory="Expert at leveraging structured knowledge sources",
        knowledge_sources=[your_knowledge_sources],  # Pre-processed knowledge
        respect_context_window=True,
        verbose=True
    )
    

### 

​

Context Window Best Practices

  1. **Monitor Context Usage** : Enable `verbose=True` to see context management in action
  2. **Design for Efficiency** : Structure tasks to minimize context accumulation
  3. **Use Appropriate Models** : Choose LLMs with context windows suitable for your tasks
  4. **Test Both Settings** : Try both `True` and `False` to see which works better for your use case
  5. **Combine with RAG** : Use RAG tools for very large datasets instead of relying solely on context windows



### 

​

Troubleshooting Context Issues

**If you’re getting context limit errors:**

Code

Copy

Ask AI
    
    
    # Quick fix: Enable automatic handling
    agent.respect_context_window = True
    
    # Better solution: Use RAG tools for large data
    from crewai_tools import RagTool
    agent.tools = [RagTool()]
    
    # Alternative: Break tasks into smaller pieces
    # Or use knowledge sources instead of large prompts
    

**If automatic summarization loses important information:**

Code

Copy

Ask AI
    
    
    # Disable auto-summarization and use RAG instead
    agent = Agent(
        role="Detailed Analyst",
        goal="Maintain complete information accuracy",
        backstory="Expert requiring full context",
        respect_context_window=False,  # No summarization
        tools=[RagTool()],  # Use RAG for large data
        verbose=True
    )
    

The context window management feature works automatically in the background. You don’t need to call any special functions - just set `respect_context_window` to your preferred behavior and CrewAI handles the rest!

## 

​

Direct Agent Interaction with `kickoff()`

Agents can be used directly without going through a task or crew workflow using the `kickoff()` method. This provides a simpler way to interact with an agent when you don’t need the full crew orchestration capabilities.

### 

​

How `kickoff()` Works

The `kickoff()` method allows you to send messages directly to an agent and get a response, similar to how you would interact with an LLM but with all the agent’s capabilities (tools, reasoning, etc.).

Code

Copy

Ask AI
    
    
    from crewai import Agent
    from crewai_tools import SerperDevTool
    
    # Create an agent
    researcher = Agent(
        role="AI Technology Researcher",
        goal="Research the latest AI developments",
        tools=[SerperDevTool()],
        verbose=True
    )
    
    # Use kickoff() to interact directly with the agent
    result = researcher.kickoff("What are the latest developments in language models?")
    
    # Access the raw response
    print(result.raw)
    

### 

​

Parameters and Return Values

Parameter| Type| Description  
---|---|---  
`messages`| `Union[str, List[Dict[str, str]]]`| Either a string query or a list of message dictionaries with role/content  
`response_format`| `Optional[Type[Any]]`| Optional Pydantic model for structured output  
  
The method returns a `LiteAgentOutput` object with the following properties:

  * `raw`: String containing the raw output text
  * `pydantic`: Parsed Pydantic model (if a `response_format` was provided)
  * `agent_role`: Role of the agent that produced the output
  * `usage_metrics`: Token usage metrics for the execution



### 

​

Structured Output

You can get structured output by providing a Pydantic model as the `response_format`:

Code

Copy

Ask AI
    
    
    from pydantic import BaseModel
    from typing import List
    
    class ResearchFindings(BaseModel):
        main_points: List[str]
        key_technologies: List[str]
        future_predictions: str
    
    # Get structured output
    result = researcher.kickoff(
        "Summarize the latest developments in AI for 2025",
        response_format=ResearchFindings
    )
    
    # Access structured data
    print(result.pydantic.main_points)
    print(result.pydantic.future_predictions)
    

### 

​

Multiple Messages

You can also provide a conversation history as a list of message dictionaries:

Code

Copy

Ask AI
    
    
    messages = [
        {"role": "user", "content": "I need information about large language models"},
        {"role": "assistant", "content": "I'd be happy to help with that! What specifically would you like to know?"},
        {"role": "user", "content": "What are the latest developments in 2025?"}
    ]
    
    result = researcher.kickoff(messages)
    

### 

​

Async Support

An asynchronous version is available via `kickoff_async()` with the same parameters:

Code

Copy

Ask AI
    
    
    import asyncio
    
    async def main():
        result = await researcher.kickoff_async("What are the latest developments in AI?")
        print(result.raw)
    
    asyncio.run(main())
    

The `kickoff()` method uses a `LiteAgent` internally, which provides a simpler execution flow while preserving all of the agent’s configuration (role, goal, backstory, tools, etc.).

## 

​

Important Considerations and Best Practices

### 

​

Security and Code Execution

  * When using `allow_code_execution`, be cautious with user input and always validate it
  * Use `code_execution_mode: "safe"` (Docker) in production environments
  * Consider setting appropriate `max_execution_time` limits to prevent infinite loops



### 

​

Performance Optimization

  * Use `respect_context_window: true` to prevent token limit issues
  * Set appropriate `max_rpm` to avoid rate limiting
  * Enable `cache: true` to improve performance for repetitive tasks
  * Adjust `max_iter` and `max_retry_limit` based on task complexity



### 

​

Memory and Context Management

  * Leverage `knowledge_sources` for domain-specific information
  * Configure `embedder` when using custom embedding models
  * Use custom templates (`system_template`, `prompt_template`, `response_template`) for fine-grained control over agent behavior



### 

​

Advanced Features

  * Enable `reasoning: true` for agents that need to plan and reflect before executing complex tasks
  * Set appropriate `max_reasoning_attempts` to control planning iterations (None for unlimited attempts)
  * Use `inject_date: true` to provide agents with current date awareness for time-sensitive tasks
  * Customize the date format with `date_format` using standard Python datetime format codes
  * Enable `multimodal: true` for agents that need to process both text and visual content



### 

​

Agent Collaboration

  * Enable `allow_delegation: true` when agents need to work together
  * Use `step_callback` to monitor and log agent interactions
  * Consider using different LLMs for different purposes: 
    * Main `llm` for complex reasoning
    * `function_calling_llm` for efficient tool usage



### 

​

Date Awareness and Reasoning

  * Use `inject_date: true` to provide agents with current date awareness for time-sensitive tasks
  * Customize the date format with `date_format` using standard Python datetime format codes
  * Valid format codes include: %Y (year), %m (month), %d (day), %B (full month name), etc.
  * Invalid date formats will be logged as warnings and will not modify the task description
  * Enable `reasoning: true` for complex tasks that benefit from upfront planning and reflection



### 

​

Model Compatibility

  * Set `use_system_prompt: false` for older models that don’t support system messages
  * Ensure your chosen `llm` supports the features you need (like function calling)



## 

​

Troubleshooting Common Issues

  1. **Rate Limiting** : If you’re hitting API rate limits:
     * Implement appropriate `max_rpm`
     * Use caching for repetitive operations
     * Consider batching requests
  2. **Context Window Errors** : If you’re exceeding context limits:
     * Enable `respect_context_window`
     * Use more efficient prompts
     * Clear agent memory periodically
  3. **Code Execution Issues** : If code execution fails:
     * Verify Docker is installed for safe mode
     * Check execution permissions
     * Review code sandbox settings
  4. **Memory Issues** : If agent responses seem inconsistent:
     * Check knowledge source configuration
     * Review conversation history management

Remember that agents are most effective when configured according to their specific use case. Take time to understand your requirements and adjust these parameters accordingly.

Was this page helpful?

YesNo

[FingerprintingPrevious](/en/guides/advanced/fingerprinting)[TasksNext](/en/concepts/tasks)

Ctrl+I

[website](https://crewai.com)[x](https://x.com/crewAIInc)[github](https://github.com/crewAIInc/crewAI)[linkedin](https://www.linkedin.com/company/crewai-inc)[youtube](https://youtube.com/@crewAIInc)[reddit](https://www.reddit.com/r/crewAIInc/)

[Powered by Mintlify](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=crewai)

Assistant

Responses are generated using AI and may contain mistakes.

![Visual Agent Builder Screenshot](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=ae6f0c18ef3679b5466177710fbc4a94)


---

# Source: https://docs.crewai.com/en/concepts/tasks

Skip to main content

[CrewAI home page![light logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)![dark logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)](/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl K

Search...

Navigation

Core Concepts

Tasks

[Home](/)[Documentation](/en/introduction)[AOP](/en/enterprise/introduction)[API Reference](/en/api-reference/introduction)[Examples](/en/examples/example)[Changelog](/en/changelog)

  * [Website](https://crewai.com)
  * [Forum](https://community.crewai.com)
  * [Blog](https://blog.crewai.com)
  * [CrewGPT](https://chatgpt.com/g/g-qqTuUWsBY-crewai-assistant)



##### Get Started

  * [Introduction](/en/introduction)
  * [Installation](/en/installation)
  * [Quickstart](/en/quickstart)



##### Guides

  * Strategy

  * Agents

  * Crews

  * Flows

  * Advanced




##### Core Concepts

  * [Agents](/en/concepts/agents)
  * [Tasks](/en/concepts/tasks)
  * [Crews](/en/concepts/crews)
  * [Flows](/en/concepts/flows)
  * [Knowledge](/en/concepts/knowledge)
  * [LLMs](/en/concepts/llms)
  * [Processes](/en/concepts/processes)
  * [Collaboration](/en/concepts/collaboration)
  * [Training](/en/concepts/training)
  * [Memory](/en/concepts/memory)
  * [Reasoning](/en/concepts/reasoning)
  * [Planning](/en/concepts/planning)
  * [Testing](/en/concepts/testing)
  * [CLI](/en/concepts/cli)
  * [Tools](/en/concepts/tools)
  * [Event Listeners](/en/concepts/event-listener)



##### MCP Integration

  * [MCP Servers as Tools in CrewAI](/en/mcp/overview)
  * [MCP DSL Integration](/en/mcp/dsl-integration)
  * [Stdio Transport](/en/mcp/stdio)
  * [SSE Transport](/en/mcp/sse)
  * [Streamable HTTP Transport](/en/mcp/streamable-http)
  * [Connecting to Multiple MCP Servers](/en/mcp/multiple-servers)
  * [MCP Security Considerations](/en/mcp/security)



##### Tools

  * [Tools Overview](/en/tools/overview)
  * File & Document

  * Web Scraping & Browsing

  * Search & Research

  * Database & Data

  * AI & Machine Learning

  * Cloud & Storage

  * Integrations

  * Automation




##### Observability

  * [CrewAI Tracing](/en/observability/tracing)
  * [Overview](/en/observability/overview)
  * [Arize Phoenix](/en/observability/arize-phoenix)
  * [Braintrust](/en/observability/braintrust)
  * [Datadog Integration](/en/observability/datadog)
  * [LangDB Integration](/en/observability/langdb)
  * [Langfuse Integration](/en/observability/langfuse)
  * [Langtrace Integration](/en/observability/langtrace)
  * [Maxim Integration](/en/observability/maxim)
  * [MLflow Integration](/en/observability/mlflow)
  * [Neatlogs Integration](/en/observability/neatlogs)
  * [OpenLIT Integration](/en/observability/openlit)
  * [Opik Integration](/en/observability/opik)
  * [Patronus AI Evaluation](/en/observability/patronus-evaluation)
  * [Portkey Integration](/en/observability/portkey)
  * [Weave Integration](/en/observability/weave)
  * [TrueFoundry Integration](/en/observability/truefoundry)



##### Learn

  * [Overview](/en/learn/overview)
  * [Strategic LLM Selection Guide](/en/learn/llm-selection-guide)
  * [Conditional Tasks](/en/learn/conditional-tasks)
  * [Coding Agents](/en/learn/coding-agents)
  * [Create Custom Tools](/en/learn/create-custom-tools)
  * [Custom LLM Implementation](/en/learn/custom-llm)
  * [Custom Manager Agent](/en/learn/custom-manager-agent)
  * [Customize Agents](/en/learn/customizing-agents)
  * [Image Generation with DALL-E](/en/learn/dalle-image-generation)
  * [Force Tool Output as Result](/en/learn/force-tool-output-as-result)
  * [Hierarchical Process](/en/learn/hierarchical-process)
  * [Human Input on Execution](/en/learn/human-input-on-execution)
  * [Human-in-the-Loop (HITL) Workflows](/en/learn/human-in-the-loop)
  * [Kickoff Crew Asynchronously](/en/learn/kickoff-async)
  * [Kickoff Crew for Each](/en/learn/kickoff-for-each)
  * [Connect to any LLM](/en/learn/llm-connections)
  * [Using Multimodal Agents](/en/learn/multimodal-agents)
  * [Replay Tasks from Latest Crew Kickoff](/en/learn/replay-tasks-from-latest-crew-kickoff)
  * [Sequential Processes](/en/learn/sequential-process)
  * [Using Annotations in crew.py](/en/learn/using-annotations)
  * [Execution Hooks Overview](/en/learn/execution-hooks)
  * [LLM Call Hooks](/en/learn/llm-hooks)
  * [Tool Call Hooks](/en/learn/tool-hooks)



##### Telemetry

  * [Telemetry](/en/telemetry)



Core Concepts

# Tasks

Copy page

Detailed guide on managing and creating tasks within the CrewAI framework.

Copy page

## 

​

Overview

In the CrewAI framework, a `Task` is a specific assignment completed by an `Agent`. Tasks provide all necessary details for execution, such as a description, the agent responsible, required tools, and more, facilitating a wide range of action complexities. Tasks within CrewAI can be collaborative, requiring multiple agents to work together. This is managed through the task properties and orchestrated by the Crew’s process, enhancing teamwork and efficiency.

CrewAI AOP includes a Visual Task Builder in Crew Studio that simplifies complex task creation and chaining. Design your task flows visually and test them in real-time without writing code.![Task Builder Screenshot](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=c4f5428b111816273b3b53d9cef14fad)The Visual Task Builder enables:

  * Drag-and-drop task creation
  * Visual task dependencies and flow
  * Real-time testing and validation
  * Easy sharing and collaboration



### 

​

Task Execution Flow

Tasks can be executed in two ways:

  * **Sequential** : Tasks are executed in the order they are defined
  * **Hierarchical** : Tasks are assigned to agents based on their roles and expertise

The execution flow is defined when creating the crew:

Code

Copy

Ask AI
    
    
    crew = Crew(
        agents=[agent1, agent2],
        tasks=[task1, task2],
        process=Process.sequential  # or Process.hierarchical
    )
    

## 

​

Task Attributes

Attribute| Parameters| Type| Description|   
---|---|---|---|---  
**Description**| `description`| `str`| A clear, concise statement of what the task entails.|   
**Expected Output**| `expected_output`| `str`| A detailed description of what the task’s completion looks like.|   
**Name** _(optional)_| `name`| `Optional[str]`| A name identifier for the task.|   
**Agent** _(optional)_| `agent`| `Optional[BaseAgent]`| The agent responsible for executing the task.|   
**Tools** _(optional)_| `tools`| `List[BaseTool]`| The tools/resources the agent is limited to use for this task.|   
**Context** _(optional)_| `context`| `Optional[List["Task"]]`| Other tasks whose outputs will be used as context for this task.|   
**Async Execution** _(optional)_| `async_execution`| `Optional[bool]`| Whether the task should be executed asynchronously. Defaults to False.|   
**Human Input** _(optional)_| `human_input`| `Optional[bool]`| Whether the task should have a human review the final answer of the agent. Defaults to False.|   
**Markdown** _(optional)_| `markdown`| `Optional[bool]`| Whether the task should instruct the agent to return the final answer formatted in Markdown. Defaults to False.|   
**Config** _(optional)_| `config`| `Optional[Dict[str, Any]]`| Task-specific configuration parameters.|   
**Output File** _(optional)_| `output_file`| `Optional[str]`| File path for storing the task output.|   
**Create Directory** _(optional)_| `create_directory`| `Optional[bool]`| Whether to create the directory for output_file if it doesn’t exist. Defaults to True.|   
**Output JSON** _(optional)_| `output_json`| `Optional[Type[BaseModel]]`| A Pydantic model to structure the JSON output.|   
**Output Pydantic** _(optional)_| `output_pydantic`| `Optional[Type[BaseModel]]`| A Pydantic model for task output.|   
**Callback** _(optional)_| `callback`| `Optional[Any]`| Function/object to be executed after task completion.|   
**Guardrail** _(optional)_| `guardrail`| `Optional[Callable]`| Function to validate task output before proceeding to next task.|   
**Guardrails** _(optional)_| `guardrails`| `Optional[List[Callable]| List[str]]`| List of guardrails to validate task output before proceeding to next task.  
**Guardrail Max Retries** _(optional)_| `guardrail_max_retries`| `Optional[int]`| Maximum number of retries when guardrail validation fails. Defaults to 3.|   
  
The task attribute `max_retries` is deprecated and will be removed in v1.0.0. Use `guardrail_max_retries` instead to control retry attempts when a guardrail fails.

## 

​

Creating Tasks

There are two ways to create tasks in CrewAI: using **YAML configuration (recommended)** or defining them **directly in code**.

### 

​

YAML Configuration (Recommended)

Using YAML configuration provides a cleaner, more maintainable way to define tasks. We strongly recommend using this approach to define tasks in your CrewAI projects. After creating your CrewAI project as outlined in the [Installation](/en/installation) section, navigate to the `src/latest_ai_development/config/tasks.yaml` file and modify the template to match your specific task requirements.

Variables in your YAML files (like `{topic}`) will be replaced with values from your inputs when running the crew:

Code

Copy

Ask AI
    
    
    crew.kickoff(inputs={'topic': 'AI Agents'})
    

Here’s an example of how to configure tasks using YAML:

tasks.yaml

Copy

Ask AI
    
    
    research_task:
      description: >
        Conduct a thorough research about {topic}
        Make sure you find any interesting and relevant information given
        the current year is 2025.
      expected_output: >
        A list with 10 bullet points of the most relevant information about {topic}
      agent: researcher
    
    reporting_task:
      description: >
        Review the context you got and expand each topic into a full section for a report.
        Make sure the report is detailed and contains any and all relevant information.
      expected_output: >
        A fully fledge reports with the mains topics, each with a full section of information.
        Formatted as markdown without '```'
      agent: reporting_analyst
      markdown: true
      output_file: report.md
    

To use this YAML configuration in your code, create a crew class that inherits from `CrewBase`:

crew.py

Copy

Ask AI
    
    
    # src/latest_ai_development/crew.py
    
    from crewai import Agent, Crew, Process, Task
    from crewai.project import CrewBase, agent, crew, task
    from crewai_tools import SerperDevTool
    
    @CrewBase
    class LatestAiDevelopmentCrew():
      """LatestAiDevelopment crew"""
    
      @agent
      def researcher(self) -> Agent:
        return Agent(
          config=self.agents_config['researcher'], # type: ignore[index]
          verbose=True,
          tools=[SerperDevTool()]
        )
    
      @agent
      def reporting_analyst(self) -> Agent:
        return Agent(
          config=self.agents_config['reporting_analyst'], # type: ignore[index]
          verbose=True
        )
    
      @task
      def research_task(self) -> Task:
        return Task(
          config=self.tasks_config['research_task'] # type: ignore[index]
        )
    
      @task
      def reporting_task(self) -> Task:
        return Task(
          config=self.tasks_config['reporting_task'] # type: ignore[index]
        )
    
      @crew
      def crew(self) -> Crew:
        return Crew(
          agents=[
            self.researcher(),
            self.reporting_analyst()
          ],
          tasks=[
            self.research_task(),
            self.reporting_task()
          ],
          process=Process.sequential
        )
    

The names you use in your YAML files (`agents.yaml` and `tasks.yaml`) should match the method names in your Python code.

### 

​

Direct Code Definition (Alternative)

Alternatively, you can define tasks directly in your code without using YAML configuration:

task.py

Copy

Ask AI
    
    
    from crewai import Task
    
    research_task = Task(
        description="""
            Conduct a thorough research about AI Agents.
            Make sure you find any interesting and relevant information given
            the current year is 2025.
        """,
        expected_output="""
            A list with 10 bullet points of the most relevant information about AI Agents
        """,
        agent=researcher
    )
    
    reporting_task = Task(
        description="""
            Review the context you got and expand each topic into a full section for a report.
            Make sure the report is detailed and contains any and all relevant information.
        """,
        expected_output="""
            A fully fledge reports with the mains topics, each with a full section of information.
        """,
        agent=reporting_analyst,
        markdown=True,  # Enable markdown formatting for the final output
        output_file="report.md"
    )
    

Directly specify an `agent` for assignment or let the `hierarchical` CrewAI’s process decide based on roles, availability, etc.

## 

​

Task Output

Understanding task outputs is crucial for building effective AI workflows. CrewAI provides a structured way to handle task results through the `TaskOutput` class, which supports multiple output formats and can be easily passed between tasks. The output of a task in CrewAI framework is encapsulated within the `TaskOutput` class. This class provides a structured way to access results of a task, including various formats such as raw output, JSON, and Pydantic models. By default, the `TaskOutput` will only include the `raw` output. A `TaskOutput` will only include the `pydantic` or `json_dict` output if the original `Task` object was configured with `output_pydantic` or `output_json`, respectively.

### 

​

Task Output Attributes

Attribute| Parameters| Type| Description  
---|---|---|---  
**Description**| `description`| `str`| Description of the task.  
**Summary**| `summary`| `Optional[str]`| Summary of the task, auto-generated from the first 10 words of the description.  
**Raw**| `raw`| `str`| The raw output of the task. This is the default format for the output.  
**Pydantic**| `pydantic`| `Optional[BaseModel]`| A Pydantic model object representing the structured output of the task.  
**JSON Dict**| `json_dict`| `Optional[Dict[str, Any]]`| A dictionary representing the JSON output of the task.  
**Agent**| `agent`| `str`| The agent that executed the task.  
**Output Format**| `output_format`| `OutputFormat`| The format of the task output, with options including RAW, JSON, and Pydantic. The default is RAW.  
**Messages**| `messages`| `list[LLMMessage]`| The messages from the last task execution.  
  
### 

​

Task Methods and Properties

Method/Property| Description  
---|---  
**json**|  Returns the JSON string representation of the task output if the output format is JSON.  
**to_dict**|  Converts the JSON and Pydantic outputs to a dictionary.  
**str**|  Returns the string representation of the task output, prioritizing Pydantic, then JSON, then raw.  
  
### 

​

Accessing Task Outputs

Once a task has been executed, its output can be accessed through the `output` attribute of the `Task` object. The `TaskOutput` class provides various ways to interact with and present this output.

#### 

​

Example

Code

Copy

Ask AI
    
    
    # Example task
    task = Task(
        description='Find and summarize the latest AI news',
        expected_output='A bullet list summary of the top 5 most important AI news',
        agent=research_agent,
        tools=[search_tool]
    )
    
    # Execute the crew
    crew = Crew(
        agents=[research_agent],
        tasks=[task],
        verbose=True
    )
    
    result = crew.kickoff()
    
    # Accessing the task output
    task_output = task.output
    
    print(f"Task Description: {task_output.description}")
    print(f"Task Summary: {task_output.summary}")
    print(f"Raw Output: {task_output.raw}")
    if task_output.json_dict:
        print(f"JSON Output: {json.dumps(task_output.json_dict, indent=2)}")
    if task_output.pydantic:
        print(f"Pydantic Output: {task_output.pydantic}")
    

## 

​

Markdown Output Formatting

The `markdown` parameter enables automatic markdown formatting for task outputs. When set to `True`, the task will instruct the agent to format the final answer using proper Markdown syntax.

### 

​

Using Markdown Formatting

Code

Copy

Ask AI
    
    
    # Example task with markdown formatting enabled
    formatted_task = Task(
        description="Create a comprehensive report on AI trends",
        expected_output="A well-structured report with headers, sections, and bullet points",
        agent=reporter_agent,
        markdown=True  # Enable automatic markdown formatting
    )
    

When `markdown=True`, the agent will receive additional instructions to format the output using:

  * `#` for headers
  * `**text**` for bold text
  * `*text*` for italic text
  * `-` or `*` for bullet points
  * ``code`` for inline code
  * ` `language ``` for code blocks



### 

​

YAML Configuration with Markdown

tasks.yaml

Copy

Ask AI
    
    
    analysis_task:
      description: >
        Analyze the market data and create a detailed report
      expected_output: >
        A comprehensive analysis with charts and key findings
      agent: analyst
      markdown: true  # Enable markdown formatting
      output_file: analysis.md
    

### 

​

Benefits of Markdown Output

  * **Consistent Formatting** : Ensures all outputs follow proper markdown conventions
  * **Better Readability** : Structured content with headers, lists, and emphasis
  * **Documentation Ready** : Output can be directly used in documentation systems
  * **Cross-Platform Compatibility** : Markdown is universally supported



The markdown formatting instructions are automatically added to the task prompt when `markdown=True`, so you don’t need to specify formatting requirements in your task description.

## 

​

Task Dependencies and Context

Tasks can depend on the output of other tasks using the `context` attribute. For example:

Code

Copy

Ask AI
    
    
    research_task = Task(
        description="Research the latest developments in AI",
        expected_output="A list of recent AI developments",
        agent=researcher
    )
    
    analysis_task = Task(
        description="Analyze the research findings and identify key trends",
        expected_output="Analysis report of AI trends",
        agent=analyst,
        context=[research_task]  # This task will wait for research_task to complete
    )
    

## 

​

Task Guardrails

Task guardrails provide a way to validate and transform task outputs before they are passed to the next task. This feature helps ensure data quality and provides feedback to agents when their output doesn’t meet specific criteria. CrewAI supports two types of guardrails:

  1. **Function-based guardrails** : Python functions with custom validation logic, giving you complete control over the validation process and ensuring reliable, deterministic results.
  2. **LLM-based guardrails** : String descriptions that use the agent’s LLM to validate outputs based on natural language criteria. These are ideal for complex or subjective validation requirements.



### 

​

Function-Based Guardrails

To add a function-based guardrail to a task, provide a validation function through the `guardrail` parameter:

Code

Copy

Ask AI
    
    
    from typing import Tuple, Union, Dict, Any
    from crewai import TaskOutput
    
    def validate_blog_content(result: TaskOutput) -> Tuple[bool, Any]:
        """Validate blog content meets requirements."""
        try:
            # Check word count
            word_count = len(result.raw.split())
            if word_count > 200:
                return (False, "Blog content exceeds 200 words")
    
            # Additional validation logic here
            return (True, result.raw.strip())
        except Exception as e:
            return (False, "Unexpected error during validation")
    
    blog_task = Task(
        description="Write a blog post about AI",
        expected_output="A blog post under 200 words",
        agent=blog_agent,
        guardrail=validate_blog_content  # Add the guardrail function
    )
    

### 

​

LLM-Based Guardrails (String Descriptions)

Instead of writing custom validation functions, you can use string descriptions that leverage LLM-based validation. When you provide a string to the `guardrail` or `guardrails` parameter, CrewAI automatically creates an `LLMGuardrail` that uses the agent’s LLM to validate the output based on your description. **Requirements** :

  * The task must have an `agent` assigned (the guardrail uses the agent’s LLM)
  * Provide a clear, descriptive string explaining the validation criteria



Code

Copy

Ask AI
    
    
    from crewai import Task
    
    # Single LLM-based guardrail
    blog_task = Task(
        description="Write a blog post about AI",
        expected_output="A blog post under 200 words",
        agent=blog_agent,
        guardrail="The blog post must be under 200 words and contain no technical jargon"
    )
    

LLM-based guardrails are particularly useful for:

  * **Complex validation logic** that’s difficult to express programmatically
  * **Subjective criteria** like tone, style, or quality assessments
  * **Natural language requirements** that are easier to describe than code

The LLM guardrail will:

  1. Analyze the task output against your description
  2. Return `(True, output)` if the output complies with the criteria
  3. Return `(False, feedback)` with specific feedback if validation fails

**Example with detailed validation criteria** :

Code

Copy

Ask AI
    
    
    research_task = Task(
        description="Research the latest developments in quantum computing",
        expected_output="A comprehensive research report",
        agent=researcher_agent,
        guardrail="""
        The research report must:
        - Be at least 1000 words long
        - Include at least 5 credible sources
        - Cover both technical and practical applications
        - Be written in a professional, academic tone
        - Avoid speculation or unverified claims
        """
    )
    

### 

​

Multiple Guardrails

You can apply multiple guardrails to a task using the `guardrails` parameter. Multiple guardrails are executed sequentially, with each guardrail receiving the output from the previous one. This allows you to chain validation and transformation steps. The `guardrails` parameter accepts:

  * A list of guardrail functions or string descriptions
  * A single guardrail function or string (same as `guardrail`)

**Note** : If `guardrails` is provided, it takes precedence over `guardrail`. The `guardrail` parameter will be ignored when `guardrails` is set.

Code

Copy

Ask AI
    
    
    from typing import Tuple, Any
    from crewai import TaskOutput, Task
    
    def validate_word_count(result: TaskOutput) -> Tuple[bool, Any]:
        """Validate word count is within limits."""
        word_count = len(result.raw.split())
        if word_count < 100:
            return (False, f"Content too short: {word_count} words. Need at least 100 words.")
        if word_count > 500:
            return (False, f"Content too long: {word_count} words. Maximum is 500 words.")
        return (True, result.raw)
    
    def validate_no_profanity(result: TaskOutput) -> Tuple[bool, Any]:
        """Check for inappropriate language."""
        profanity_words = ["badword1", "badword2"]  # Example list
        content_lower = result.raw.lower()
        for word in profanity_words:
            if word in content_lower:
                return (False, f"Inappropriate language detected: {word}")
        return (True, result.raw)
    
    def format_output(result: TaskOutput) -> Tuple[bool, Any]:
        """Format and clean the output."""
        formatted = result.raw.strip()
        # Capitalize first letter
        formatted = formatted[0].upper() + formatted[1:] if formatted else formatted
        return (True, formatted)
    
    # Apply multiple guardrails sequentially
    blog_task = Task(
        description="Write a blog post about AI",
        expected_output="A well-formatted blog post between 100-500 words",
        agent=blog_agent,
        guardrails=[
            validate_word_count,      # First: validate length
            validate_no_profanity,    # Second: check content
            format_output             # Third: format the result
        ],
        guardrail_max_retries=3
    )
    

In this example, the guardrails execute in order:

  1. `validate_word_count` checks the word count
  2. `validate_no_profanity` checks for inappropriate language (using the output from step 1)
  3. `format_output` formats the final result (using the output from step 2)

If any guardrail fails, the error is sent back to the agent, and the task is retried up to `guardrail_max_retries` times. **Mixing function-based and LLM-based guardrails** : You can combine both function-based and string-based guardrails in the same list:

Code

Copy

Ask AI
    
    
    from typing import Tuple, Any
    from crewai import TaskOutput, Task
    
    def validate_word_count(result: TaskOutput) -> Tuple[bool, Any]:
        """Validate word count is within limits."""
        word_count = len(result.raw.split())
        if word_count < 100:
            return (False, f"Content too short: {word_count} words. Need at least 100 words.")
        if word_count > 500:
            return (False, f"Content too long: {word_count} words. Maximum is 500 words.")
        return (True, result.raw)
    
    # Mix function-based and LLM-based guardrails
    blog_task = Task(
        description="Write a blog post about AI",
        expected_output="A well-formatted blog post between 100-500 words",
        agent=blog_agent,
        guardrails=[
            validate_word_count,  # Function-based: precise word count check
            "The content must be engaging and suitable for a general audience",  # LLM-based: subjective quality check
            "The writing style should be clear, concise, and free of technical jargon"  # LLM-based: style validation
        ],
        guardrail_max_retries=3
    )
    

This approach combines the precision of programmatic validation with the flexibility of LLM-based assessment for subjective criteria.

### 

​

Guardrail Function Requirements

  1. **Function Signature** :
     * Must accept exactly one parameter (the task output)
     * Should return a tuple of `(bool, Any)`
     * Type hints are recommended but optional
  2. **Return Values** :
     * On success: it returns a tuple of `(bool, Any)`. For example: `(True, validated_result)`
     * On Failure: it returns a tuple of `(bool, str)`. For example: `(False, "Error message explain the failure")`



### 

​

Error Handling Best Practices

  1. **Structured Error Responses** :



Code

Copy

Ask AI
    
    
    from crewai import TaskOutput, LLMGuardrail
    
    def validate_with_context(result: TaskOutput) -> Tuple[bool, Any]:
        try:
            # Main validation logic
            validated_data = perform_validation(result)
            return (True, validated_data)
        except ValidationError as e:
            return (False, f"VALIDATION_ERROR: {str(e)}")
        except Exception as e:
            return (False, str(e))
    

  2. **Error Categories** :
     * Use specific error codes
     * Include relevant context
     * Provide actionable feedback
  3. **Validation Chain** :



Code

Copy

Ask AI
    
    
    from typing import Any, Dict, List, Tuple, Union
    from crewai import TaskOutput
    
    def complex_validation(result: TaskOutput) -> Tuple[bool, Any]:
        """Chain multiple validation steps."""
        # Step 1: Basic validation
        if not result:
            return (False, "Empty result")
    
        # Step 2: Content validation
        try:
            validated = validate_content(result)
            if not validated:
                return (False, "Invalid content")
    
            # Step 3: Format validation
            formatted = format_output(validated)
            return (True, formatted)
        except Exception as e:
            return (False, str(e))
    

### 

​

Handling Guardrail Results

When a guardrail returns `(False, error)`:

  1. The error is sent back to the agent
  2. The agent attempts to fix the issue
  3. The process repeats until: 
     * The guardrail returns `(True, result)`
     * Maximum retries are reached (`guardrail_max_retries`)

Example with retry handling:

Code

Copy

Ask AI
    
    
    from typing import Optional, Tuple, Union
    from crewai import TaskOutput, Task
    
    def validate_json_output(result: TaskOutput) -> Tuple[bool, Any]:
        """Validate and parse JSON output."""
        try:
            # Try to parse as JSON
            data = json.loads(result)
            return (True, data)
        except json.JSONDecodeError as e:
            return (False, "Invalid JSON format")
    
    task = Task(
        description="Generate a JSON report",
        expected_output="A valid JSON object",
        agent=analyst,
        guardrail=validate_json_output,
        guardrail_max_retries=3  # Limit retry attempts
    )
    

## 

​

Getting Structured Consistent Outputs from Tasks

It’s also important to note that the output of the final task of a crew becomes the final output of the actual crew itself.

### 

​

Using `output_pydantic`

The `output_pydantic` property allows you to define a Pydantic model that the task output should conform to. This ensures that the output is not only structured but also validated according to the Pydantic model. Here’s an example demonstrating how to use output_pydantic:

Code

Copy

Ask AI
    
    
    import json
    
    from crewai import Agent, Crew, Process, Task
    from pydantic import BaseModel
    
    
    class Blog(BaseModel):
        title: str
        content: str
    
    
    blog_agent = Agent(
        role="Blog Content Generator Agent",
        goal="Generate a blog title and content",
        backstory="""You are an expert content creator, skilled in crafting engaging and informative blog posts.""",
        verbose=False,
        allow_delegation=False,
        llm="gpt-4o",
    )
    
    task1 = Task(
        description="""Create a blog title and content on a given topic. Make sure the content is under 200 words.""",
        expected_output="A compelling blog title and well-written content.",
        agent=blog_agent,
        output_pydantic=Blog,
    )
    
    # Instantiate your crew with a sequential process
    crew = Crew(
        agents=[blog_agent],
        tasks=[task1],
        verbose=True,
        process=Process.sequential,
    )
    
    result = crew.kickoff()
    
    # Option 1: Accessing Properties Using Dictionary-Style Indexing
    print("Accessing Properties - Option 1")
    title = result["title"]
    content = result["content"]
    print("Title:", title)
    print("Content:", content)
    
    # Option 2: Accessing Properties Directly from the Pydantic Model
    print("Accessing Properties - Option 2")
    title = result.pydantic.title
    content = result.pydantic.content
    print("Title:", title)
    print("Content:", content)
    
    # Option 3: Accessing Properties Using the to_dict() Method
    print("Accessing Properties - Option 3")
    output_dict = result.to_dict()
    title = output_dict["title"]
    content = output_dict["content"]
    print("Title:", title)
    print("Content:", content)
    
    # Option 4: Printing the Entire Blog Object
    print("Accessing Properties - Option 5")
    print("Blog:", result)
    
    

In this example:

  * A Pydantic model Blog is defined with title and content fields.
  * The task task1 uses the output_pydantic property to specify that its output should conform to the Blog model.
  * After executing the crew, you can access the structured output in multiple ways as shown.



#### 

​

Explanation of Accessing the Output

  1. Dictionary-Style Indexing: You can directly access the fields using result[“field_name”]. This works because the CrewOutput class implements the **getitem** method.
  2. Directly from Pydantic Model: Access the attributes directly from the result.pydantic object.
  3. Using to_dict() Method: Convert the output to a dictionary and access the fields.
  4. Printing the Entire Object: Simply print the result object to see the structured output.



### 

​

Using `output_json`

The `output_json` property allows you to define the expected output in JSON format. This ensures that the task’s output is a valid JSON structure that can be easily parsed and used in your application. Here’s an example demonstrating how to use `output_json`:

Code

Copy

Ask AI
    
    
    import json
    
    from crewai import Agent, Crew, Process, Task
    from pydantic import BaseModel
    
    
    # Define the Pydantic model for the blog
    class Blog(BaseModel):
        title: str
        content: str
    
    
    # Define the agent
    blog_agent = Agent(
        role="Blog Content Generator Agent",
        goal="Generate a blog title and content",
        backstory="""You are an expert content creator, skilled in crafting engaging and informative blog posts.""",
        verbose=False,
        allow_delegation=False,
        llm="gpt-4o",
    )
    
    # Define the task with output_json set to the Blog model
    task1 = Task(
        description="""Create a blog title and content on a given topic. Make sure the content is under 200 words.""",
        expected_output="A JSON object with 'title' and 'content' fields.",
        agent=blog_agent,
        output_json=Blog,
    )
    
    # Instantiate the crew with a sequential process
    crew = Crew(
        agents=[blog_agent],
        tasks=[task1],
        verbose=True,
        process=Process.sequential,
    )
    
    # Kickoff the crew to execute the task
    result = crew.kickoff()
    
    # Option 1: Accessing Properties Using Dictionary-Style Indexing
    print("Accessing Properties - Option 1")
    title = result["title"]
    content = result["content"]
    print("Title:", title)
    print("Content:", content)
    
    # Option 2: Printing the Entire Blog Object
    print("Accessing Properties - Option 2")
    print("Blog:", result)
    

In this example:

  * A Pydantic model Blog is defined with title and content fields, which is used to specify the structure of the JSON output.
  * The task task1 uses the output_json property to indicate that it expects a JSON output conforming to the Blog model.
  * After executing the crew, you can access the structured JSON output in two ways as shown.



#### 

​

Explanation of Accessing the Output

  1. Accessing Properties Using Dictionary-Style Indexing: You can access the fields directly using result[“field_name”]. This is possible because the CrewOutput class implements the **getitem** method, allowing you to treat the output like a dictionary. In this option, we’re retrieving the title and content from the result.
  2. Printing the Entire Blog Object: By printing result, you get the string representation of the CrewOutput object. Since the **str** method is implemented to return the JSON output, this will display the entire output as a formatted string representing the Blog object.



* * *

By using output_pydantic or output_json, you ensure that your tasks produce outputs in a consistent and structured format, making it easier to process and utilize the data within your application or across multiple tasks.

## 

​

Integrating Tools with Tasks

Leverage tools from the [CrewAI Toolkit](https://github.com/joaomdmoura/crewai-tools) and [LangChain Tools](https://python.langchain.com/docs/integrations/tools) for enhanced task performance and agent interaction.

## 

​

Creating a Task with Tools

Code

Copy

Ask AI
    
    
    import os
    os.environ["OPENAI_API_KEY"] = "Your Key"
    os.environ["SERPER_API_KEY"] = "Your Key" # serper.dev API key
    
    from crewai import Agent, Task, Crew
    from crewai_tools import SerperDevTool
    
    research_agent = Agent(
      role='Researcher',
      goal='Find and summarize the latest AI news',
      backstory="""You're a researcher at a large company.
      You're responsible for analyzing data and providing insights
      to the business.""",
      verbose=True
    )
    
    # to perform a semantic search for a specified query from a text's content across the internet
    search_tool = SerperDevTool()
    
    task = Task(
      description='Find and summarize the latest AI news',
      expected_output='A bullet list summary of the top 5 most important AI news',
      agent=research_agent,
      tools=[search_tool]
    )
    
    crew = Crew(
        agents=[research_agent],
        tasks=[task],
        verbose=True
    )
    
    result = crew.kickoff()
    print(result)
    

This demonstrates how tasks with specific tools can override an agent’s default set for tailored task execution.

## 

​

Referring to Other Tasks

In CrewAI, the output of one task is automatically relayed into the next one, but you can specifically define what tasks’ output, including multiple, should be used as context for another task. This is useful when you have a task that depends on the output of another task that is not performed immediately after it. This is done through the `context` attribute of the task:

Code

Copy

Ask AI
    
    
    # ...
    
    research_ai_task = Task(
        description="Research the latest developments in AI",
        expected_output="A list of recent AI developments",
        async_execution=True,
        agent=research_agent,
        tools=[search_tool]
    )
    
    research_ops_task = Task(
        description="Research the latest developments in AI Ops",
        expected_output="A list of recent AI Ops developments",
        async_execution=True,
        agent=research_agent,
        tools=[search_tool]
    )
    
    write_blog_task = Task(
        description="Write a full blog post about the importance of AI and its latest news",
        expected_output="Full blog post that is 4 paragraphs long",
        agent=writer_agent,
        context=[research_ai_task, research_ops_task]
    )
    
    #...
    

## 

​

Asynchronous Execution

You can define a task to be executed asynchronously. This means that the crew will not wait for it to be completed to continue with the next task. This is useful for tasks that take a long time to be completed, or that are not crucial for the next tasks to be performed. You can then use the `context` attribute to define in a future task that it should wait for the output of the asynchronous task to be completed.

Code

Copy

Ask AI
    
    
    #...
    
    list_ideas = Task(
        description="List of 5 interesting ideas to explore for an article about AI.",
        expected_output="Bullet point list of 5 ideas for an article.",
        agent=researcher,
        async_execution=True # Will be executed asynchronously
    )
    
    list_important_history = Task(
        description="Research the history of AI and give me the 5 most important events.",
        expected_output="Bullet point list of 5 important events.",
        agent=researcher,
        async_execution=True # Will be executed asynchronously
    )
    
    write_article = Task(
        description="Write an article about AI, its history, and interesting ideas.",
        expected_output="A 4 paragraph article about AI.",
        agent=writer,
        context=[list_ideas, list_important_history] # Will wait for the output of the two tasks to be completed
    )
    
    #...
    

## 

​

Callback Mechanism

The callback function is executed after the task is completed, allowing for actions or notifications to be triggered based on the task’s outcome.

Code

Copy

Ask AI
    
    
    # ...
    
    def callback_function(output: TaskOutput):
        # Do something after the task is completed
        # Example: Send an email to the manager
        print(f"""
            Task completed!
            Task: {output.description}
            Output: {output.raw}
        """)
    
    research_task = Task(
        description='Find and summarize the latest AI news',
        expected_output='A bullet list summary of the top 5 most important AI news',
        agent=research_agent,
        tools=[search_tool],
        callback=callback_function
    )
    
    #...
    

## 

​

Accessing a Specific Task Output

Once a crew finishes running, you can access the output of a specific task by using the `output` attribute of the task object:

Code

Copy

Ask AI
    
    
    # ...
    task1 = Task(
        description='Find and summarize the latest AI news',
        expected_output='A bullet list summary of the top 5 most important AI news',
        agent=research_agent,
        tools=[search_tool]
    )
    
    #...
    
    crew = Crew(
        agents=[research_agent],
        tasks=[task1, task2, task3],
        verbose=True
    )
    
    result = crew.kickoff()
    
    # Returns a TaskOutput object with the description and results of the task
    print(f"""
        Task completed!
        Task: {task1.output.description}
        Output: {task1.output.raw}
    """)
    

## 

​

Tool Override Mechanism

Specifying tools in a task allows for dynamic adaptation of agent capabilities, emphasizing CrewAI’s flexibility.

## 

​

Error Handling and Validation Mechanisms

While creating and executing tasks, certain validation mechanisms are in place to ensure the robustness and reliability of task attributes. These include but are not limited to:

  * Ensuring only one output type is set per task to maintain clear output expectations.
  * Preventing the manual assignment of the `id` attribute to uphold the integrity of the unique identifier system.

These validations help in maintaining the consistency and reliability of task executions within the crewAI framework.

## 

​

Creating Directories when Saving Files

The `create_directory` parameter controls whether CrewAI should automatically create directories when saving task outputs to files. This feature is particularly useful for organizing outputs and ensuring that file paths are correctly structured, especially when working with complex project hierarchies.

### 

​

Default Behavior

By default, `create_directory=True`, which means CrewAI will automatically create any missing directories in the output file path:

Code

Copy

Ask AI
    
    
    # Default behavior - directories are created automatically
    report_task = Task(
        description='Generate a comprehensive market analysis report',
        expected_output='A detailed market analysis with charts and insights',
        agent=analyst_agent,
        output_file='reports/2025/market_analysis.md',  # Creates 'reports/2025/' if it doesn't exist
        markdown=True
    )
    

### 

​

Disabling Directory Creation

If you want to prevent automatic directory creation and ensure that the directory already exists, set `create_directory=False`:

Code

Copy

Ask AI
    
    
    # Strict mode - directory must already exist
    strict_output_task = Task(
        description='Save critical data that requires existing infrastructure',
        expected_output='Data saved to pre-configured location',
        agent=data_agent,
        output_file='secure/vault/critical_data.json',
        create_directory=False  # Will raise RuntimeError if 'secure/vault/' doesn't exist
    )
    

### 

​

YAML Configuration

You can also configure this behavior in your YAML task definitions:

tasks.yaml

Copy

Ask AI
    
    
    analysis_task:
      description: >
        Generate quarterly financial analysis
      expected_output: >
        A comprehensive financial report with quarterly insights
      agent: financial_analyst
      output_file: reports/quarterly/q4_2024_analysis.pdf
      create_directory: true  # Automatically create 'reports/quarterly/' directory
    
    audit_task:
      description: >
        Perform compliance audit and save to existing audit directory
      expected_output: >
        A compliance audit report
      agent: auditor
      output_file: audit/compliance_report.md
      create_directory: false  # Directory must already exist
    

### 

​

Use Cases

**Automatic Directory Creation (`create_directory=True`):**

  * Development and prototyping environments
  * Dynamic report generation with date-based folders
  * Automated workflows where directory structure may vary
  * Multi-tenant applications with user-specific folders

**Manual Directory Management (`create_directory=False`):**

  * Production environments with strict file system controls
  * Security-sensitive applications where directories must be pre-configured
  * Systems with specific permission requirements
  * Compliance environments where directory creation is audited



### 

​

Error Handling

When `create_directory=False` and the directory doesn’t exist, CrewAI will raise a `RuntimeError`:

Code

Copy

Ask AI
    
    
    try:
        result = crew.kickoff()
    except RuntimeError as e:
        # Handle missing directory error
        print(f"Directory creation failed: {e}")
        # Create directory manually or use fallback location
    

Check out the video below to see how to use structured outputs in CrewAI:

## 

​

Conclusion

Tasks are the driving force behind the actions of agents in CrewAI. By properly defining tasks and their outcomes, you set the stage for your AI agents to work effectively, either independently or as a collaborative unit. Equipping tasks with appropriate tools, understanding the execution process, and following robust validation practices are crucial for maximizing CrewAI’s potential, ensuring agents are effectively prepared for their assignments and that tasks are executed as intended.

Was this page helpful?

YesNo

[AgentsPrevious](/en/concepts/agents)[CrewsNext](/en/concepts/crews)

Ctrl+I

[website](https://crewai.com)[x](https://x.com/crewAIInc)[github](https://github.com/crewAIInc/crewAI)[linkedin](https://www.linkedin.com/company/crewai-inc)[youtube](https://youtube.com/@crewAIInc)[reddit](https://www.reddit.com/r/crewAIInc/)

[Powered by Mintlify](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=crewai)

Assistant

Responses are generated using AI and may contain mistakes.

![Task Builder Screenshot](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=ae6f0c18ef3679b5466177710fbc4a94)


---

# Source: https://docs.crewai.com/en/concepts/crews

Skip to main content

[CrewAI home page![light logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)![dark logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)](/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl K

Search...

Navigation

Core Concepts

Crews

[Home](/)[Documentation](/en/introduction)[AOP](/en/enterprise/introduction)[API Reference](/en/api-reference/introduction)[Examples](/en/examples/example)[Changelog](/en/changelog)

  * [Website](https://crewai.com)
  * [Forum](https://community.crewai.com)
  * [Blog](https://blog.crewai.com)
  * [CrewGPT](https://chatgpt.com/g/g-qqTuUWsBY-crewai-assistant)



##### Get Started

  * [Introduction](/en/introduction)
  * [Installation](/en/installation)
  * [Quickstart](/en/quickstart)



##### Guides

  * Strategy

  * Agents

  * Crews

  * Flows

  * Advanced




##### Core Concepts

  * [Agents](/en/concepts/agents)
  * [Tasks](/en/concepts/tasks)
  * [Crews](/en/concepts/crews)
  * [Flows](/en/concepts/flows)
  * [Knowledge](/en/concepts/knowledge)
  * [LLMs](/en/concepts/llms)
  * [Processes](/en/concepts/processes)
  * [Collaboration](/en/concepts/collaboration)
  * [Training](/en/concepts/training)
  * [Memory](/en/concepts/memory)
  * [Reasoning](/en/concepts/reasoning)
  * [Planning](/en/concepts/planning)
  * [Testing](/en/concepts/testing)
  * [CLI](/en/concepts/cli)
  * [Tools](/en/concepts/tools)
  * [Event Listeners](/en/concepts/event-listener)



##### MCP Integration

  * [MCP Servers as Tools in CrewAI](/en/mcp/overview)
  * [MCP DSL Integration](/en/mcp/dsl-integration)
  * [Stdio Transport](/en/mcp/stdio)
  * [SSE Transport](/en/mcp/sse)
  * [Streamable HTTP Transport](/en/mcp/streamable-http)
  * [Connecting to Multiple MCP Servers](/en/mcp/multiple-servers)
  * [MCP Security Considerations](/en/mcp/security)



##### Tools

  * [Tools Overview](/en/tools/overview)
  * File & Document

  * Web Scraping & Browsing

  * Search & Research

  * Database & Data

  * AI & Machine Learning

  * Cloud & Storage

  * Integrations

  * Automation




##### Observability

  * [CrewAI Tracing](/en/observability/tracing)
  * [Overview](/en/observability/overview)
  * [Arize Phoenix](/en/observability/arize-phoenix)
  * [Braintrust](/en/observability/braintrust)
  * [Datadog Integration](/en/observability/datadog)
  * [LangDB Integration](/en/observability/langdb)
  * [Langfuse Integration](/en/observability/langfuse)
  * [Langtrace Integration](/en/observability/langtrace)
  * [Maxim Integration](/en/observability/maxim)
  * [MLflow Integration](/en/observability/mlflow)
  * [Neatlogs Integration](/en/observability/neatlogs)
  * [OpenLIT Integration](/en/observability/openlit)
  * [Opik Integration](/en/observability/opik)
  * [Patronus AI Evaluation](/en/observability/patronus-evaluation)
  * [Portkey Integration](/en/observability/portkey)
  * [Weave Integration](/en/observability/weave)
  * [TrueFoundry Integration](/en/observability/truefoundry)



##### Learn

  * [Overview](/en/learn/overview)
  * [Strategic LLM Selection Guide](/en/learn/llm-selection-guide)
  * [Conditional Tasks](/en/learn/conditional-tasks)
  * [Coding Agents](/en/learn/coding-agents)
  * [Create Custom Tools](/en/learn/create-custom-tools)
  * [Custom LLM Implementation](/en/learn/custom-llm)
  * [Custom Manager Agent](/en/learn/custom-manager-agent)
  * [Customize Agents](/en/learn/customizing-agents)
  * [Image Generation with DALL-E](/en/learn/dalle-image-generation)
  * [Force Tool Output as Result](/en/learn/force-tool-output-as-result)
  * [Hierarchical Process](/en/learn/hierarchical-process)
  * [Human Input on Execution](/en/learn/human-input-on-execution)
  * [Human-in-the-Loop (HITL) Workflows](/en/learn/human-in-the-loop)
  * [Kickoff Crew Asynchronously](/en/learn/kickoff-async)
  * [Kickoff Crew for Each](/en/learn/kickoff-for-each)
  * [Connect to any LLM](/en/learn/llm-connections)
  * [Using Multimodal Agents](/en/learn/multimodal-agents)
  * [Replay Tasks from Latest Crew Kickoff](/en/learn/replay-tasks-from-latest-crew-kickoff)
  * [Sequential Processes](/en/learn/sequential-process)
  * [Using Annotations in crew.py](/en/learn/using-annotations)
  * [Execution Hooks Overview](/en/learn/execution-hooks)
  * [LLM Call Hooks](/en/learn/llm-hooks)
  * [Tool Call Hooks](/en/learn/tool-hooks)



##### Telemetry

  * [Telemetry](/en/telemetry)



Core Concepts

# Crews

Copy page

Understanding and utilizing crews in the crewAI framework with comprehensive attributes and functionalities.

Copy page

## 

​

Overview

A crew in crewAI represents a collaborative group of agents working together to achieve a set of tasks. Each crew defines the strategy for task execution, agent collaboration, and the overall workflow.

## 

​

Crew Attributes

Attribute| Parameters| Description|   
---|---|---|---  
**Tasks**| `tasks`| A list of tasks assigned to the crew.|   
**Agents**| `agents`| A list of agents that are part of the crew.|   
**Process** _(optional)_| `process`| The process flow (e.g., sequential, hierarchical) the crew follows. Default is `sequential`.|   
**Verbose** _(optional)_| `verbose`| The verbosity level for logging during execution. Defaults to `False`.|   
**Manager LLM** _(optional)_| `manager_llm`| The language model used by the manager agent in a hierarchical process. **Required when using a hierarchical process.**|   
**Function Calling LLM** _(optional)_| `function_calling_llm`| If passed, the crew will use this LLM to do function calling for tools for all agents in the crew. Each agent can have its own LLM, which overrides the crew’s LLM for function calling.|   
**Config** _(optional)_| `config`| Optional configuration settings for the crew, in `Json` or `Dict[str, Any]` format.|   
**Max RPM** _(optional)_| `max_rpm`| Maximum requests per minute the crew adheres to during execution. Defaults to `None`.|   
**Memory** _(optional)_| `memory`| Utilized for storing execution memories (short-term, long-term, entity memory).|   
**Cache** _(optional)_| `cache`| Specifies whether to use a cache for storing the results of tools’ execution. Defaults to `True`.|   
**Embedder** _(optional)_| `embedder`| Configuration for the embedder to be used by the crew. Mostly used by memory for now. Default is `{"provider": "openai"}`.|   
**Step Callback** _(optional)_| `step_callback`| A function that is called after each step of every agent. This can be used to log the agent’s actions or to perform other operations; it won’t override the agent-specific `step_callback`.|   
**Task Callback** _(optional)_| `task_callback`| A function that is called after the completion of each task. Useful for monitoring or additional operations post-task execution.|   
**Share Crew** _(optional)_| `share_crew`| Whether you want to share the complete crew information and execution with the crewAI team to make the library better, and allow us to train models.|   
**Output Log File** _(optional)_| `output_log_file`| Set to True to save logs as logs.txt in the current directory or provide a file path. Logs will be in JSON format if the filename ends in .json, otherwise .txt. Defaults to `None`.|   
**Manager Agent** _(optional)_| `manager_agent`| `manager` sets a custom agent that will be used as a manager.|   
**Prompt File** _(optional)_| `prompt_file`| Path to the prompt JSON file to be used for the crew.|   
**Planning** _(optional)_| `planning`| Adds planning ability to the Crew. When activated before each Crew iteration, all Crew data is sent to an AgentPlanner that will plan the tasks and this plan will be added to each task description.|   
**Planning LLM** _(optional)_| `planning_llm`| The language model used by the AgentPlanner in a planning process.|   
**Knowledge Sources** _(optional)_| `knowledge_sources`| Knowledge sources available at the crew level, accessible to all the agents.|   
**Stream** _(optional)_| `stream`| Enable streaming output to receive real-time updates during crew execution. Returns a `CrewStreamingOutput` object that can be iterated for chunks. Defaults to `False`.|   
  
**Crew Max RPM** : The `max_rpm` attribute sets the maximum number of requests per minute the crew can perform to avoid rate limits and will override individual agents’ `max_rpm` settings if you set it.

## 

​

Creating Crews

There are two ways to create crews in CrewAI: using **YAML configuration (recommended)** or defining them **directly in code**.

### 

​

YAML Configuration (Recommended)

Using YAML configuration provides a cleaner, more maintainable way to define crews and is consistent with how agents and tasks are defined in CrewAI projects. After creating your CrewAI project as outlined in the [Installation](/en/installation) section, you can define your crew in a class that inherits from `CrewBase` and uses decorators to define agents, tasks, and the crew itself.

#### 

​

Example Crew Class with Decorators

code

Copy

Ask AI
    
    
    from crewai import Agent, Crew, Task, Process
    from crewai.project import CrewBase, agent, task, crew, before_kickoff, after_kickoff
    from crewai.agents.agent_builder.base_agent import BaseAgent
    from typing import List
    
    @CrewBase
    class YourCrewName:
        """Description of your crew"""
    
        agents: List[BaseAgent]
        tasks: List[Task]
    
        # Paths to your YAML configuration files
        # To see an example agent and task defined in YAML, checkout the following:
        # - Task: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
        # - Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
        agents_config = 'config/agents.yaml'
        tasks_config = 'config/tasks.yaml'
    
        @before_kickoff
        def prepare_inputs(self, inputs):
            # Modify inputs before the crew starts
            inputs['additional_data'] = "Some extra information"
            return inputs
    
        @after_kickoff
        def process_output(self, output):
            # Modify output after the crew finishes
            output.raw += "\nProcessed after kickoff."
            return output
    
        @agent
        def agent_one(self) -> Agent:
            return Agent(
                config=self.agents_config['agent_one'], # type: ignore[index]
                verbose=True
            )
    
        @agent
        def agent_two(self) -> Agent:
            return Agent(
                config=self.agents_config['agent_two'], # type: ignore[index]
                verbose=True
            )
    
        @task
        def task_one(self) -> Task:
            return Task(
                config=self.tasks_config['task_one'] # type: ignore[index]
            )
    
        @task
        def task_two(self) -> Task:
            return Task(
                config=self.tasks_config['task_two'] # type: ignore[index]
            )
    
        @crew
        def crew(self) -> Crew:
            return Crew(
                agents=self.agents,  # Automatically collected by the @agent decorator
                tasks=self.tasks,    # Automatically collected by the @task decorator.
                process=Process.sequential,
                verbose=True,
            )
    

How to run the above code:

code

Copy

Ask AI
    
    
    YourCrewName().crew().kickoff(inputs={"any": "input here"})
    

Tasks will be executed in the order they are defined.

The `CrewBase` class, along with these decorators, automates the collection of agents and tasks, reducing the need for manual management.

#### 

​

Decorators overview from `annotations.py`

CrewAI provides several decorators in the `annotations.py` file that are used to mark methods within your crew class for special handling:

  * `@CrewBase`: Marks the class as a crew base class.
  * `@agent`: Denotes a method that returns an `Agent` object.
  * `@task`: Denotes a method that returns a `Task` object.
  * `@crew`: Denotes the method that returns the `Crew` object.
  * `@before_kickoff`: (Optional) Marks a method to be executed before the crew starts.
  * `@after_kickoff`: (Optional) Marks a method to be executed after the crew finishes.

These decorators help in organizing your crew’s structure and automatically collecting agents and tasks without manually listing them.

### 

​

Direct Code Definition (Alternative)

Alternatively, you can define the crew directly in code without using YAML configuration files.

code

Copy

Ask AI
    
    
    from crewai import Agent, Crew, Task, Process
    from crewai_tools import YourCustomTool
    
    class YourCrewName:
        def agent_one(self) -> Agent:
            return Agent(
                role="Data Analyst",
                goal="Analyze data trends in the market",
                backstory="An experienced data analyst with a background in economics",
                verbose=True,
                tools=[YourCustomTool()]
            )
    
        def agent_two(self) -> Agent:
            return Agent(
                role="Market Researcher",
                goal="Gather information on market dynamics",
                backstory="A diligent researcher with a keen eye for detail",
                verbose=True
            )
    
        def task_one(self) -> Task:
            return Task(
                description="Collect recent market data and identify trends.",
                expected_output="A report summarizing key trends in the market.",
                agent=self.agent_one()
            )
    
        def task_two(self) -> Task:
            return Task(
                description="Research factors affecting market dynamics.",
                expected_output="An analysis of factors influencing the market.",
                agent=self.agent_two()
            )
    
        def crew(self) -> Crew:
            return Crew(
                agents=[self.agent_one(), self.agent_two()],
                tasks=[self.task_one(), self.task_two()],
                process=Process.sequential,
                verbose=True
            )
    

How to run the above code:

code

Copy

Ask AI
    
    
    YourCrewName().crew().kickoff(inputs={})
    

In this example:

  * Agents and tasks are defined directly within the class without decorators.
  * We manually create and manage the list of agents and tasks.
  * This approach provides more control but can be less maintainable for larger projects.



## 

​

Crew Output

The output of a crew in the CrewAI framework is encapsulated within the `CrewOutput` class. This class provides a structured way to access results of the crew’s execution, including various formats such as raw strings, JSON, and Pydantic models. The `CrewOutput` includes the results from the final task output, token usage, and individual task outputs.

### 

​

Crew Output Attributes

Attribute| Parameters| Type| Description  
---|---|---|---  
**Raw**| `raw`| `str`| The raw output of the crew. This is the default format for the output.  
**Pydantic**| `pydantic`| `Optional[BaseModel]`| A Pydantic model object representing the structured output of the crew.  
**JSON Dict**| `json_dict`| `Optional[Dict[str, Any]]`| A dictionary representing the JSON output of the crew.  
**Tasks Output**| `tasks_output`| `List[TaskOutput]`| A list of `TaskOutput` objects, each representing the output of a task in the crew.  
**Token Usage**| `token_usage`| `Dict[str, Any]`| A summary of token usage, providing insights into the language model’s performance during execution.  
  
### 

​

Crew Output Methods and Properties

Method/Property| Description  
---|---  
**json**|  Returns the JSON string representation of the crew output if the output format is JSON.  
**to_dict**|  Converts the JSON and Pydantic outputs to a dictionary.  
* ***str****|  Returns the string representation of the crew output, prioritizing Pydantic, then JSON, then raw.  
  
### 

​

Accessing Crew Outputs

Once a crew has been executed, its output can be accessed through the `output` attribute of the `Crew` object. The `CrewOutput` class provides various ways to interact with and present this output.

#### 

​

Example

Code

Copy

Ask AI
    
    
    # Example crew execution
    crew = Crew(
        agents=[research_agent, writer_agent],
        tasks=[research_task, write_article_task],
        verbose=True
    )
    
    crew_output = crew.kickoff()
    
    # Accessing the crew output
    print(f"Raw Output: {crew_output.raw}")
    if crew_output.json_dict:
        print(f"JSON Output: {json.dumps(crew_output.json_dict, indent=2)}")
    if crew_output.pydantic:
        print(f"Pydantic Output: {crew_output.pydantic}")
    print(f"Tasks Output: {crew_output.tasks_output}")
    print(f"Token Usage: {crew_output.token_usage}")
    

## 

​

Accessing Crew Logs

You can see real time log of the crew execution, by setting `output_log_file` as a `True(Boolean)` or a `file_name(str)`. Supports logging of events as both `file_name.txt` and `file_name.json`. In case of `True(Boolean)` will save as `logs.txt`. In case of `output_log_file` is set as `False(Boolean)` or `None`, the logs will not be populated.

Code

Copy

Ask AI
    
    
    # Save crew logs
    crew = Crew(output_log_file = True)  # Logs will be saved as logs.txt
    crew = Crew(output_log_file = file_name)  # Logs will be saved as file_name.txt
    crew = Crew(output_log_file = file_name.txt)  # Logs will be saved as file_name.txt
    crew = Crew(output_log_file = file_name.json)  # Logs will be saved as file_name.json
    

## 

​

Memory Utilization

Crews can utilize memory (short-term, long-term, and entity memory) to enhance their execution and learning over time. This feature allows crews to store and recall execution memories, aiding in decision-making and task execution strategies.

## 

​

Cache Utilization

Caches can be employed to store the results of tools’ execution, making the process more efficient by reducing the need to re-execute identical tasks.

## 

​

Crew Usage Metrics

After the crew execution, you can access the `usage_metrics` attribute to view the language model (LLM) usage metrics for all tasks executed by the crew. This provides insights into operational efficiency and areas for improvement.

Code

Copy

Ask AI
    
    
    # Access the crew's usage metrics
    crew = Crew(agents=[agent1, agent2], tasks=[task1, task2])
    crew.kickoff()
    print(crew.usage_metrics)
    

## 

​

Crew Execution Process

  * **Sequential Process** : Tasks are executed one after another, allowing for a linear flow of work.
  * **Hierarchical Process** : A manager agent coordinates the crew, delegating tasks and validating outcomes before proceeding. **Note** : A `manager_llm` or `manager_agent` is required for this process and it’s essential for validating the process flow.



### 

​

Kicking Off a Crew

Once your crew is assembled, initiate the workflow with the `kickoff()` method. This starts the execution process according to the defined process flow.

Code

Copy

Ask AI
    
    
    # Start the crew's task execution
    result = my_crew.kickoff()
    print(result)
    

### 

​

Different Ways to Kick Off a Crew

Once your crew is assembled, initiate the workflow with the appropriate kickoff method. CrewAI provides several methods for better control over the kickoff process: `kickoff()`, `kickoff_for_each()`, `kickoff_async()`, and `kickoff_for_each_async()`.

  * `kickoff()`: Starts the execution process according to the defined process flow.
  * `kickoff_for_each()`: Executes tasks sequentially for each provided input event or item in the collection.
  * `kickoff_async()`: Initiates the workflow asynchronously.
  * `kickoff_for_each_async()`: Executes tasks concurrently for each provided input event or item, leveraging asynchronous processing.



Code

Copy

Ask AI
    
    
    # Start the crew's task execution
    result = my_crew.kickoff()
    print(result)
    
    # Example of using kickoff_for_each
    inputs_array = [{'topic': 'AI in healthcare'}, {'topic': 'AI in finance'}]
    results = my_crew.kickoff_for_each(inputs=inputs_array)
    for result in results:
        print(result)
    
    # Example of using kickoff_async
    inputs = {'topic': 'AI in healthcare'}
    async_result = await my_crew.kickoff_async(inputs=inputs)
    print(async_result)
    
    # Example of using kickoff_for_each_async
    inputs_array = [{'topic': 'AI in healthcare'}, {'topic': 'AI in finance'}]
    async_results = await my_crew.kickoff_for_each_async(inputs=inputs_array)
    for async_result in async_results:
        print(async_result)
    

These methods provide flexibility in how you manage and execute tasks within your crew, allowing for both synchronous and asynchronous workflows tailored to your needs.

### 

​

Streaming Crew Execution

For real-time visibility into crew execution, you can enable streaming to receive output as it’s generated:

Code

Copy

Ask AI
    
    
    # Enable streaming
    crew = Crew(
        agents=[researcher],
        tasks=[task],
        stream=True
    )
    
    # Iterate over streaming output
    streaming = crew.kickoff(inputs={"topic": "AI"})
    for chunk in streaming:
        print(chunk.content, end="", flush=True)
    
    # Access final result
    result = streaming.result
    

Learn more about streaming in the [Streaming Crew Execution](/en/learn/streaming-crew-execution) guide.

### 

​

Replaying from a Specific Task

You can now replay from a specific task using our CLI command `replay`. The replay feature in CrewAI allows you to replay from a specific task using the command-line interface (CLI). By running the command `crewai replay -t <task_id>`, you can specify the `task_id` for the replay process. Kickoffs will now save the latest kickoffs returned task outputs locally for you to be able to replay from.

### 

​

Replaying from a Specific Task Using the CLI

To use the replay feature, follow these steps:

  1. Open your terminal or command prompt.
  2. Navigate to the directory where your CrewAI project is located.
  3. Run the following command:

To view the latest kickoff task IDs, use:

Copy

Ask AI
    
    
    crewai log-tasks-outputs
    

Then, to replay from a specific task, use:

Copy

Ask AI
    
    
    crewai replay -t <task_id>
    

These commands let you replay from your latest kickoff tasks, still retaining context from previously executed tasks.

Was this page helpful?

YesNo

[TasksPrevious](/en/concepts/tasks)[FlowsNext](/en/concepts/flows)

Ctrl+I

[website](https://crewai.com)[x](https://x.com/crewAIInc)[github](https://github.com/crewAIInc/crewAI)[linkedin](https://www.linkedin.com/company/crewai-inc)[youtube](https://youtube.com/@crewAIInc)[reddit](https://www.reddit.com/r/crewAIInc/)

[Powered by Mintlify](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=crewai)

Assistant

Responses are generated using AI and may contain mistakes.


---

# Source: https://docs.crewai.com/en/concepts/flows

Skip to main content

[CrewAI home page![light logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)![dark logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)](/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl K

Search...

Navigation

Core Concepts

Flows

[Home](/)[Documentation](/en/introduction)[AOP](/en/enterprise/introduction)[API Reference](/en/api-reference/introduction)[Examples](/en/examples/example)[Changelog](/en/changelog)

  * [Website](https://crewai.com)
  * [Forum](https://community.crewai.com)
  * [Blog](https://blog.crewai.com)
  * [CrewGPT](https://chatgpt.com/g/g-qqTuUWsBY-crewai-assistant)



##### Get Started

  * [Introduction](/en/introduction)
  * [Installation](/en/installation)
  * [Quickstart](/en/quickstart)



##### Guides

  * Strategy

  * Agents

  * Crews

  * Flows

  * Advanced




##### Core Concepts

  * [Agents](/en/concepts/agents)
  * [Tasks](/en/concepts/tasks)
  * [Crews](/en/concepts/crews)
  * [Flows](/en/concepts/flows)
  * [Knowledge](/en/concepts/knowledge)
  * [LLMs](/en/concepts/llms)
  * [Processes](/en/concepts/processes)
  * [Collaboration](/en/concepts/collaboration)
  * [Training](/en/concepts/training)
  * [Memory](/en/concepts/memory)
  * [Reasoning](/en/concepts/reasoning)
  * [Planning](/en/concepts/planning)
  * [Testing](/en/concepts/testing)
  * [CLI](/en/concepts/cli)
  * [Tools](/en/concepts/tools)
  * [Event Listeners](/en/concepts/event-listener)



##### MCP Integration

  * [MCP Servers as Tools in CrewAI](/en/mcp/overview)
  * [MCP DSL Integration](/en/mcp/dsl-integration)
  * [Stdio Transport](/en/mcp/stdio)
  * [SSE Transport](/en/mcp/sse)
  * [Streamable HTTP Transport](/en/mcp/streamable-http)
  * [Connecting to Multiple MCP Servers](/en/mcp/multiple-servers)
  * [MCP Security Considerations](/en/mcp/security)



##### Tools

  * [Tools Overview](/en/tools/overview)
  * File & Document

  * Web Scraping & Browsing

  * Search & Research

  * Database & Data

  * AI & Machine Learning

  * Cloud & Storage

  * Integrations

  * Automation




##### Observability

  * [CrewAI Tracing](/en/observability/tracing)
  * [Overview](/en/observability/overview)
  * [Arize Phoenix](/en/observability/arize-phoenix)
  * [Braintrust](/en/observability/braintrust)
  * [Datadog Integration](/en/observability/datadog)
  * [LangDB Integration](/en/observability/langdb)
  * [Langfuse Integration](/en/observability/langfuse)
  * [Langtrace Integration](/en/observability/langtrace)
  * [Maxim Integration](/en/observability/maxim)
  * [MLflow Integration](/en/observability/mlflow)
  * [Neatlogs Integration](/en/observability/neatlogs)
  * [OpenLIT Integration](/en/observability/openlit)
  * [Opik Integration](/en/observability/opik)
  * [Patronus AI Evaluation](/en/observability/patronus-evaluation)
  * [Portkey Integration](/en/observability/portkey)
  * [Weave Integration](/en/observability/weave)
  * [TrueFoundry Integration](/en/observability/truefoundry)



##### Learn

  * [Overview](/en/learn/overview)
  * [Strategic LLM Selection Guide](/en/learn/llm-selection-guide)
  * [Conditional Tasks](/en/learn/conditional-tasks)
  * [Coding Agents](/en/learn/coding-agents)
  * [Create Custom Tools](/en/learn/create-custom-tools)
  * [Custom LLM Implementation](/en/learn/custom-llm)
  * [Custom Manager Agent](/en/learn/custom-manager-agent)
  * [Customize Agents](/en/learn/customizing-agents)
  * [Image Generation with DALL-E](/en/learn/dalle-image-generation)
  * [Force Tool Output as Result](/en/learn/force-tool-output-as-result)
  * [Hierarchical Process](/en/learn/hierarchical-process)
  * [Human Input on Execution](/en/learn/human-input-on-execution)
  * [Human-in-the-Loop (HITL) Workflows](/en/learn/human-in-the-loop)
  * [Kickoff Crew Asynchronously](/en/learn/kickoff-async)
  * [Kickoff Crew for Each](/en/learn/kickoff-for-each)
  * [Connect to any LLM](/en/learn/llm-connections)
  * [Using Multimodal Agents](/en/learn/multimodal-agents)
  * [Replay Tasks from Latest Crew Kickoff](/en/learn/replay-tasks-from-latest-crew-kickoff)
  * [Sequential Processes](/en/learn/sequential-process)
  * [Using Annotations in crew.py](/en/learn/using-annotations)
  * [Execution Hooks Overview](/en/learn/execution-hooks)
  * [LLM Call Hooks](/en/learn/llm-hooks)
  * [Tool Call Hooks](/en/learn/tool-hooks)



##### Telemetry

  * [Telemetry](/en/telemetry)



Core Concepts

# Flows

Copy page

Learn how to create and manage AI workflows using CrewAI Flows.

Copy page

## 

​

Overview

CrewAI Flows is a powerful feature designed to streamline the creation and management of AI workflows. Flows allow developers to combine and coordinate coding tasks and Crews efficiently, providing a robust framework for building sophisticated AI automations. Flows allow you to create structured, event-driven workflows. They provide a seamless way to connect multiple tasks, manage state, and control the flow of execution in your AI applications. With Flows, you can easily design and implement multi-step processes that leverage the full potential of CrewAI’s capabilities.

  1. **Simplified Workflow Creation** : Easily chain together multiple Crews and tasks to create complex AI workflows.
  2. **State Management** : Flows make it super easy to manage and share state between different tasks in your workflow.
  3. **Event-Driven Architecture** : Built on an event-driven model, allowing for dynamic and responsive workflows.
  4. **Flexible Control Flow** : Implement conditional logic, loops, and branching within your workflows.



## 

​

Getting Started

Let’s create a simple Flow where you will use OpenAI to generate a random city in one task and then use that city to generate a fun fact in another task.

Code

Copy

Ask AI
    
    
    from crewai.flow.flow import Flow, listen, start
    from dotenv import load_dotenv
    from litellm import completion
    
    
    class ExampleFlow(Flow):
        model = "gpt-4o-mini"
    
        @start()
        def generate_city(self):
            print("Starting flow")
            # Each flow state automatically gets a unique ID
            print(f"Flow State ID: {self.state['id']}")
    
            response = completion(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": "Return the name of a random city in the world.",
                    },
                ],
            )
    
            random_city = response["choices"][0]["message"]["content"]
            # Store the city in our state
            self.state["city"] = random_city
            print(f"Random City: {random_city}")
    
            return random_city
    
        @listen(generate_city)
        def generate_fun_fact(self, random_city):
            response = completion(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": f"Tell me a fun fact about {random_city}",
                    },
                ],
            )
    
            fun_fact = response["choices"][0]["message"]["content"]
            # Store the fun fact in our state
            self.state["fun_fact"] = fun_fact
            return fun_fact
    
    
    
    flow = ExampleFlow()
    flow.plot()
    result = flow.kickoff()
    
    print(f"Generated fun fact: {result}")
    

![Flow Visual image](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-1.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=18b381277b7b017abf7cb19bc5e03923) In the above example, we have created a simple Flow that generates a random city using OpenAI and then generates a fun fact about that city. The Flow consists of two tasks: `generate_city` and `generate_fun_fact`. The `generate_city` task is the starting point of the Flow, and the `generate_fun_fact` task listens for the output of the `generate_city` task. Each Flow instance automatically receives a unique identifier (UUID) in its state, which helps track and manage flow executions. The state can also store additional data (like the generated city and fun fact) that persists throughout the flow’s execution. When you run the Flow, it will:

  1. Generate a unique ID for the flow state
  2. Generate a random city and store it in the state
  3. Generate a fun fact about that city and store it in the state
  4. Print the results to the console

The state’s unique ID and stored data can be useful for tracking flow executions and maintaining context between tasks. **Note:** Ensure you have set up your `.env` file to store your `OPENAI_API_KEY`. This key is necessary for authenticating requests to the OpenAI API.

### 

​

@start()

The `@start()` decorator marks entry points for a Flow. You can:

  * Declare multiple unconditional starts: `@start()`
  * Gate a start on a prior method or router label: `@start("method_or_label")`
  * Provide a callable condition to control when a start should fire

All satisfied `@start()` methods will execute (often in parallel) when the Flow begins or resumes.

### 

​

@listen()

The `@listen()` decorator is used to mark a method as a listener for the output of another task in the Flow. The method decorated with `@listen()` will be executed when the specified task emits an output. The method can access the output of the task it is listening to as an argument.

#### 

​

Usage

The `@listen()` decorator can be used in several ways:

  1. **Listening to a Method by Name** : You can pass the name of the method you want to listen to as a string. When that method completes, the listener method will be triggered.

Code

Copy

Ask AI
         
         @listen("generate_city")
         def generate_fun_fact(self, random_city):
             # Implementation
         

  2. **Listening to a Method Directly** : You can pass the method itself. When that method completes, the listener method will be triggered.

Code

Copy

Ask AI
         
         @listen(generate_city)
         def generate_fun_fact(self, random_city):
             # Implementation
         




### 

​

Flow Output

Accessing and handling the output of a Flow is essential for integrating your AI workflows into larger applications or systems. CrewAI Flows provide straightforward mechanisms to retrieve the final output, access intermediate results, and manage the overall state of your Flow.

#### 

​

Retrieving the Final Output

When you run a Flow, the final output is determined by the last method that completes. The `kickoff()` method returns the output of this final method. Here’s how you can access the final output:

Code

Output

Copy

Ask AI
    
    
    from crewai.flow.flow import Flow, listen, start
    
    class OutputExampleFlow(Flow):
        @start()
        def first_method(self):
            return "Output from first_method"
    
        @listen(first_method)
        def second_method(self, first_output):
            return f"Second method received: {first_output}"
    
    
    flow = OutputExampleFlow()
    flow.plot("my_flow_plot")
    final_output = flow.kickoff()
    
    print("---- Final Output ----")
    print(final_output)
    

![Flow Visual image](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3d987994d2c99a06a3cf149c71831fd5) In this example, the `second_method` is the last method to complete, so its output will be the final output of the Flow. The `kickoff()` method will return the final output, which is then printed to the console. The `plot()` method will generate the HTML file, which will help you understand the flow.

#### 

​

Accessing and Updating State

In addition to retrieving the final output, you can also access and update the state within your Flow. The state can be used to store and share data between different methods in the Flow. After the Flow has run, you can access the state to retrieve any information that was added or updated during the execution. Here’s an example of how to update and access the state:

Code

Output

Copy

Ask AI
    
    
    from crewai.flow.flow import Flow, listen, start
    from pydantic import BaseModel
    
    class ExampleState(BaseModel):
        counter: int = 0
        message: str = ""
    
    class StateExampleFlow(Flow[ExampleState]):
    
        @start()
        def first_method(self):
            self.state.message = "Hello from first_method"
            self.state.counter += 1
    
        @listen(first_method)
        def second_method(self):
            self.state.message += " - updated by second_method"
            self.state.counter += 1
            return self.state.message
    
    flow = StateExampleFlow()
    flow.plot("my_flow_plot")
    final_output = flow.kickoff()
    print(f"Final Output: {final_output}")
    print("Final State:")
    print(flow.state)
    

![Flow Visual image](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3d987994d2c99a06a3cf149c71831fd5) In this example, the state is updated by both `first_method` and `second_method`. After the Flow has run, you can access the final state to see the updates made by these methods. By ensuring that the final method’s output is returned and providing access to the state, CrewAI Flows make it easy to integrate the results of your AI workflows into larger applications or systems, while also maintaining and accessing the state throughout the Flow’s execution.

## 

​

Flow State Management

Managing state effectively is crucial for building reliable and maintainable AI workflows. CrewAI Flows provides robust mechanisms for both unstructured and structured state management, allowing developers to choose the approach that best fits their application’s needs.

### 

​

Unstructured State Management

In unstructured state management, all state is stored in the `state` attribute of the `Flow` class. This approach offers flexibility, enabling developers to add or modify state attributes on the fly without defining a strict schema. Even with unstructured states, CrewAI Flows automatically generates and maintains a unique identifier (UUID) for each state instance.

Code

Copy

Ask AI
    
    
    from crewai.flow.flow import Flow, listen, start
    
    class UnstructuredExampleFlow(Flow):
    
        @start()
        def first_method(self):
            # The state automatically includes an 'id' field
            print(f"State ID: {self.state['id']}")
            self.state['counter'] = 0
            self.state['message'] = "Hello from structured flow"
    
        @listen(first_method)
        def second_method(self):
            self.state['counter'] += 1
            self.state['message'] += " - updated"
    
        @listen(second_method)
        def third_method(self):
            self.state['counter'] += 1
            self.state['message'] += " - updated again"
    
            print(f"State after third_method: {self.state}")
    
    
    flow = UnstructuredExampleFlow()
    flow.plot("my_flow_plot")
    flow.kickoff()
    

![Flow Visual image](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1d64a80a490430f29b7fa1085a3062c4) **Note:** The `id` field is automatically generated and preserved throughout the flow’s execution. You don’t need to manage or set it manually, and it will be maintained even when updating the state with new data. **Key Points:**

  * **Flexibility:** You can dynamically add attributes to `self.state` without predefined constraints.
  * **Simplicity:** Ideal for straightforward workflows where state structure is minimal or varies significantly.



### 

​

Structured State Management

Structured state management leverages predefined schemas to ensure consistency and type safety across the workflow. By using models like Pydantic’s `BaseModel`, developers can define the exact shape of the state, enabling better validation and auto-completion in development environments. Each state in CrewAI Flows automatically receives a unique identifier (UUID) to help track and manage state instances. This ID is automatically generated and managed by the Flow system.

Code

Copy

Ask AI
    
    
    from crewai.flow.flow import Flow, listen, start
    from pydantic import BaseModel
    
    
    class ExampleState(BaseModel):
        # Note: 'id' field is automatically added to all states
        counter: int = 0
        message: str = ""
    
    
    class StructuredExampleFlow(Flow[ExampleState]):
    
        @start()
        def first_method(self):
            # Access the auto-generated ID if needed
            print(f"State ID: {self.state.id}")
            self.state.message = "Hello from structured flow"
    
        @listen(first_method)
        def second_method(self):
            self.state.counter += 1
            self.state.message += " - updated"
    
        @listen(second_method)
        def third_method(self):
            self.state.counter += 1
            self.state.message += " - updated again"
    
            print(f"State after third_method: {self.state}")
    
    
    flow = StructuredExampleFlow()
    flow.kickoff()
    

![Flow Visual image](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1d64a80a490430f29b7fa1085a3062c4) **Key Points:**

  * **Defined Schema:** `ExampleState` clearly outlines the state structure, enhancing code readability and maintainability.
  * **Type Safety:** Leveraging Pydantic ensures that state attributes adhere to the specified types, reducing runtime errors.
  * **Auto-Completion:** IDEs can provide better auto-completion and error checking based on the defined state model.



### 

​

Choosing Between Unstructured and Structured State Management

  * **Use Unstructured State Management when:**
    * The workflow’s state is simple or highly dynamic.
    * Flexibility is prioritized over strict state definitions.
    * Rapid prototyping is required without the overhead of defining schemas.
  * **Use Structured State Management when:**
    * The workflow requires a well-defined and consistent state structure.
    * Type safety and validation are important for your application’s reliability.
    * You want to leverage IDE features like auto-completion and type checking for better developer experience.

By providing both unstructured and structured state management options, CrewAI Flows empowers developers to build AI workflows that are both flexible and robust, catering to a wide range of application requirements.

## 

​

Flow Persistence

The @persist decorator enables automatic state persistence in CrewAI Flows, allowing you to maintain flow state across restarts or different workflow executions. This decorator can be applied at either the class level or method level, providing flexibility in how you manage state persistence.

### 

​

Class-Level Persistence

When applied at the class level, the @persist decorator automatically persists all flow method states:

Copy

Ask AI
    
    
    @persist  # Using SQLiteFlowPersistence by default
    class MyFlow(Flow[MyState]):
        @start()
        def initialize_flow(self):
            # This method will automatically have its state persisted
            self.state.counter = 1
            print("Initialized flow. State ID:", self.state.id)
    
        @listen(initialize_flow)
        def next_step(self):
            # The state (including self.state.id) is automatically reloaded
            self.state.counter += 1
            print("Flow state is persisted. Counter:", self.state.counter)
    

### 

​

Method-Level Persistence

For more granular control, you can apply @persist to specific methods:

Copy

Ask AI
    
    
    class AnotherFlow(Flow[dict]):
        @persist  # Persists only this method's state
        @start()
        def begin(self):
            if "runs" not in self.state:
                self.state["runs"] = 0
            self.state["runs"] += 1
            print("Method-level persisted runs:", self.state["runs"])
    

### 

​

How It Works

  1. **Unique State Identification**
     * Each flow state automatically receives a unique UUID
     * The ID is preserved across state updates and method calls
     * Supports both structured (Pydantic BaseModel) and unstructured (dictionary) states
  2. **Default SQLite Backend**
     * SQLiteFlowPersistence is the default storage backend
     * States are automatically saved to a local SQLite database
     * Robust error handling ensures clear messages if database operations fail
  3. **Error Handling**
     * Comprehensive error messages for database operations
     * Automatic state validation during save and load
     * Clear feedback when persistence operations encounter issues



### 

​

Important Considerations

  * **State Types** : Both structured (Pydantic BaseModel) and unstructured (dictionary) states are supported
  * **Automatic ID** : The `id` field is automatically added if not present
  * **State Recovery** : Failed or restarted flows can automatically reload their previous state
  * **Custom Implementation** : You can provide your own FlowPersistence implementation for specialized storage needs



### 

​

Technical Advantages

  1. **Precise Control Through Low-Level Access**
     * Direct access to persistence operations for advanced use cases
     * Fine-grained control via method-level persistence decorators
     * Built-in state inspection and debugging capabilities
     * Full visibility into state changes and persistence operations
  2. **Enhanced Reliability**
     * Automatic state recovery after system failures or restarts
     * Transaction-based state updates for data integrity
     * Comprehensive error handling with clear error messages
     * Robust validation during state save and load operations
  3. **Extensible Architecture**
     * Customizable persistence backend through FlowPersistence interface
     * Support for specialized storage solutions beyond SQLite
     * Compatible with both structured (Pydantic) and unstructured (dict) states
     * Seamless integration with existing CrewAI flow patterns

The persistence system’s architecture emphasizes technical precision and customization options, allowing developers to maintain full control over state management while benefiting from built-in reliability features.

## 

​

Flow Control

### 

​

Conditional Logic: `or`

The `or_` function in Flows allows you to listen to multiple methods and trigger the listener method when any of the specified methods emit an output.

Code

Output

Copy

Ask AI
    
    
    from crewai.flow.flow import Flow, listen, or_, start
    
    class OrExampleFlow(Flow):
    
        @start()
        def start_method(self):
            return "Hello from the start method"
    
        @listen(start_method)
        def second_method(self):
            return "Hello from the second method"
    
        @listen(or_(start_method, second_method))
        def logger(self, result):
            print(f"Logger: {result}")
    
    
    
    flow = OrExampleFlow()
    flow.plot("my_flow_plot")
    flow.kickoff()
    

![Flow Visual image](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-4.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=88ce9c9f10781b835f170847bc541a13) When you run this Flow, the `logger` method will be triggered by the output of either the `start_method` or the `second_method`. The `or_` function is used to listen to multiple methods and trigger the listener method when any of the specified methods emit an output.

### 

​

Conditional Logic: `and`

The `and_` function in Flows allows you to listen to multiple methods and trigger the listener method only when all the specified methods emit an output.

Code

Output

Copy

Ask AI
    
    
    from crewai.flow.flow import Flow, and_, listen, start
    
    class AndExampleFlow(Flow):
    
        @start()
        def start_method(self):
            self.state["greeting"] = "Hello from the start method"
    
        @listen(start_method)
        def second_method(self):
            self.state["joke"] = "What do computers eat? Microchips."
    
        @listen(and_(start_method, second_method))
        def logger(self):
            print("---- Logger ----")
            print(self.state)
    
    flow = AndExampleFlow()
    flow.plot()
    flow.kickoff()
    

![Flow Visual image](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-5.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=104318219be9d3502ac57ebb513aded7) When you run this Flow, the `logger` method will be triggered only when both the `start_method` and the `second_method` emit an output. The `and_` function is used to listen to multiple methods and trigger the listener method only when all the specified methods emit an output.

### 

​

Router

The `@router()` decorator in Flows allows you to define conditional routing logic based on the output of a method. You can specify different routes based on the output of the method, allowing you to control the flow of execution dynamically.

Code

Output

Copy

Ask AI
    
    
    import random
    from crewai.flow.flow import Flow, listen, router, start
    from pydantic import BaseModel
    
    class ExampleState(BaseModel):
        success_flag: bool = False
    
    class RouterFlow(Flow[ExampleState]):
    
        @start()
        def start_method(self):
            print("Starting the structured flow")
            random_boolean = random.choice([True, False])
            self.state.success_flag = random_boolean
    
        @router(start_method)
        def second_method(self):
            if self.state.success_flag:
                return "success"
            else:
                return "failed"
    
        @listen("success")
        def third_method(self):
            print("Third method running")
    
        @listen("failed")
        def fourth_method(self):
            print("Fourth method running")
    
    
    flow = RouterFlow()
    flow.plot("my_flow_plot")
    flow.kickoff()
    

![Flow Visual image](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-6.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f8cad73f073b4e936ef68d88545f1777) In the above example, the `start_method` generates a random boolean value and sets it in the state. The `second_method` uses the `@router()` decorator to define conditional routing logic based on the value of the boolean. If the boolean is `True`, the method returns `"success"`, and if it is `False`, the method returns `"failed"`. The `third_method` and `fourth_method` listen to the output of the `second_method` and execute based on the returned value. When you run this Flow, the output will change based on the random boolean value generated by the `start_method`.

## 

​

Adding Agents to Flows

Agents can be seamlessly integrated into your flows, providing a lightweight alternative to full Crews when you need simpler, focused task execution. Here’s an example of how to use an Agent within a flow to perform market research:

Copy

Ask AI
    
    
    import asyncio
    from typing import Any, Dict, List
    
    from crewai_tools import SerperDevTool
    from pydantic import BaseModel, Field
    
    from crewai.agent import Agent
    from crewai.flow.flow import Flow, listen, start
    
    
    # Define a structured output format
    class MarketAnalysis(BaseModel):
        key_trends: List[str] = Field(description="List of identified market trends")
        market_size: str = Field(description="Estimated market size")
        competitors: List[str] = Field(description="Major competitors in the space")
    
    
    # Define flow state
    class MarketResearchState(BaseModel):
        product: str = ""
        analysis: MarketAnalysis | None = None
    
    
    # Create a flow class
    class MarketResearchFlow(Flow[MarketResearchState]):
        @start()
        def initialize_research(self) -> Dict[str, Any]:
            print(f"Starting market research for {self.state.product}")
            return {"product": self.state.product}
    
        @listen(initialize_research)
        async def analyze_market(self) -> Dict[str, Any]:
            # Create an Agent for market research
            analyst = Agent(
                role="Market Research Analyst",
                goal=f"Analyze the market for {self.state.product}",
                backstory="You are an experienced market analyst with expertise in "
                "identifying market trends and opportunities.",
                tools=[SerperDevTool()],
                verbose=True,
            )
    
            # Define the research query
            query = f"""
            Research the market for {self.state.product}. Include:
            1. Key market trends
            2. Market size
            3. Major competitors
    
            Format your response according to the specified structure.
            """
    
            # Execute the analysis with structured output format
            result = await analyst.kickoff_async(query, response_format=MarketAnalysis)
            if result.pydantic:
                print("result", result.pydantic)
            else:
                print("result", result)
    
            # Return the analysis to update the state
            return {"analysis": result.pydantic}
    
        @listen(analyze_market)
        def present_results(self, analysis) -> None:
            print("\nMarket Analysis Results")
            print("=====================")
    
            if isinstance(analysis, dict):
                # If we got a dict with 'analysis' key, extract the actual analysis object
                market_analysis = analysis.get("analysis")
            else:
                market_analysis = analysis
    
            if market_analysis and isinstance(market_analysis, MarketAnalysis):
                print("\nKey Market Trends:")
                for trend in market_analysis.key_trends:
                    print(f"- {trend}")
    
                print(f"\nMarket Size: {market_analysis.market_size}")
    
                print("\nMajor Competitors:")
                for competitor in market_analysis.competitors:
                    print(f"- {competitor}")
            else:
                print("No structured analysis data available.")
                print("Raw analysis:", analysis)
    
    
    # Usage example
    async def run_flow():
        flow = MarketResearchFlow()
        flow.plot("MarketResearchFlowPlot")
        result = await flow.kickoff_async(inputs={"product": "AI-powered chatbots"})
        return result
    
    
    # Run the flow
    if __name__ == "__main__":
        asyncio.run(run_flow())
    

![Flow Visual image](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-7.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=6c60457e1a2b9bc0ef957c373a88359b) This example demonstrates several key features of using Agents in flows:

  1. **Structured Output** : Using Pydantic models to define the expected output format (`MarketAnalysis`) ensures type safety and structured data throughout the flow.
  2. **State Management** : The flow state (`MarketResearchState`) maintains context between steps and stores both inputs and outputs.
  3. **Tool Integration** : Agents can use tools (like `WebsiteSearchTool`) to enhance their capabilities.



## 

​

Adding Crews to Flows

Creating a flow with multiple crews in CrewAI is straightforward. You can generate a new CrewAI project that includes all the scaffolding needed to create a flow with multiple crews by running the following command:

Copy

Ask AI
    
    
    crewai create flow name_of_flow
    

This command will generate a new CrewAI project with the necessary folder structure. The generated project includes a prebuilt crew called `poem_crew` that is already working. You can use this crew as a template by copying, pasting, and editing it to create other crews.

### 

​

Folder Structure

After running the `crewai create flow name_of_flow` command, you will see a folder structure similar to the following:

Directory/File| Description  
---|---  
`name_of_flow/`| Root directory for the flow.  
├── `crews/`| Contains directories for specific crews.  
│ └── `poem_crew/`| Directory for the “poem_crew” with its configurations and scripts.  
│ ├── `config/`| Configuration files directory for the “poem_crew”.  
│ │ ├── `agents.yaml`| YAML file defining the agents for “poem_crew”.  
│ │ └── `tasks.yaml`| YAML file defining the tasks for “poem_crew”.  
│ ├── `poem_crew.py`| Script for “poem_crew” functionality.  
├── `tools/`| Directory for additional tools used in the flow.  
│ └── `custom_tool.py`| Custom tool implementation.  
├── `main.py`| Main script for running the flow.  
├── `README.md`| Project description and instructions.  
├── `pyproject.toml`| Configuration file for project dependencies and settings.  
└── `.gitignore`| Specifies files and directories to ignore in version control.  
  
### 

​

Building Your Crews

In the `crews` folder, you can define multiple crews. Each crew will have its own folder containing configuration files and the crew definition file. For example, the `poem_crew` folder contains:

  * `config/agents.yaml`: Defines the agents for the crew.
  * `config/tasks.yaml`: Defines the tasks for the crew.
  * `poem_crew.py`: Contains the crew definition, including agents, tasks, and the crew itself.

You can copy, paste, and edit the `poem_crew` to create other crews.

### 

​

Connecting Crews in `main.py`

The `main.py` file is where you create your flow and connect the crews together. You can define your flow by using the `Flow` class and the decorators `@start` and `@listen` to specify the flow of execution. Here’s an example of how you can connect the `poem_crew` in the `main.py` file:

Code

Copy

Ask AI
    
    
    #!/usr/bin/env python
    from random import randint
    
    from pydantic import BaseModel
    from crewai.flow.flow import Flow, listen, start
    from .crews.poem_crew.poem_crew import PoemCrew
    
    class PoemState(BaseModel):
        sentence_count: int = 1
        poem: str = ""
    
    class PoemFlow(Flow[PoemState]):
    
        @start()
        def generate_sentence_count(self):
            print("Generating sentence count")
            self.state.sentence_count = randint(1, 5)
    
        @listen(generate_sentence_count)
        def generate_poem(self):
            print("Generating poem")
            result = PoemCrew().crew().kickoff(inputs={"sentence_count": self.state.sentence_count})
    
            print("Poem generated", result.raw)
            self.state.poem = result.raw
    
        @listen(generate_poem)
        def save_poem(self):
            print("Saving poem")
            with open("poem.txt", "w") as f:
                f.write(self.state.poem)
    
    def kickoff():
        poem_flow = PoemFlow()
        poem_flow.kickoff()
    
    
    def plot():
        poem_flow = PoemFlow()
        poem_flow.plot("PoemFlowPlot")
    
    if __name__ == "__main__":
        kickoff()
        plot()
    

In this example, the `PoemFlow` class defines a flow that generates a sentence count, uses the `PoemCrew` to generate a poem, and then saves the poem to a file. The flow is kicked off by calling the `kickoff()` method. The PoemFlowPlot will be generated by `plot()` method. ![Flow Visual image](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-8.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=5321ca5d1f3c662dc7cff6950ba46000)

### 

​

Running the Flow

(Optional) Before running the flow, you can install the dependencies by running:

Copy

Ask AI
    
    
    crewai install
    

Once all of the dependencies are installed, you need to activate the virtual environment by running:

Copy

Ask AI
    
    
    source .venv/bin/activate
    

After activating the virtual environment, you can run the flow by executing one of the following commands:

Copy

Ask AI
    
    
    crewai flow kickoff
    

or

Copy

Ask AI
    
    
    uv run kickoff
    

The flow will execute, and you should see the output in the console.

## 

​

Plot Flows

Visualizing your AI workflows can provide valuable insights into the structure and execution paths of your flows. CrewAI offers a powerful visualization tool that allows you to generate interactive plots of your flows, making it easier to understand and optimize your AI workflows.

### 

​

What are Plots?

Plots in CrewAI are graphical representations of your AI workflows. They display the various tasks, their connections, and the flow of data between them. This visualization helps in understanding the sequence of operations, identifying bottlenecks, and ensuring that the workflow logic aligns with your expectations.

### 

​

How to Generate a Plot

CrewAI provides two convenient methods to generate plots of your flows:

#### 

​

Option 1: Using the `plot()` Method

If you are working directly with a flow instance, you can generate a plot by calling the `plot()` method on your flow object. This method will create an HTML file containing the interactive plot of your flow.

Code

Copy

Ask AI
    
    
    # Assuming you have a flow instance
    flow.plot("my_flow_plot")
    

This will generate a file named `my_flow_plot.html` in your current directory. You can open this file in a web browser to view the interactive plot.

#### 

​

Option 2: Using the Command Line

If you are working within a structured CrewAI project, you can generate a plot using the command line. This is particularly useful for larger projects where you want to visualize the entire flow setup.

Copy

Ask AI
    
    
    crewai flow plot
    

This command will generate an HTML file with the plot of your flow, similar to the `plot()` method. The file will be saved in your project directory, and you can open it in a web browser to explore the flow.

### 

​

Understanding the Plot

The generated plot will display nodes representing the tasks in your flow, with directed edges indicating the flow of execution. The plot is interactive, allowing you to zoom in and out, and hover over nodes to see additional details. By visualizing your flows, you can gain a clearer understanding of the workflow’s structure, making it easier to debug, optimize, and communicate your AI processes to others.

### 

​

Conclusion

Plotting your flows is a powerful feature of CrewAI that enhances your ability to design and manage complex AI workflows. Whether you choose to use the `plot()` method or the command line, generating plots will provide you with a visual representation of your workflows, aiding in both development and presentation.

## 

​

Next Steps

If you’re interested in exploring additional examples of flows, we have a variety of recommendations in our examples repository. Here are four specific flow examples, each showcasing unique use cases to help you match your current problem type to a specific example:

  1. **Email Auto Responder Flow** : This example demonstrates an infinite loop where a background job continually runs to automate email responses. It’s a great use case for tasks that need to be performed repeatedly without manual intervention. [View Example](https://github.com/crewAIInc/crewAI-examples/tree/main/email_auto_responder_flow)
  2. **Lead Score Flow** : This flow showcases adding human-in-the-loop feedback and handling different conditional branches using the router. It’s an excellent example of how to incorporate dynamic decision-making and human oversight into your workflows. [View Example](https://github.com/crewAIInc/crewAI-examples/tree/main/lead-score-flow)
  3. **Write a Book Flow** : This example excels at chaining multiple crews together, where the output of one crew is used by another. Specifically, one crew outlines an entire book, and another crew generates chapters based on the outline. Eventually, everything is connected to produce a complete book. This flow is perfect for complex, multi-step processes that require coordination between different tasks. [View Example](https://github.com/crewAIInc/crewAI-examples/tree/main/write_a_book_with_flows)
  4. **Meeting Assistant Flow** : This flow demonstrates how to broadcast one event to trigger multiple follow-up actions. For instance, after a meeting is completed, the flow can update a Trello board, send a Slack message, and save the results. It’s a great example of handling multiple outcomes from a single event, making it ideal for comprehensive task management and notification systems. [View Example](https://github.com/crewAIInc/crewAI-examples/tree/main/meeting_assistant_flow)

By exploring these examples, you can gain insights into how to leverage CrewAI Flows for various use cases, from automating repetitive tasks to managing complex, multi-step processes with dynamic decision-making and human feedback. Also, check out our YouTube video on how to use flows in CrewAI below!

## 

​

Running Flows

There are two ways to run a flow:

### 

​

Using the Flow API

You can run a flow programmatically by creating an instance of your flow class and calling the `kickoff()` method:

Copy

Ask AI
    
    
    flow = ExampleFlow()
    result = flow.kickoff()
    

### 

​

Streaming Flow Execution

For real-time visibility into flow execution, you can enable streaming to receive output as it’s generated:

Copy

Ask AI
    
    
    class StreamingFlow(Flow):
        stream = True  # Enable streaming
    
        @start()
        def research(self):
            # Your flow implementation
            pass
    
    # Iterate over streaming output
    flow = StreamingFlow()
    streaming = flow.kickoff()
    for chunk in streaming:
        print(chunk.content, end="", flush=True)
    
    # Access final result
    result = streaming.result
    

Learn more about streaming in the [Streaming Flow Execution](/en/learn/streaming-flow-execution) guide.

### 

​

Using the CLI

Starting from version 0.103.0, you can run flows using the `crewai run` command:

Copy

Ask AI
    
    
    crewai run
    

This command automatically detects if your project is a flow (based on the `type = "flow"` setting in your pyproject.toml) and runs it accordingly. This is the recommended way to run flows from the command line. For backward compatibility, you can also use:

Copy

Ask AI
    
    
    crewai flow kickoff
    

However, the `crewai run` command is now the preferred method as it works for both crews and flows.

Was this page helpful?

YesNo

[CrewsPrevious](/en/concepts/crews)[KnowledgeNext](/en/concepts/knowledge)

Ctrl+I

[website](https://crewai.com)[x](https://x.com/crewAIInc)[github](https://github.com/crewAIInc/crewAI)[linkedin](https://www.linkedin.com/company/crewai-inc)[youtube](https://youtube.com/@crewAIInc)[reddit](https://www.reddit.com/r/crewAIInc/)

[Powered by Mintlify](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=crewai)

Assistant

Responses are generated using AI and may contain mistakes.

![Flow Visual image](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-1.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3d87938c680e7aa201798075fe19dcf8)

![Flow Visual image](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=245303e4f6e5bc30819aa9357561e7b3)

![Flow Visual image](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=245303e4f6e5bc30819aa9357561e7b3)

![Flow Visual image](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f41cbc9a268ba4bbb466fa2e2a1c2c1e)

![Flow Visual image](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-3.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f41cbc9a268ba4bbb466fa2e2a1c2c1e)

![Flow Visual image](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-4.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=260fcd89a5b3a6a42a25dd4f41e7c5c6)

![Flow Visual image](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-5.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=07cbcc6de6e8c8ae5da6c02a6fe4b457)

![Flow Visual image](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-6.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=78e66eabae15099e2ef1d0c314d3cb04)

![Flow Visual image](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-7.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=740f254bb03d60cd011911dab702ca77)

![Flow Visual image](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-8.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=994b487041be812c1df343b23b5da9f2)


---

# Source: https://docs.crewai.com/en/concepts/knowledge

Skip to main content

[CrewAI home page![light logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)![dark logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)](/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl K

Search...

Navigation

Core Concepts

Knowledge

[Home](/)[Documentation](/en/introduction)[AOP](/en/enterprise/introduction)[API Reference](/en/api-reference/introduction)[Examples](/en/examples/example)[Changelog](/en/changelog)

  * [Website](https://crewai.com)
  * [Forum](https://community.crewai.com)
  * [Blog](https://blog.crewai.com)
  * [CrewGPT](https://chatgpt.com/g/g-qqTuUWsBY-crewai-assistant)



##### Get Started

  * [Introduction](/en/introduction)
  * [Installation](/en/installation)
  * [Quickstart](/en/quickstart)



##### Guides

  * Strategy

  * Agents

  * Crews

  * Flows

  * Advanced




##### Core Concepts

  * [Agents](/en/concepts/agents)
  * [Tasks](/en/concepts/tasks)
  * [Crews](/en/concepts/crews)
  * [Flows](/en/concepts/flows)
  * [Knowledge](/en/concepts/knowledge)
  * [LLMs](/en/concepts/llms)
  * [Processes](/en/concepts/processes)
  * [Collaboration](/en/concepts/collaboration)
  * [Training](/en/concepts/training)
  * [Memory](/en/concepts/memory)
  * [Reasoning](/en/concepts/reasoning)
  * [Planning](/en/concepts/planning)
  * [Testing](/en/concepts/testing)
  * [CLI](/en/concepts/cli)
  * [Tools](/en/concepts/tools)
  * [Event Listeners](/en/concepts/event-listener)



##### MCP Integration

  * [MCP Servers as Tools in CrewAI](/en/mcp/overview)
  * [MCP DSL Integration](/en/mcp/dsl-integration)
  * [Stdio Transport](/en/mcp/stdio)
  * [SSE Transport](/en/mcp/sse)
  * [Streamable HTTP Transport](/en/mcp/streamable-http)
  * [Connecting to Multiple MCP Servers](/en/mcp/multiple-servers)
  * [MCP Security Considerations](/en/mcp/security)



##### Tools

  * [Tools Overview](/en/tools/overview)
  * File & Document

  * Web Scraping & Browsing

  * Search & Research

  * Database & Data

  * AI & Machine Learning

  * Cloud & Storage

  * Integrations

  * Automation




##### Observability

  * [CrewAI Tracing](/en/observability/tracing)
  * [Overview](/en/observability/overview)
  * [Arize Phoenix](/en/observability/arize-phoenix)
  * [Braintrust](/en/observability/braintrust)
  * [Datadog Integration](/en/observability/datadog)
  * [LangDB Integration](/en/observability/langdb)
  * [Langfuse Integration](/en/observability/langfuse)
  * [Langtrace Integration](/en/observability/langtrace)
  * [Maxim Integration](/en/observability/maxim)
  * [MLflow Integration](/en/observability/mlflow)
  * [Neatlogs Integration](/en/observability/neatlogs)
  * [OpenLIT Integration](/en/observability/openlit)
  * [Opik Integration](/en/observability/opik)
  * [Patronus AI Evaluation](/en/observability/patronus-evaluation)
  * [Portkey Integration](/en/observability/portkey)
  * [Weave Integration](/en/observability/weave)
  * [TrueFoundry Integration](/en/observability/truefoundry)



##### Learn

  * [Overview](/en/learn/overview)
  * [Strategic LLM Selection Guide](/en/learn/llm-selection-guide)
  * [Conditional Tasks](/en/learn/conditional-tasks)
  * [Coding Agents](/en/learn/coding-agents)
  * [Create Custom Tools](/en/learn/create-custom-tools)
  * [Custom LLM Implementation](/en/learn/custom-llm)
  * [Custom Manager Agent](/en/learn/custom-manager-agent)
  * [Customize Agents](/en/learn/customizing-agents)
  * [Image Generation with DALL-E](/en/learn/dalle-image-generation)
  * [Force Tool Output as Result](/en/learn/force-tool-output-as-result)
  * [Hierarchical Process](/en/learn/hierarchical-process)
  * [Human Input on Execution](/en/learn/human-input-on-execution)
  * [Human-in-the-Loop (HITL) Workflows](/en/learn/human-in-the-loop)
  * [Kickoff Crew Asynchronously](/en/learn/kickoff-async)
  * [Kickoff Crew for Each](/en/learn/kickoff-for-each)
  * [Connect to any LLM](/en/learn/llm-connections)
  * [Using Multimodal Agents](/en/learn/multimodal-agents)
  * [Replay Tasks from Latest Crew Kickoff](/en/learn/replay-tasks-from-latest-crew-kickoff)
  * [Sequential Processes](/en/learn/sequential-process)
  * [Using Annotations in crew.py](/en/learn/using-annotations)
  * [Execution Hooks Overview](/en/learn/execution-hooks)
  * [LLM Call Hooks](/en/learn/llm-hooks)
  * [Tool Call Hooks](/en/learn/tool-hooks)



##### Telemetry

  * [Telemetry](/en/telemetry)



Core Concepts

# Knowledge

Copy page

What is knowledge in CrewAI and how to use it.

Copy page

## 

​

Overview

Knowledge in CrewAI is a powerful system that allows AI agents to access and utilize external information sources during their tasks. Think of it as giving your agents a reference library they can consult while working.

Key benefits of using Knowledge:

  * Enhance agents with domain-specific information
  * Support decisions with real-world data
  * Maintain context across conversations
  * Ground responses in factual information



## 

​

Quickstart Examples

For file-based Knowledge Sources, make sure to place your files in a `knowledge` directory at the root of your project. Also, use relative paths from the `knowledge` directory when creating the source.

### 

​

Vector store (RAG) client configuration

CrewAI exposes a provider-neutral RAG client abstraction for vector stores. The default provider is ChromaDB, and Qdrant is supported as well. You can switch providers using configuration utilities. Supported today:

  * ChromaDB (default)
  * Qdrant



Code

Copy

Ask AI
    
    
    from crewai.rag.config.utils import set_rag_config, get_rag_client, clear_rag_config
    
    # ChromaDB (default)
    from crewai.rag.chromadb.config import ChromaDBConfig
    set_rag_config(ChromaDBConfig())
    chromadb_client = get_rag_client()
    
    # Qdrant
    from crewai.rag.qdrant.config import QdrantConfig
    set_rag_config(QdrantConfig())
    qdrant_client = get_rag_client()
    
    # Example operations (same API for any provider)
    client = qdrant_client  # or chromadb_client
    client.create_collection(collection_name="docs")
    client.add_documents(
        collection_name="docs",
        documents=[{"id": "1", "content": "CrewAI enables collaborative AI agents."}],
    )
    results = client.search(collection_name="docs", query="collaborative agents", limit=3)
    
    clear_rag_config()  # optional reset
    

This RAG client is separate from Knowledge’s built-in storage. Use it when you need direct vector-store control or custom retrieval pipelines.

### 

​

Basic String Knowledge Example

Code

Copy

Ask AI
    
    
    from crewai import Agent, Task, Crew, Process, LLM
    from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource
    
    # Create a knowledge source
    content = "Users name is John. He is 30 years old and lives in San Francisco."
    string_source = StringKnowledgeSource(content=content)
    
    # Create an LLM with a temperature of 0 to ensure deterministic outputs
    llm = LLM(model="gpt-4o-mini", temperature=0)
    
    # Create an agent with the knowledge store
    agent = Agent(
        role="About User",
        goal="You know everything about the user.",
        backstory="You are a master at understanding people and their preferences.",
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )
    
    task = Task(
        description="Answer the following questions about the user: {question}",
        expected_output="An answer to the question.",
        agent=agent,
    )
    
    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True,
        process=Process.sequential,
        knowledge_sources=[string_source], # Enable knowledge by adding the sources here
    )
    
    result = crew.kickoff(inputs={"question": "What city does John live in and how old is he?"})
    

### 

​

Web Content Knowledge Example

You need to install `docling` for the following example to work: `uv add docling`

Code

Copy

Ask AI
    
    
    from crewai import LLM, Agent, Crew, Process, Task
    from crewai.knowledge.source.crew_docling_source import CrewDoclingSource
    
    # Create a knowledge source from web content
    content_source = CrewDoclingSource(
        file_paths=[
            "https://lilianweng.github.io/posts/2024-11-28-reward-hacking",
            "https://lilianweng.github.io/posts/2024-07-07-hallucination",
        ],
    )
    
    # Create an LLM with a temperature of 0 to ensure deterministic outputs
    llm = LLM(model="gpt-4o-mini", temperature=0)
    
    # Create an agent with the knowledge store
    agent = Agent(
        role="About papers",
        goal="You know everything about the papers.",
        backstory="You are a master at understanding papers and their content.",
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )
    
    task = Task(
        description="Answer the following questions about the papers: {question}",
        expected_output="An answer to the question.",
        agent=agent,
    )
    
    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True,
        process=Process.sequential,
        knowledge_sources=[content_source],
    )
    
    result = crew.kickoff(
        inputs={"question": "What is the reward hacking paper about? Be sure to provide sources."}
    )
    

## 

​

Supported Knowledge Sources

CrewAI supports various types of knowledge sources out of the box:

## Text Sources

  * Raw strings
  * Text files (.txt)
  * PDF documents



## Structured Data

  * CSV files
  * Excel spreadsheets
  * JSON documents



### 

​

Text File Knowledge Source

Copy

Ask AI
    
    
    from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
    
    text_source = TextFileKnowledgeSource(
        file_paths=["document.txt", "another.txt"]
    )
    

### 

​

PDF Knowledge Source

Copy

Ask AI
    
    
    from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource
    
    pdf_source = PDFKnowledgeSource(
        file_paths=["document.pdf", "another.pdf"]
    )
    

### 

​

CSV Knowledge Source

Copy

Ask AI
    
    
    from crewai.knowledge.source.csv_knowledge_source import CSVKnowledgeSource
    
    csv_source = CSVKnowledgeSource(
        file_paths=["data.csv"]
    )
    

### 

​

Excel Knowledge Source

Copy

Ask AI
    
    
    from crewai.knowledge.source.excel_knowledge_source import ExcelKnowledgeSource
    
    excel_source = ExcelKnowledgeSource(
        file_paths=["spreadsheet.xlsx"]
    )
    

### 

​

JSON Knowledge Source

Copy

Ask AI
    
    
    from crewai.knowledge.source.json_knowledge_source import JSONKnowledgeSource
    
    json_source = JSONKnowledgeSource(
        file_paths=["data.json"]
    )
    

Please ensure that you create the ./knowledge folder. All source files (e.g., .txt, .pdf, .xlsx, .json) should be placed in this folder for centralized management.

## 

​

Agent vs Crew Knowledge: Complete Guide

**Understanding Knowledge Levels** : CrewAI supports knowledge at both agent and crew levels. This section clarifies exactly how each works, when they’re initialized, and addresses common misconceptions about dependencies.

### 

​

How Knowledge Initialization Actually Works

Here’s exactly what happens when you use knowledge:

#### 

​

Agent-Level Knowledge (Independent)

Copy

Ask AI
    
    
    from crewai import Agent, Task, Crew
    from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource
    
    # Agent with its own knowledge - NO crew knowledge needed
    specialist_knowledge = StringKnowledgeSource(
        content="Specialized technical information for this agent only"
    )
    
    specialist_agent = Agent(
        role="Technical Specialist",
        goal="Provide technical expertise",
        backstory="Expert in specialized technical domains",
        knowledge_sources=[specialist_knowledge]  # Agent-specific knowledge
    )
    
    task = Task(
        description="Answer technical questions",
        agent=specialist_agent,
        expected_output="Technical answer"
    )
    
    # No crew-level knowledge required
    crew = Crew(
        agents=[specialist_agent],
        tasks=[task]
    )
    
    result = crew.kickoff()  # Agent knowledge works independently
    

#### 

​

What Happens During `crew.kickoff()`

When you call `crew.kickoff()`, here’s the exact sequence:

Copy

Ask AI
    
    
    # During kickoff
    for agent in self.agents:
        agent.crew = self  # Agent gets reference to crew
        agent.set_knowledge(crew_embedder=self.embedder)  # Agent knowledge initialized
        agent.create_agent_executor()
    

#### 

​

Storage Independence

Each knowledge level uses independent storage collections:

Copy

Ask AI
    
    
    # Agent knowledge storage
    agent_collection_name = agent.role  # e.g., "Technical Specialist"
    
    # Crew knowledge storage  
    crew_collection_name = "crew"
    
    # Both stored in same ChromaDB instance but different collections
    # Path: ~/.local/share/CrewAI/{project}/knowledge/
    #   ├── crew/                    # Crew knowledge collection
    #   ├── Technical Specialist/    # Agent knowledge collection
    #   └── Another Agent Role/      # Another agent's collection
    

### 

​

Complete Working Examples

#### 

​

Example 1: Agent-Only Knowledge

Copy

Ask AI
    
    
    from crewai import Agent, Task, Crew
    from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource
    
    # Agent-specific knowledge
    agent_knowledge = StringKnowledgeSource(
        content="Agent-specific information that only this agent needs"
    )
    
    agent = Agent(
        role="Specialist",
        goal="Use specialized knowledge",
        backstory="Expert with specific knowledge",
        knowledge_sources=[agent_knowledge],
        embedder={  # Agent can have its own embedder
            "provider": "openai",
            "config": {"model": "text-embedding-3-small"}
        }
    )
    
    task = Task(
        description="Answer using your specialized knowledge",
        agent=agent,
        expected_output="Answer based on agent knowledge"
    )
    
    # No crew knowledge needed
    crew = Crew(agents=[agent], tasks=[task])
    result = crew.kickoff()  # Works perfectly
    

#### 

​

Example 2: Both Agent and Crew Knowledge

Copy

Ask AI
    
    
    # Crew-wide knowledge (shared by all agents)
    crew_knowledge = StringKnowledgeSource(
        content="Company policies and general information for all agents"
    )
    
    # Agent-specific knowledge
    specialist_knowledge = StringKnowledgeSource(
        content="Technical specifications only the specialist needs"
    )
    
    specialist = Agent(
        role="Technical Specialist",
        goal="Provide technical expertise",
        backstory="Technical expert",
        knowledge_sources=[specialist_knowledge]  # Agent-specific
    )
    
    generalist = Agent(
        role="General Assistant", 
        goal="Provide general assistance",
        backstory="General helper"
        # No agent-specific knowledge
    )
    
    crew = Crew(
        agents=[specialist, generalist],
        tasks=[...],
        knowledge_sources=[crew_knowledge]  # Crew-wide knowledge
    )
    
    # Result:
    # - specialist gets: crew_knowledge + specialist_knowledge
    # - generalist gets: crew_knowledge only
    

#### 

​

Example 3: Multiple Agents with Different Knowledge

Copy

Ask AI
    
    
    # Different knowledge for different agents
    sales_knowledge = StringKnowledgeSource(content="Sales procedures and pricing")
    tech_knowledge = StringKnowledgeSource(content="Technical documentation")
    support_knowledge = StringKnowledgeSource(content="Support procedures")
    
    sales_agent = Agent(
        role="Sales Representative",
        knowledge_sources=[sales_knowledge],
        embedder={"provider": "openai", "config": {"model": "text-embedding-3-small"}}
    )
    
    tech_agent = Agent(
        role="Technical Expert", 
        knowledge_sources=[tech_knowledge],
        embedder={"provider": "ollama", "config": {"model": "mxbai-embed-large"}}
    )
    
    support_agent = Agent(
        role="Support Specialist",
        knowledge_sources=[support_knowledge]
        # Will use crew embedder as fallback
    )
    
    crew = Crew(
        agents=[sales_agent, tech_agent, support_agent],
        tasks=[...],
        embedder={  # Fallback embedder for agents without their own
            "provider": "google-generativeai",
            "config": {"model_name": "gemini-embedding-001"}
        }
    )
    
    # Each agent gets only their specific knowledge
    # Each can use different embedding providers
    

Unlike retrieval from a vector database using a tool, agents preloaded with knowledge will not need a retrieval persona or task. Simply add the relevant knowledge sources your agent or crew needs to function.Knowledge sources can be added at the agent or crew level. Crew level knowledge sources will be used by **all agents** in the crew. Agent level knowledge sources will be used by the **specific agent** that is preloaded with the knowledge.

## 

​

Knowledge Configuration

You can configure the knowledge configuration for the crew or agent.

Code

Copy

Ask AI
    
    
    from crewai.knowledge.knowledge_config import KnowledgeConfig
    
    knowledge_config = KnowledgeConfig(results_limit=10, score_threshold=0.5)
    
    agent = Agent(
        ...
        knowledge_config=knowledge_config
    )
    

`results_limit`: is the number of relevant documents to return. Default is 3. `score_threshold`: is the minimum score for a document to be considered relevant. Default is 0.35.

## 

​

Supported Knowledge Parameters

​

sources

List[BaseKnowledgeSource]

required

List of knowledge sources that provide content to be stored and queried. Can include PDF, CSV, Excel, JSON, text files, or string content.

​

collection_name

str

Name of the collection where the knowledge will be stored. Used to identify different sets of knowledge. Defaults to “knowledge” if not provided.

​

storage

Optional[KnowledgeStorage]

Custom storage configuration for managing how the knowledge is stored and retrieved. If not provided, a default storage will be created.

## 

​

Knowledge Storage Transparency

**Understanding Knowledge Storage** : CrewAI automatically stores knowledge sources in platform-specific directories using ChromaDB for vector storage. Understanding these locations and defaults helps with production deployments, debugging, and storage management.

### 

​

Where CrewAI Stores Knowledge Files

By default, CrewAI uses the same storage system as memory, storing knowledge in platform-specific directories:

#### 

​

Default Storage Locations by Platform

**macOS:**

Copy

Ask AI
    
    
    ~/Library/Application Support/CrewAI/{project_name}/
    └── knowledge/                    # Knowledge ChromaDB files
        ├── chroma.sqlite3           # ChromaDB metadata
        ├── {collection_id}/         # Vector embeddings
        └── knowledge_{collection}/  # Named collections
    

**Linux:**

Copy

Ask AI
    
    
    ~/.local/share/CrewAI/{project_name}/
    └── knowledge/
        ├── chroma.sqlite3
        ├── {collection_id}/
        └── knowledge_{collection}/
    

**Windows:**

Copy

Ask AI
    
    
    C:\Users\{username}\AppData\Local\CrewAI\{project_name}\
    └── knowledge\
        ├── chroma.sqlite3
        ├── {collection_id}\
        └── knowledge_{collection}\
    

### 

​

Finding Your Knowledge Storage Location

To see exactly where CrewAI is storing your knowledge files:

Copy

Ask AI
    
    
    from crewai.utilities.paths import db_storage_path
    import os
    
    # Get the knowledge storage path
    knowledge_path = os.path.join(db_storage_path(), "knowledge")
    print(f"Knowledge storage location: {knowledge_path}")
    
    # List knowledge collections and files
    if os.path.exists(knowledge_path):
        print("\nKnowledge storage contents:")
        for item in os.listdir(knowledge_path):
            item_path = os.path.join(knowledge_path, item)
            if os.path.isdir(item_path):
                print(f"📁 Collection: {item}/")
                # Show collection contents
                try:
                    for subitem in os.listdir(item_path):
                        print(f"   └── {subitem}")
                except PermissionError:
                    print(f"   └── (permission denied)")
            else:
                print(f"📄 {item}")
    else:
        print("No knowledge storage found yet.")
    

### 

​

Controlling Knowledge Storage Locations

#### 

​

Option 1: Environment Variable (Recommended)

Copy

Ask AI
    
    
    import os
    from crewai import Crew
    
    # Set custom storage location for all CrewAI data
    os.environ["CREWAI_STORAGE_DIR"] = "./my_project_storage"
    
    # All knowledge will now be stored in ./my_project_storage/knowledge/
    crew = Crew(
        agents=[...],
        tasks=[...],
        knowledge_sources=[...]
    )
    

#### 

​

Option 2: Custom Knowledge Storage

Copy

Ask AI
    
    
    from crewai.knowledge.storage.knowledge_storage import KnowledgeStorage
    from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource
    
    # Create custom storage with specific embedder
    custom_storage = KnowledgeStorage(
        embedder={
            "provider": "ollama",
            "config": {"model": "mxbai-embed-large"}
        },
        collection_name="my_custom_knowledge"
    )
    
    # Use with knowledge sources
    knowledge_source = StringKnowledgeSource(
        content="Your knowledge content here"
    )
    knowledge_source.storage = custom_storage
    

#### 

​

Option 3: Project-Specific Knowledge Storage

Copy

Ask AI
    
    
    import os
    from pathlib import Path
    
    # Store knowledge in project directory
    project_root = Path(__file__).parent
    knowledge_dir = project_root / "knowledge_storage"
    
    os.environ["CREWAI_STORAGE_DIR"] = str(knowledge_dir)
    
    # Now all knowledge will be stored in your project directory
    

### 

​

Default Embedding Provider Behavior

**Default Embedding Provider** : CrewAI defaults to OpenAI embeddings (`text-embedding-3-small`) for knowledge storage, even when using different LLM providers. You can easily customize this to match your setup.

#### 

​

Understanding Default Behavior

Copy

Ask AI
    
    
    from crewai import Agent, Crew, LLM
    from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource
    
    # When using Claude as your LLM...
    agent = Agent(
        role="Researcher",
        goal="Research topics",
        backstory="Expert researcher",
        llm=LLM(provider="anthropic", model="claude-3-sonnet")  # Using Claude
    )
    
    # CrewAI will still use OpenAI embeddings by default for knowledge
    # This ensures consistency but may not match your LLM provider preference
    knowledge_source = StringKnowledgeSource(content="Research data...")
    
    crew = Crew(
        agents=[agent],
        tasks=[...],
        knowledge_sources=[knowledge_source]
        # Default: Uses OpenAI embeddings even with Claude LLM
    )
    

#### 

​

Customizing Knowledge Embedding Providers

Copy

Ask AI
    
    
    # Option 1: Use Voyage AI (recommended by Anthropic for Claude users)
    crew = Crew(
        agents=[agent],
        tasks=[...],
        knowledge_sources=[knowledge_source],
        embedder={
            "provider": "voyageai",  # Recommended for Claude users
            "config": {
                "api_key": "your-voyage-api-key",
                "model": "voyage-3"  # or "voyage-3-large" for best quality
            }
        }
    )
    
    # Option 2: Use local embeddings (no external API calls)
    crew = Crew(
        agents=[agent],
        tasks=[...],
        knowledge_sources=[knowledge_source],
        embedder={
            "provider": "ollama",
            "config": {
                "model": "mxbai-embed-large",
                "url": "http://localhost:11434/api/embeddings"
            }
        }
    )
    
    # Option 3: Agent-level embedding customization
    agent = Agent(
        role="Researcher",
        goal="Research topics",
        backstory="Expert researcher",
        knowledge_sources=[knowledge_source],
        embedder={
            "provider": "google-generativeai",
            "config": {
                "model_name": "gemini-embedding-001",
                "api_key": "your-google-key"
            }
        }
    )
    

#### 

​

Configuring Azure OpenAI Embeddings

When using Azure OpenAI embeddings:

  1. Make sure you deploy the embedding model in Azure platform first
  2. Then you need to use the following configuration:



Copy

Ask AI
    
    
    agent = Agent(
        role="Researcher",
        goal="Research topics",
        backstory="Expert researcher",
        knowledge_sources=[knowledge_source],
        embedder={
            "provider": "azure",
            "config": {
                "api_key": "your-azure-api-key",
                "model": "text-embedding-ada-002", # change to the model you are using and is deployed in Azure
                "api_base": "https://your-azure-endpoint.openai.azure.com/",
                "api_version": "2024-02-01"
            }
        }
    )
    

## 

​

Advanced Features

### 

​

Query Rewriting

CrewAI implements an intelligent query rewriting mechanism to optimize knowledge retrieval. When an agent needs to search through knowledge sources, the raw task prompt is automatically transformed into a more effective search query.

#### 

​

How Query Rewriting Works

  1. When an agent executes a task with knowledge sources available, the `_get_knowledge_search_query` method is triggered
  2. The agent’s LLM is used to transform the original task prompt into an optimized search query
  3. This optimized query is then used to retrieve relevant information from knowledge sources



#### 

​

Benefits of Query Rewriting

## Improved Retrieval Accuracy

By focusing on key concepts and removing irrelevant content, query rewriting helps retrieve more relevant information.

## Context Awareness

The rewritten queries are designed to be more specific and context-aware for vector database retrieval.

#### 

​

Example

Copy

Ask AI
    
    
    # Original task prompt
    task_prompt = "Answer the following questions about the user's favorite movies: What movie did John watch last week? Format your answer in JSON."
    
    # Behind the scenes, this might be rewritten as:
    rewritten_query = "What movies did John watch last week?"
    

The rewritten query is more focused on the core information need and removes irrelevant instructions about output formatting.

This mechanism is fully automatic and requires no configuration from users. The agent’s LLM is used to perform the query rewriting, so using a more capable LLM can improve the quality of rewritten queries.

### 

​

Knowledge Events

CrewAI emits events during the knowledge retrieval process that you can listen for using the event system. These events allow you to monitor, debug, and analyze how knowledge is being retrieved and used by your agents.

#### 

​

Available Knowledge Events

  * **KnowledgeRetrievalStartedEvent** : Emitted when an agent starts retrieving knowledge from sources
  * **KnowledgeRetrievalCompletedEvent** : Emitted when knowledge retrieval is completed, including the query used and the retrieved content
  * **KnowledgeQueryStartedEvent** : Emitted when a query to knowledge sources begins
  * **KnowledgeQueryCompletedEvent** : Emitted when a query completes successfully
  * **KnowledgeQueryFailedEvent** : Emitted when a query to knowledge sources fails
  * **KnowledgeSearchQueryFailedEvent** : Emitted when a search query fails



#### 

​

Example: Monitoring Knowledge Retrieval

Copy

Ask AI
    
    
    from crewai.events import (
        KnowledgeRetrievalStartedEvent,
        KnowledgeRetrievalCompletedEvent,
        BaseEventListener,
    )
    
    class KnowledgeMonitorListener(BaseEventListener):
        def setup_listeners(self, crewai_event_bus):
            @crewai_event_bus.on(KnowledgeRetrievalStartedEvent)
            def on_knowledge_retrieval_started(source, event):
                print(f"Agent '{event.agent.role}' started retrieving knowledge")
                
            @crewai_event_bus.on(KnowledgeRetrievalCompletedEvent)
            def on_knowledge_retrieval_completed(source, event):
                print(f"Agent '{event.agent.role}' completed knowledge retrieval")
                print(f"Query: {event.query}")
                print(f"Retrieved {len(event.retrieved_knowledge)} knowledge chunks")
    
    # Create an instance of your listener
    knowledge_monitor = KnowledgeMonitorListener()
    

For more information on using events, see the [Event Listeners](/en/concepts/event-listener) documentation.

### 

​

Custom Knowledge Sources

CrewAI allows you to create custom knowledge sources for any type of data by extending the `BaseKnowledgeSource` class. Let’s create a practical example that fetches and processes space news articles.

#### 

​

Space News Knowledge Source Example

Code

Output

Copy

Ask AI
    
    
    from crewai import Agent, Task, Crew, Process, LLM
    from crewai.knowledge.source.base_knowledge_source import BaseKnowledgeSource
    import requests
    from datetime import datetime
    from typing import Dict, Any
    from pydantic import BaseModel, Field
    
    class SpaceNewsKnowledgeSource(BaseKnowledgeSource):
        """Knowledge source that fetches data from Space News API."""
    
        api_endpoint: str = Field(description="API endpoint URL")
        limit: int = Field(default=10, description="Number of articles to fetch")
    
        def load_content(self) -> Dict[Any, str]:
            """Fetch and format space news articles."""
            try:
                response = requests.get(
                    f"{self.api_endpoint}?limit={self.limit}"
                )
                response.raise_for_status()
    
                data = response.json()
                articles = data.get('results', [])
    
                formatted_data = self.validate_content(articles)
                return {self.api_endpoint: formatted_data}
            except Exception as e:
                raise ValueError(f"Failed to fetch space news: {str(e)}")
    
        def validate_content(self, articles: list) -> str:
            """Format articles into readable text."""
            formatted = "Space News Articles:\n\n"
            for article in articles:
                formatted += f"""
                    Title: {article['title']}
                    Published: {article['published_at']}
                    Summary: {article['summary']}
                    News Site: {article['news_site']}
                    URL: {article['url']}
                    -------------------"""
            return formatted
    
        def add(self) -> None:
            """Process and store the articles."""
            content = self.load_content()
            for _, text in content.items():
                chunks = self._chunk_text(text)
                self.chunks.extend(chunks)
    
            self._save_documents()
    
    # Create knowledge source
    recent_news = SpaceNewsKnowledgeSource(
        api_endpoint="https://api.spaceflightnewsapi.net/v4/articles",
        limit=10,
    )
    
    # Create specialized agent
    space_analyst = Agent(
        role="Space News Analyst",
        goal="Answer questions about space news accurately and comprehensively",
        backstory="""You are a space industry analyst with expertise in space exploration,
        satellite technology, and space industry trends. You excel at answering questions
        about space news and providing detailed, accurate information.""",
        knowledge_sources=[recent_news],
        llm=LLM(model="gpt-4", temperature=0.0)
    )
    
    # Create task that handles user questions
    analysis_task = Task(
        description="Answer this question about space news: {user_question}",
        expected_output="A detailed answer based on the recent space news articles",
        agent=space_analyst
    )
    
    # Create and run the crew
    crew = Crew(
        agents=[space_analyst],
        tasks=[analysis_task],
        verbose=True,
        process=Process.sequential
    )
    
    # Example usage
    result = crew.kickoff(
        inputs={"user_question": "What are the latest developments in space exploration?"}
    )
    

## 

​

Debugging and Troubleshooting

### 

​

Debugging Knowledge Issues

#### 

​

Check Agent Knowledge Initialization

Copy

Ask AI
    
    
    from crewai import Agent, Crew, Task
    from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource
    
    knowledge_source = StringKnowledgeSource(content="Test knowledge")
    
    agent = Agent(
        role="Test Agent",
        goal="Test knowledge",
        backstory="Testing",
        knowledge_sources=[knowledge_source]
    )
    
    crew = Crew(agents=[agent], tasks=[Task(...)])
    
    # Before kickoff - knowledge not initialized
    print(f"Before kickoff - Agent knowledge: {getattr(agent, 'knowledge', None)}")
    
    crew.kickoff()
    
    # After kickoff - knowledge initialized
    print(f"After kickoff - Agent knowledge: {agent.knowledge}")
    print(f"Agent knowledge collection: {agent.knowledge.storage.collection_name}")
    print(f"Number of sources: {len(agent.knowledge.sources)}")
    

#### 

​

Verify Knowledge Storage Locations

Copy

Ask AI
    
    
    import os
    from crewai.utilities.paths import db_storage_path
    
    # Check storage structure
    storage_path = db_storage_path()
    knowledge_path = os.path.join(storage_path, "knowledge")
    
    if os.path.exists(knowledge_path):
        print("Knowledge collections found:")
        for collection in os.listdir(knowledge_path):
            collection_path = os.path.join(knowledge_path, collection)
            if os.path.isdir(collection_path):
                print(f"  - {collection}/")
                # Show collection contents
                for item in os.listdir(collection_path):
                    print(f"    └── {item}")
    

#### 

​

Test Knowledge Retrieval

Copy

Ask AI
    
    
    # Test agent knowledge retrieval
    if hasattr(agent, 'knowledge') and agent.knowledge:
        test_query = ["test query"]
        results = agent.knowledge.query(test_query)
        print(f"Agent knowledge results: {len(results)} documents found")
        
        # Test crew knowledge retrieval (if exists)
        if hasattr(crew, 'knowledge') and crew.knowledge:
            crew_results = crew.query_knowledge(test_query)
            print(f"Crew knowledge results: {len(crew_results)} documents found")
    

#### 

​

Inspect Knowledge Collections

Copy

Ask AI
    
    
    import chromadb
    from crewai.utilities.paths import db_storage_path
    import os
    
    # Connect to CrewAI's knowledge ChromaDB
    knowledge_path = os.path.join(db_storage_path(), "knowledge")
    
    if os.path.exists(knowledge_path):
        client = chromadb.PersistentClient(path=knowledge_path)
        collections = client.list_collections()
        
        print("Knowledge Collections:")
        for collection in collections:
            print(f"  - {collection.name}: {collection.count()} documents")
            
            # Sample a few documents to verify content
            if collection.count() > 0:
                sample = collection.peek(limit=2)
                print(f"    Sample content: {sample['documents'][0][:100]}...")
    else:
        print("No knowledge storage found")
    

#### 

​

Check Knowledge Processing

Copy

Ask AI
    
    
    from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource
    
    # Create a test knowledge source
    test_source = StringKnowledgeSource(
        content="Test knowledge content for debugging",
        chunk_size=100,  # Small chunks for testing
        chunk_overlap=20
    )
    
    # Check chunking behavior
    print(f"Original content length: {len(test_source.content)}")
    print(f"Chunk size: {test_source.chunk_size}")
    print(f"Chunk overlap: {test_source.chunk_overlap}")
    
    # Process and inspect chunks
    test_source.add()
    print(f"Number of chunks created: {len(test_source.chunks)}")
    for i, chunk in enumerate(test_source.chunks[:3]):  # Show first 3 chunks
        print(f"Chunk {i+1}: {chunk[:50]}...")
    

### 

​

Common Knowledge Storage Issues

**“File not found” errors:**

Copy

Ask AI
    
    
    # Ensure files are in the correct location
    from crewai.utilities.constants import KNOWLEDGE_DIRECTORY
    import os
    
    knowledge_dir = KNOWLEDGE_DIRECTORY  # Usually "knowledge"
    file_path = os.path.join(knowledge_dir, "your_file.pdf")
    
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        print(f"Current working directory: {os.getcwd()}")
        print(f"Expected knowledge directory: {os.path.abspath(knowledge_dir)}")
    

**“Embedding dimension mismatch” errors:**

Copy

Ask AI
    
    
    # This happens when switching embedding providers
    # Reset knowledge storage to clear old embeddings
    crew.reset_memories(command_type='knowledge')
    
    # Or use consistent embedding providers
    crew = Crew(
        agents=[...],
        tasks=[...],
        knowledge_sources=[...],
        embedder={"provider": "openai", "config": {"model": "text-embedding-3-small"}}
    )
    

**“ChromaDB permission denied” errors:**

Copy

Ask AI
    
    
    # Fix storage permissions
    chmod -R 755 ~/.local/share/CrewAI/
    

**Knowledge not persisting between runs:**

Copy

Ask AI
    
    
    # Verify storage location consistency
    import os
    from crewai.utilities.paths import db_storage_path
    
    print("CREWAI_STORAGE_DIR:", os.getenv("CREWAI_STORAGE_DIR"))
    print("Computed storage path:", db_storage_path())
    print("Knowledge path:", os.path.join(db_storage_path(), "knowledge"))
    

### 

​

Knowledge Reset Commands

Copy

Ask AI
    
    
    # Reset only agent-specific knowledge
    crew.reset_memories(command_type='agent_knowledge')
    
    # Reset both crew and agent knowledge  
    crew.reset_memories(command_type='knowledge')
    
    # CLI commands
    # crewai reset-memories --agent-knowledge  # Agent knowledge only
    # crewai reset-memories --knowledge        # All knowledge
    

### 

​

Clearing Knowledge

If you need to clear the knowledge stored in CrewAI, you can use the `crewai reset-memories` command with the `--knowledge` option.

Command

Copy

Ask AI
    
    
    crewai reset-memories --knowledge
    

This is useful when you’ve updated your knowledge sources and want to ensure that the agents are using the most recent information.

## 

​

Best Practices

Content Organization

  * Keep chunk sizes appropriate for your content type
  * Consider content overlap for context preservation
  * Organize related information into separate knowledge sources



Performance Tips

  * Adjust chunk sizes based on content complexity
  * Configure appropriate embedding models
  * Consider using local embedding providers for faster processing



One Time Knowledge

  * With the typical file structure provided by CrewAI, knowledge sources are embedded every time the kickoff is triggered.
  * If the knowledge sources are large, this leads to inefficiency and increased latency, as the same data is embedded each time.
  * To resolve this, directly initialize the knowledge parameter instead of the knowledge_sources parameter.
  * Link to the issue to get complete idea [Github Issue](https://github.com/crewAIInc/crewAI/issues/2755)



Knowledge Management

  * Use agent-level knowledge for role-specific information
  * Use crew-level knowledge for shared information all agents need
  * Set embedders at agent level if you need different embedding strategies
  * Use consistent collection naming by keeping agent roles descriptive
  * Test knowledge initialization by checking agent.knowledge after kickoff
  * Monitor storage locations to understand where knowledge is stored
  * Reset knowledge appropriately using the correct command types



Production Best Practices

  * Set `CREWAI_STORAGE_DIR` to a known location in production
  * Choose explicit embedding providers to match your LLM setup and avoid API key conflicts
  * Monitor knowledge storage size as it grows with document additions
  * Organize knowledge sources by domain or purpose using collection names
  * Include knowledge directories in your backup and deployment strategies
  * Set appropriate file permissions for knowledge files and storage directories
  * Use environment variables for API keys and sensitive configuration



Was this page helpful?

YesNo

[FlowsPrevious](/en/concepts/flows)[LLMsNext](/en/concepts/llms)

Ctrl+I

[website](https://crewai.com)[x](https://x.com/crewAIInc)[github](https://github.com/crewAIInc/crewAI)[linkedin](https://www.linkedin.com/company/crewai-inc)[youtube](https://youtube.com/@crewAIInc)[reddit](https://www.reddit.com/r/crewAIInc/)

[Powered by Mintlify](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=crewai)

Assistant

Responses are generated using AI and may contain mistakes.


---

# Source: https://docs.crewai.com/en/guides/concepts/evaluating-use-cases

Skip to main content

[CrewAI home page![light logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)![dark logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)](/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl K

Search...

Navigation

Strategy

Evaluating Use Cases for CrewAI

[Home](/)[Documentation](/en/introduction)[AOP](/en/enterprise/introduction)[API Reference](/en/api-reference/introduction)[Examples](/en/examples/example)[Changelog](/en/changelog)

  * [Website](https://crewai.com)
  * [Forum](https://community.crewai.com)
  * [Blog](https://blog.crewai.com)
  * [CrewGPT](https://chatgpt.com/g/g-qqTuUWsBY-crewai-assistant)



##### Get Started

  * [Introduction](/en/introduction)
  * [Installation](/en/installation)
  * [Quickstart](/en/quickstart)



##### Guides

  * Strategy

    * [Evaluating Use Cases for CrewAI](/en/guides/concepts/evaluating-use-cases)
  * Agents

  * Crews

  * Flows

  * Advanced




##### Core Concepts

  * [Agents](/en/concepts/agents)
  * [Tasks](/en/concepts/tasks)
  * [Crews](/en/concepts/crews)
  * [Flows](/en/concepts/flows)
  * [Knowledge](/en/concepts/knowledge)
  * [LLMs](/en/concepts/llms)
  * [Processes](/en/concepts/processes)
  * [Collaboration](/en/concepts/collaboration)
  * [Training](/en/concepts/training)
  * [Memory](/en/concepts/memory)
  * [Reasoning](/en/concepts/reasoning)
  * [Planning](/en/concepts/planning)
  * [Testing](/en/concepts/testing)
  * [CLI](/en/concepts/cli)
  * [Tools](/en/concepts/tools)
  * [Event Listeners](/en/concepts/event-listener)



##### MCP Integration

  * [MCP Servers as Tools in CrewAI](/en/mcp/overview)
  * [MCP DSL Integration](/en/mcp/dsl-integration)
  * [Stdio Transport](/en/mcp/stdio)
  * [SSE Transport](/en/mcp/sse)
  * [Streamable HTTP Transport](/en/mcp/streamable-http)
  * [Connecting to Multiple MCP Servers](/en/mcp/multiple-servers)
  * [MCP Security Considerations](/en/mcp/security)



##### Tools

  * [Tools Overview](/en/tools/overview)
  * File & Document

  * Web Scraping & Browsing

  * Search & Research

  * Database & Data

  * AI & Machine Learning

  * Cloud & Storage

  * Integrations

  * Automation




##### Observability

  * [CrewAI Tracing](/en/observability/tracing)
  * [Overview](/en/observability/overview)
  * [Arize Phoenix](/en/observability/arize-phoenix)
  * [Braintrust](/en/observability/braintrust)
  * [Datadog Integration](/en/observability/datadog)
  * [LangDB Integration](/en/observability/langdb)
  * [Langfuse Integration](/en/observability/langfuse)
  * [Langtrace Integration](/en/observability/langtrace)
  * [Maxim Integration](/en/observability/maxim)
  * [MLflow Integration](/en/observability/mlflow)
  * [Neatlogs Integration](/en/observability/neatlogs)
  * [OpenLIT Integration](/en/observability/openlit)
  * [Opik Integration](/en/observability/opik)
  * [Patronus AI Evaluation](/en/observability/patronus-evaluation)
  * [Portkey Integration](/en/observability/portkey)
  * [Weave Integration](/en/observability/weave)
  * [TrueFoundry Integration](/en/observability/truefoundry)



##### Learn

  * [Overview](/en/learn/overview)
  * [Strategic LLM Selection Guide](/en/learn/llm-selection-guide)
  * [Conditional Tasks](/en/learn/conditional-tasks)
  * [Coding Agents](/en/learn/coding-agents)
  * [Create Custom Tools](/en/learn/create-custom-tools)
  * [Custom LLM Implementation](/en/learn/custom-llm)
  * [Custom Manager Agent](/en/learn/custom-manager-agent)
  * [Customize Agents](/en/learn/customizing-agents)
  * [Image Generation with DALL-E](/en/learn/dalle-image-generation)
  * [Force Tool Output as Result](/en/learn/force-tool-output-as-result)
  * [Hierarchical Process](/en/learn/hierarchical-process)
  * [Human Input on Execution](/en/learn/human-input-on-execution)
  * [Human-in-the-Loop (HITL) Workflows](/en/learn/human-in-the-loop)
  * [Kickoff Crew Asynchronously](/en/learn/kickoff-async)
  * [Kickoff Crew for Each](/en/learn/kickoff-for-each)
  * [Connect to any LLM](/en/learn/llm-connections)
  * [Using Multimodal Agents](/en/learn/multimodal-agents)
  * [Replay Tasks from Latest Crew Kickoff](/en/learn/replay-tasks-from-latest-crew-kickoff)
  * [Sequential Processes](/en/learn/sequential-process)
  * [Using Annotations in crew.py](/en/learn/using-annotations)
  * [Execution Hooks Overview](/en/learn/execution-hooks)
  * [LLM Call Hooks](/en/learn/llm-hooks)
  * [Tool Call Hooks](/en/learn/tool-hooks)



##### Telemetry

  * [Telemetry](/en/telemetry)



Strategy

# Evaluating Use Cases for CrewAI

Copy page

Learn how to assess your AI application needs and choose the right approach between Crews and Flows based on complexity and precision requirements.

Copy page

## 

​

Understanding the Decision Framework

When building AI applications with CrewAI, one of the most important decisions you’ll make is choosing the right approach for your specific use case. Should you use a Crew? A Flow? A combination of both? This guide will help you evaluate your requirements and make informed architectural decisions. At the heart of this decision is understanding the relationship between **complexity** and **precision** in your application:

![Complexity vs. Precision Matrix](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/complexity_precision.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=ba6f265da6ac72075285b5008735be82)

Complexity vs. Precision Matrix for CrewAI Applications

This matrix helps visualize how different approaches align with varying requirements for complexity and precision. Let’s explore what each quadrant means and how it guides your architectural choices.

## 

​

The Complexity-Precision Matrix Explained

### 

​

What is Complexity?

In the context of CrewAI applications, **complexity** refers to:

  * The number of distinct steps or operations required
  * The diversity of tasks that need to be performed
  * The interdependencies between different components
  * The need for conditional logic and branching
  * The sophistication of the overall workflow



### 

​

What is Precision?

**Precision** in this context refers to:

  * The accuracy required in the final output
  * The need for structured, predictable results
  * The importance of reproducibility
  * The level of control needed over each step
  * The tolerance for variation in outputs



### 

​

The Four Quadrants

#### 

​

1\. Low Complexity, Low Precision

**Characteristics:**

  * Simple, straightforward tasks
  * Tolerance for some variation in outputs
  * Limited number of steps
  * Creative or exploratory applications

**Recommended Approach:** Simple Crews with minimal agents **Example Use Cases:**

  * Basic content generation
  * Idea brainstorming
  * Simple summarization tasks
  * Creative writing assistance



#### 

​

2\. Low Complexity, High Precision

**Characteristics:**

  * Simple workflows that require exact, structured outputs
  * Need for reproducible results
  * Limited steps but high accuracy requirements
  * Often involves data processing or transformation

**Recommended Approach:** Flows with direct LLM calls or simple Crews with structured outputs **Example Use Cases:**

  * Data extraction and transformation
  * Form filling and validation
  * Structured content generation (JSON, XML)
  * Simple classification tasks



#### 

​

3\. High Complexity, Low Precision

**Characteristics:**

  * Multi-stage processes with many steps
  * Creative or exploratory outputs
  * Complex interactions between components
  * Tolerance for variation in final results

**Recommended Approach:** Complex Crews with multiple specialized agents **Example Use Cases:**

  * Research and analysis
  * Content creation pipelines
  * Exploratory data analysis
  * Creative problem-solving



#### 

​

4\. High Complexity, High Precision

**Characteristics:**

  * Complex workflows requiring structured outputs
  * Multiple interdependent steps with strict accuracy requirements
  * Need for both sophisticated processing and precise results
  * Often mission-critical applications

**Recommended Approach:** Flows orchestrating multiple Crews with validation steps **Example Use Cases:**

  * Enterprise decision support systems
  * Complex data processing pipelines
  * Multi-stage document processing
  * Regulated industry applications



## 

​

Choosing Between Crews and Flows

### 

​

When to Choose Crews

Crews are ideal when:

  1. **You need collaborative intelligence** \- Multiple agents with different specializations need to work together
  2. **The problem requires emergent thinking** \- The solution benefits from different perspectives and approaches
  3. **The task is primarily creative or analytical** \- The work involves research, content creation, or analysis
  4. **You value adaptability over strict structure** \- The workflow can benefit from agent autonomy
  5. **The output format can be somewhat flexible** \- Some variation in output structure is acceptable



Copy

Ask AI
    
    
    # Example: Research Crew for market analysis
    from crewai import Agent, Crew, Process, Task
    
    # Create specialized agents
    researcher = Agent(
        role="Market Research Specialist",
        goal="Find comprehensive market data on emerging technologies",
        backstory="You are an expert at discovering market trends and gathering data."
    )
    
    analyst = Agent(
        role="Market Analyst",
        goal="Analyze market data and identify key opportunities",
        backstory="You excel at interpreting market data and spotting valuable insights."
    )
    
    # Define their tasks
    research_task = Task(
        description="Research the current market landscape for AI-powered healthcare solutions",
        expected_output="Comprehensive market data including key players, market size, and growth trends",
        agent=researcher
    )
    
    analysis_task = Task(
        description="Analyze the market data and identify the top 3 investment opportunities",
        expected_output="Analysis report with 3 recommended investment opportunities and rationale",
        agent=analyst,
        context=[research_task]
    )
    
    # Create the crew
    market_analysis_crew = Crew(
        agents=[researcher, analyst],
        tasks=[research_task, analysis_task],
        process=Process.sequential,
        verbose=True
    )
    
    # Run the crew
    result = market_analysis_crew.kickoff()
    

### 

​

When to Choose Flows

Flows are ideal when:

  1. **You need precise control over execution** \- The workflow requires exact sequencing and state management
  2. **The application has complex state requirements** \- You need to maintain and transform state across multiple steps
  3. **You need structured, predictable outputs** \- The application requires consistent, formatted results
  4. **The workflow involves conditional logic** \- Different paths need to be taken based on intermediate results
  5. **You need to combine AI with procedural code** \- The solution requires both AI capabilities and traditional programming



Copy

Ask AI
    
    
    # Example: Customer Support Flow with structured processing
    from crewai.flow.flow import Flow, listen, router, start
    from pydantic import BaseModel
    from typing import List, Dict
    
    # Define structured state
    class SupportTicketState(BaseModel):
        ticket_id: str = ""
        customer_name: str = ""
        issue_description: str = ""
        category: str = ""
        priority: str = "medium"
        resolution: str = ""
        satisfaction_score: int = 0
    
    class CustomerSupportFlow(Flow[SupportTicketState]):
        @start()
        def receive_ticket(self):
            # In a real app, this might come from an API
            self.state.ticket_id = "TKT-12345"
            self.state.customer_name = "Alex Johnson"
            self.state.issue_description = "Unable to access premium features after payment"
            return "Ticket received"
    
        @listen(receive_ticket)
        def categorize_ticket(self, _):
            # Use a direct LLM call for categorization
            from crewai import LLM
            llm = LLM(model="openai/gpt-4o-mini")
    
            prompt = f"""
            Categorize the following customer support issue into one of these categories:
            - Billing
            - Account Access
            - Technical Issue
            - Feature Request
            - Other
    
            Issue: {self.state.issue_description}
    
            Return only the category name.
            """
    
            self.state.category = llm.call(prompt).strip()
            return self.state.category
    
        @router(categorize_ticket)
        def route_by_category(self, category):
            # Route to different handlers based on category
            return category.lower().replace(" ", "_")
    
        @listen("billing")
        def handle_billing_issue(self):
            # Handle billing-specific logic
            self.state.priority = "high"
            # More billing-specific processing...
            return "Billing issue handled"
    
        @listen("account_access")
        def handle_access_issue(self):
            # Handle access-specific logic
            self.state.priority = "high"
            # More access-specific processing...
            return "Access issue handled"
    
        # Additional category handlers...
    
        @listen("billing", "account_access", "technical_issue", "feature_request", "other")
        def resolve_ticket(self, resolution_info):
            # Final resolution step
            self.state.resolution = f"Issue resolved: {resolution_info}"
            return self.state.resolution
    
    # Run the flow
    support_flow = CustomerSupportFlow()
    result = support_flow.kickoff()
    

### 

​

When to Combine Crews and Flows

The most sophisticated applications often benefit from combining Crews and Flows:

  1. **Complex multi-stage processes** \- Use Flows to orchestrate the overall process and Crews for complex subtasks
  2. **Applications requiring both creativity and structure** \- Use Crews for creative tasks and Flows for structured processing
  3. **Enterprise-grade AI applications** \- Use Flows to manage state and process flow while leveraging Crews for specialized work



Copy

Ask AI
    
    
    # Example: Content Production Pipeline combining Crews and Flows
    from crewai.flow.flow import Flow, listen, start
    from crewai import Agent, Crew, Process, Task
    from pydantic import BaseModel
    from typing import List, Dict
    
    class ContentState(BaseModel):
        topic: str = ""
        target_audience: str = ""
        content_type: str = ""
        outline: Dict = {}
        draft_content: str = ""
        final_content: str = ""
        seo_score: int = 0
    
    class ContentProductionFlow(Flow[ContentState]):
        @start()
        def initialize_project(self):
            # Set initial parameters
            self.state.topic = "Sustainable Investing"
            self.state.target_audience = "Millennial Investors"
            self.state.content_type = "Blog Post"
            return "Project initialized"
    
        @listen(initialize_project)
        def create_outline(self, _):
            # Use a research crew to create an outline
            researcher = Agent(
                role="Content Researcher",
                goal=f"Research {self.state.topic} for {self.state.target_audience}",
                backstory="You are an expert researcher with deep knowledge of content creation."
            )
    
            outliner = Agent(
                role="Content Strategist",
                goal=f"Create an engaging outline for a {self.state.content_type}",
                backstory="You excel at structuring content for maximum engagement."
            )
    
            research_task = Task(
                description=f"Research {self.state.topic} focusing on what would interest {self.state.target_audience}",
                expected_output="Comprehensive research notes with key points and statistics",
                agent=researcher
            )
    
            outline_task = Task(
                description=f"Create an outline for a {self.state.content_type} about {self.state.topic}",
                expected_output="Detailed content outline with sections and key points",
                agent=outliner,
                context=[research_task]
            )
    
            outline_crew = Crew(
                agents=[researcher, outliner],
                tasks=[research_task, outline_task],
                process=Process.sequential,
                verbose=True
            )
    
            # Run the crew and store the result
            result = outline_crew.kickoff()
    
            # Parse the outline (in a real app, you might use a more robust parsing approach)
            import json
            try:
                self.state.outline = json.loads(result.raw)
            except:
                # Fallback if not valid JSON
                self.state.outline = {"sections": result.raw}
    
            return "Outline created"
    
        @listen(create_outline)
        def write_content(self, _):
            # Use a writing crew to create the content
            writer = Agent(
                role="Content Writer",
                goal=f"Write engaging content for {self.state.target_audience}",
                backstory="You are a skilled writer who creates compelling content."
            )
    
            editor = Agent(
                role="Content Editor",
                goal="Ensure content is polished, accurate, and engaging",
                backstory="You have a keen eye for detail and a talent for improving content."
            )
    
            writing_task = Task(
                description=f"Write a {self.state.content_type} about {self.state.topic} following this outline: {self.state.outline}",
                expected_output="Complete draft content in markdown format",
                agent=writer
            )
    
            editing_task = Task(
                description="Edit and improve the draft content for clarity, engagement, and accuracy",
                expected_output="Polished final content in markdown format",
                agent=editor,
                context=[writing_task]
            )
    
            writing_crew = Crew(
                agents=[writer, editor],
                tasks=[writing_task, editing_task],
                process=Process.sequential,
                verbose=True
            )
    
            # Run the crew and store the result
            result = writing_crew.kickoff()
            self.state.final_content = result.raw
    
            return "Content created"
    
        @listen(write_content)
        def optimize_for_seo(self, _):
            # Use a direct LLM call for SEO optimization
            from crewai import LLM
            llm = LLM(model="openai/gpt-4o-mini")
    
            prompt = f"""
            Analyze this content for SEO effectiveness for the keyword "{self.state.topic}".
            Rate it on a scale of 1-100 and provide 3 specific recommendations for improvement.
    
            Content: {self.state.final_content[:1000]}... (truncated for brevity)
    
            Format your response as JSON with the following structure:
            {{
                "score": 85,
                "recommendations": [
                    "Recommendation 1",
                    "Recommendation 2",
                    "Recommendation 3"
                ]
            }}
            """
    
            seo_analysis = llm.call(prompt)
    
            # Parse the SEO analysis
            import json
            try:
                analysis = json.loads(seo_analysis)
                self.state.seo_score = analysis.get("score", 0)
                return analysis
            except:
                self.state.seo_score = 50
                return {"score": 50, "recommendations": ["Unable to parse SEO analysis"]}
    
    # Run the flow
    content_flow = ContentProductionFlow()
    result = content_flow.kickoff()
    

## 

​

Practical Evaluation Framework

To determine the right approach for your specific use case, follow this step-by-step evaluation framework:

### 

​

Step 1: Assess Complexity

Rate your application’s complexity on a scale of 1-10 by considering:

  1. **Number of steps** : How many distinct operations are required?
     * 1-3 steps: Low complexity (1-3)
     * 4-7 steps: Medium complexity (4-7)
     * 8+ steps: High complexity (8-10)
  2. **Interdependencies** : How interconnected are the different parts?
     * Few dependencies: Low complexity (1-3)
     * Some dependencies: Medium complexity (4-7)
     * Many complex dependencies: High complexity (8-10)
  3. **Conditional logic** : How much branching and decision-making is needed?
     * Linear process: Low complexity (1-3)
     * Some branching: Medium complexity (4-7)
     * Complex decision trees: High complexity (8-10)
  4. **Domain knowledge** : How specialized is the knowledge required?
     * General knowledge: Low complexity (1-3)
     * Some specialized knowledge: Medium complexity (4-7)
     * Deep expertise in multiple domains: High complexity (8-10)

Calculate your average score to determine overall complexity.

### 

​

Step 2: Assess Precision Requirements

Rate your precision requirements on a scale of 1-10 by considering:

  1. **Output structure** : How structured must the output be?
     * Free-form text: Low precision (1-3)
     * Semi-structured: Medium precision (4-7)
     * Strictly formatted (JSON, XML): High precision (8-10)
  2. **Accuracy needs** : How important is factual accuracy?
     * Creative content: Low precision (1-3)
     * Informational content: Medium precision (4-7)
     * Critical information: High precision (8-10)
  3. **Reproducibility** : How consistent must results be across runs?
     * Variation acceptable: Low precision (1-3)
     * Some consistency needed: Medium precision (4-7)
     * Exact reproducibility required: High precision (8-10)
  4. **Error tolerance** : What is the impact of errors?
     * Low impact: Low precision (1-3)
     * Moderate impact: Medium precision (4-7)
     * High impact: High precision (8-10)

Calculate your average score to determine overall precision requirements.

### 

​

Step 3: Map to the Matrix

Plot your complexity and precision scores on the matrix:

  * **Low Complexity (1-4), Low Precision (1-4)** : Simple Crews
  * **Low Complexity (1-4), High Precision (5-10)** : Flows with direct LLM calls
  * **High Complexity (5-10), Low Precision (1-4)** : Complex Crews
  * **High Complexity (5-10), High Precision (5-10)** : Flows orchestrating Crews



### 

​

Step 4: Consider Additional Factors

Beyond complexity and precision, consider:

  1. **Development time** : Crews are often faster to prototype
  2. **Maintenance needs** : Flows provide better long-term maintainability
  3. **Team expertise** : Consider your team’s familiarity with different approaches
  4. **Scalability requirements** : Flows typically scale better for complex applications
  5. **Integration needs** : Consider how the solution will integrate with existing systems



## 

​

Conclusion

Choosing between Crews and Flows—or combining them—is a critical architectural decision that impacts the effectiveness, maintainability, and scalability of your CrewAI application. By evaluating your use case along the dimensions of complexity and precision, you can make informed decisions that align with your specific requirements. Remember that the best approach often evolves as your application matures. Start with the simplest solution that meets your needs, and be prepared to refine your architecture as you gain experience and your requirements become clearer.

You now have a framework for evaluating CrewAI use cases and choosing the right approach based on complexity and precision requirements. This will help you build more effective, maintainable, and scalable AI applications.

## 

​

Next Steps

  * Learn more about [crafting effective agents](/en/guides/agents/crafting-effective-agents)
  * Explore [building your first crew](/en/guides/crews/first-crew)
  * Dive into [mastering flow state management](/en/guides/flows/mastering-flow-state)
  * Check out the [core concepts](/en/concepts/agents) for deeper understanding



Was this page helpful?

YesNo

[QuickstartPrevious](/en/quickstart)[Crafting Effective AgentsNext](/en/guides/agents/crafting-effective-agents)

Ctrl+I

[website](https://crewai.com)[x](https://x.com/crewAIInc)[github](https://github.com/crewAIInc/crewAI)[linkedin](https://www.linkedin.com/company/crewai-inc)[youtube](https://youtube.com/@crewAIInc)[reddit](https://www.reddit.com/r/crewAIInc/)

[Powered by Mintlify](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=crewai)

Assistant

Responses are generated using AI and may contain mistakes.

![Complexity vs. Precision Matrix](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/complexity_precision.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=780bae03e53c2fcfd4dce5e3c8672372)


---

# Source: https://docs.crewai.com/en/guides/agents/crafting-effective-agents

Skip to main content

[CrewAI home page![light logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)![dark logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)](/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl K

Search...

Navigation

Agents

Crafting Effective Agents

[Home](/)[Documentation](/en/introduction)[AOP](/en/enterprise/introduction)[API Reference](/en/api-reference/introduction)[Examples](/en/examples/example)[Changelog](/en/changelog)

  * [Website](https://crewai.com)
  * [Forum](https://community.crewai.com)
  * [Blog](https://blog.crewai.com)
  * [CrewGPT](https://chatgpt.com/g/g-qqTuUWsBY-crewai-assistant)



##### Get Started

  * [Introduction](/en/introduction)
  * [Installation](/en/installation)
  * [Quickstart](/en/quickstart)



##### Guides

  * Strategy

  * Agents

    * [Crafting Effective Agents](/en/guides/agents/crafting-effective-agents)
  * Crews

  * Flows

  * Advanced




##### Core Concepts

  * [Agents](/en/concepts/agents)
  * [Tasks](/en/concepts/tasks)
  * [Crews](/en/concepts/crews)
  * [Flows](/en/concepts/flows)
  * [Knowledge](/en/concepts/knowledge)
  * [LLMs](/en/concepts/llms)
  * [Processes](/en/concepts/processes)
  * [Collaboration](/en/concepts/collaboration)
  * [Training](/en/concepts/training)
  * [Memory](/en/concepts/memory)
  * [Reasoning](/en/concepts/reasoning)
  * [Planning](/en/concepts/planning)
  * [Testing](/en/concepts/testing)
  * [CLI](/en/concepts/cli)
  * [Tools](/en/concepts/tools)
  * [Event Listeners](/en/concepts/event-listener)



##### MCP Integration

  * [MCP Servers as Tools in CrewAI](/en/mcp/overview)
  * [MCP DSL Integration](/en/mcp/dsl-integration)
  * [Stdio Transport](/en/mcp/stdio)
  * [SSE Transport](/en/mcp/sse)
  * [Streamable HTTP Transport](/en/mcp/streamable-http)
  * [Connecting to Multiple MCP Servers](/en/mcp/multiple-servers)
  * [MCP Security Considerations](/en/mcp/security)



##### Tools

  * [Tools Overview](/en/tools/overview)
  * File & Document

  * Web Scraping & Browsing

  * Search & Research

  * Database & Data

  * AI & Machine Learning

  * Cloud & Storage

  * Integrations

  * Automation




##### Observability

  * [CrewAI Tracing](/en/observability/tracing)
  * [Overview](/en/observability/overview)
  * [Arize Phoenix](/en/observability/arize-phoenix)
  * [Braintrust](/en/observability/braintrust)
  * [Datadog Integration](/en/observability/datadog)
  * [LangDB Integration](/en/observability/langdb)
  * [Langfuse Integration](/en/observability/langfuse)
  * [Langtrace Integration](/en/observability/langtrace)
  * [Maxim Integration](/en/observability/maxim)
  * [MLflow Integration](/en/observability/mlflow)
  * [Neatlogs Integration](/en/observability/neatlogs)
  * [OpenLIT Integration](/en/observability/openlit)
  * [Opik Integration](/en/observability/opik)
  * [Patronus AI Evaluation](/en/observability/patronus-evaluation)
  * [Portkey Integration](/en/observability/portkey)
  * [Weave Integration](/en/observability/weave)
  * [TrueFoundry Integration](/en/observability/truefoundry)



##### Learn

  * [Overview](/en/learn/overview)
  * [Strategic LLM Selection Guide](/en/learn/llm-selection-guide)
  * [Conditional Tasks](/en/learn/conditional-tasks)
  * [Coding Agents](/en/learn/coding-agents)
  * [Create Custom Tools](/en/learn/create-custom-tools)
  * [Custom LLM Implementation](/en/learn/custom-llm)
  * [Custom Manager Agent](/en/learn/custom-manager-agent)
  * [Customize Agents](/en/learn/customizing-agents)
  * [Image Generation with DALL-E](/en/learn/dalle-image-generation)
  * [Force Tool Output as Result](/en/learn/force-tool-output-as-result)
  * [Hierarchical Process](/en/learn/hierarchical-process)
  * [Human Input on Execution](/en/learn/human-input-on-execution)
  * [Human-in-the-Loop (HITL) Workflows](/en/learn/human-in-the-loop)
  * [Kickoff Crew Asynchronously](/en/learn/kickoff-async)
  * [Kickoff Crew for Each](/en/learn/kickoff-for-each)
  * [Connect to any LLM](/en/learn/llm-connections)
  * [Using Multimodal Agents](/en/learn/multimodal-agents)
  * [Replay Tasks from Latest Crew Kickoff](/en/learn/replay-tasks-from-latest-crew-kickoff)
  * [Sequential Processes](/en/learn/sequential-process)
  * [Using Annotations in crew.py](/en/learn/using-annotations)
  * [Execution Hooks Overview](/en/learn/execution-hooks)
  * [LLM Call Hooks](/en/learn/llm-hooks)
  * [Tool Call Hooks](/en/learn/tool-hooks)



##### Telemetry

  * [Telemetry](/en/telemetry)



Agents

# Crafting Effective Agents

Copy page

Learn best practices for designing powerful, specialized AI agents that collaborate effectively to solve complex problems.

Copy page

## 

​

The Art and Science of Agent Design

At the heart of CrewAI lies the agent - a specialized AI entity designed to perform specific roles within a collaborative framework. While creating basic agents is simple, crafting truly effective agents that produce exceptional results requires understanding key design principles and best practices. This guide will help you master the art of agent design, enabling you to create specialized AI personas that collaborate effectively, think critically, and produce high-quality outputs tailored to your specific needs.

### 

​

Why Agent Design Matters

The way you define your agents significantly impacts:

  1. **Output quality** : Well-designed agents produce more relevant, high-quality results
  2. **Collaboration effectiveness** : Agents with complementary skills work together more efficiently
  3. **Task performance** : Agents with clear roles and goals execute tasks more effectively
  4. **System scalability** : Thoughtfully designed agents can be reused across multiple crews and contexts

Let’s explore best practices for creating agents that excel in these dimensions.

## 

​

The 80/20 Rule: Focus on Tasks Over Agents

When building effective AI systems, remember this crucial principle: **80% of your effort should go into designing tasks, and only 20% into defining agents**. Why? Because even the most perfectly defined agent will fail with poorly designed tasks, but well-designed tasks can elevate even a simple agent. This means:

  * Spend most of your time writing clear task instructions
  * Define detailed inputs and expected outputs
  * Add examples and context to guide execution
  * Dedicate the remaining time to agent role, goal, and backstory

This doesn’t mean agent design isn’t important - it absolutely is. But task design is where most execution failures occur, so prioritize accordingly.

## 

​

Core Principles of Effective Agent Design

### 

​

1\. The Role-Goal-Backstory Framework

The most powerful agents in CrewAI are built on a strong foundation of three key elements:

#### 

​

Role: The Agent’s Specialized Function

The role defines what the agent does and their area of expertise. When crafting roles:

  * **Be specific and specialized** : Instead of “Writer,” use “Technical Documentation Specialist” or “Creative Storyteller”
  * **Align with real-world professions** : Base roles on recognizable professional archetypes
  * **Include domain expertise** : Specify the agent’s field of knowledge (e.g., “Financial Analyst specializing in market trends”)

**Examples of effective roles:**

Copy

Ask AI
    
    
    role: "Senior UX Researcher specializing in user interview analysis"
    role: "Full-Stack Software Architect with expertise in distributed systems"
    role: "Corporate Communications Director specializing in crisis management"
    

#### 

​

Goal: The Agent’s Purpose and Motivation

The goal directs the agent’s efforts and shapes their decision-making process. Effective goals should:

  * **Be clear and outcome-focused** : Define what the agent is trying to achieve
  * **Emphasize quality standards** : Include expectations about the quality of work
  * **Incorporate success criteria** : Help the agent understand what “good” looks like

**Examples of effective goals:**

Copy

Ask AI
    
    
    goal: "Uncover actionable user insights by analyzing interview data and identifying recurring patterns, unmet needs, and improvement opportunities"
    goal: "Design robust, scalable system architectures that balance performance, maintainability, and cost-effectiveness"
    goal: "Craft clear, empathetic crisis communications that address stakeholder concerns while protecting organizational reputation"
    

#### 

​

Backstory: The Agent’s Experience and Perspective

The backstory gives depth to the agent, influencing how they approach problems and interact with others. Good backstories:

  * **Establish expertise and experience** : Explain how the agent gained their skills
  * **Define working style and values** : Describe how the agent approaches their work
  * **Create a cohesive persona** : Ensure all elements of the backstory align with the role and goal

**Examples of effective backstories:**

Copy

Ask AI
    
    
    backstory: "You have spent 15 years conducting and analyzing user research for top tech companies. You have a talent for reading between the lines and identifying patterns that others miss. You believe that good UX is invisible and that the best insights come from listening to what users don't say as much as what they do say."
    
    backstory: "With 20+ years of experience building distributed systems at scale, you've developed a pragmatic approach to software architecture. You've seen both successful and failed systems and have learned valuable lessons from each. You balance theoretical best practices with practical constraints and always consider the maintenance and operational aspects of your designs."
    
    backstory: "As a seasoned communications professional who has guided multiple organizations through high-profile crises, you understand the importance of transparency, speed, and empathy in crisis response. You have a methodical approach to crafting messages that address concerns while maintaining organizational credibility."
    

### 

​

2\. Specialists Over Generalists

Agents perform significantly better when given specialized roles rather than general ones. A highly focused agent delivers more precise, relevant outputs: **Generic (Less Effective):**

Copy

Ask AI
    
    
    role: "Writer"
    

**Specialized (More Effective):**

Copy

Ask AI
    
    
    role: "Technical Blog Writer specializing in explaining complex AI concepts to non-technical audiences"
    

**Specialist Benefits:**

  * Clearer understanding of expected output
  * More consistent performance
  * Better alignment with specific tasks
  * Improved ability to make domain-specific judgments



### 

​

3\. Balancing Specialization and Versatility

Effective agents strike the right balance between specialization (doing one thing extremely well) and versatility (being adaptable to various situations):

  * **Specialize in role, versatile in application** : Create agents with specialized skills that can be applied across multiple contexts
  * **Avoid overly narrow definitions** : Ensure agents can handle variations within their domain of expertise
  * **Consider the collaborative context** : Design agents whose specializations complement the other agents they’ll work with



### 

​

4\. Setting Appropriate Expertise Levels

The expertise level you assign to your agent shapes how they approach tasks:

  * **Novice agents** : Good for straightforward tasks, brainstorming, or initial drafts
  * **Intermediate agents** : Suitable for most standard tasks with reliable execution
  * **Expert agents** : Best for complex, specialized tasks requiring depth and nuance
  * **World-class agents** : Reserved for critical tasks where exceptional quality is needed

Choose the appropriate expertise level based on task complexity and quality requirements. For most collaborative crews, a mix of expertise levels often works best, with higher expertise assigned to core specialized functions.

## 

​

Practical Examples: Before and After

Let’s look at some examples of agent definitions before and after applying these best practices:

### 

​

Example 1: Content Creation Agent

**Before:**

Copy

Ask AI
    
    
    role: "Writer"
    goal: "Write good content"
    backstory: "You are a writer who creates content for websites."
    

**After:**

Copy

Ask AI
    
    
    role: "B2B Technology Content Strategist"
    goal: "Create compelling, technically accurate content that explains complex topics in accessible language while driving reader engagement and supporting business objectives"
    backstory: "You have spent a decade creating content for leading technology companies, specializing in translating technical concepts for business audiences. You excel at research, interviewing subject matter experts, and structuring information for maximum clarity and impact. You believe that the best B2B content educates first and sells second, building trust through genuine expertise rather than marketing hype."
    

### 

​

Example 2: Research Agent

**Before:**

Copy

Ask AI
    
    
    role: "Researcher"
    goal: "Find information"
    backstory: "You are good at finding information online."
    

**After:**

Copy

Ask AI
    
    
    role: "Academic Research Specialist in Emerging Technologies"
    goal: "Discover and synthesize cutting-edge research, identifying key trends, methodologies, and findings while evaluating the quality and reliability of sources"
    backstory: "With a background in both computer science and library science, you've mastered the art of digital research. You've worked with research teams at prestigious universities and know how to navigate academic databases, evaluate research quality, and synthesize findings across disciplines. You're methodical in your approach, always cross-referencing information and tracing claims to primary sources before drawing conclusions."
    

## 

​

Crafting Effective Tasks for Your Agents

While agent design is important, task design is critical for successful execution. Here are best practices for designing tasks that set your agents up for success:

### 

​

The Anatomy of an Effective Task

A well-designed task has two key components that serve different purposes:

#### 

​

Task Description: The Process

The description should focus on what to do and how to do it, including:

  * Detailed instructions for execution
  * Context and background information
  * Scope and constraints
  * Process steps to follow



#### 

​

Expected Output: The Deliverable

The expected output should define what the final result should look like:

  * Format specifications (markdown, JSON, etc.)
  * Structure requirements
  * Quality criteria
  * Examples of good outputs (when possible)



### 

​

Task Design Best Practices

#### 

​

1\. Single Purpose, Single Output

Tasks perform best when focused on one clear objective: **Bad Example (Too Broad):**

Copy

Ask AI
    
    
    task_description: "Research market trends, analyze the data, and create a visualization."
    

**Good Example (Focused):**

Copy

Ask AI
    
    
    # Task 1
    research_task:
      description: "Research the top 5 market trends in the AI industry for 2024."
      expected_output: "A markdown list of the 5 trends with supporting evidence."
    
    # Task 2
    analysis_task:
      description: "Analyze the identified trends to determine potential business impacts."
      expected_output: "A structured analysis with impact ratings (High/Medium/Low)."
    
    # Task 3
    visualization_task:
      description: "Create a visual representation of the analyzed trends."
      expected_output: "A description of a chart showing trends and their impact ratings."
    

#### 

​

2\. Be Explicit About Inputs and Outputs

Always clearly specify what inputs the task will use and what the output should look like: **Example:**

Copy

Ask AI
    
    
    analysis_task:
      description: >
        Analyze the customer feedback data from the CSV file.
        Focus on identifying recurring themes related to product usability.
        Consider sentiment and frequency when determining importance.
      expected_output: >
        A markdown report with the following sections:
        1. Executive summary (3-5 bullet points)
        2. Top 3 usability issues with supporting data
        3. Recommendations for improvement
    

#### 

​

3\. Include Purpose and Context

Explain why the task matters and how it fits into the larger workflow: **Example:**

Copy

Ask AI
    
    
    competitor_analysis_task:
      description: >
        Analyze our three main competitors' pricing strategies.
        This analysis will inform our upcoming pricing model revision.
        Focus on identifying patterns in how they price premium features
        and how they structure their tiered offerings.
    

#### 

​

4\. Use Structured Output Tools

For machine-readable outputs, specify the format clearly: **Example:**

Copy

Ask AI
    
    
    data_extraction_task:
      description: "Extract key metrics from the quarterly report."
      expected_output: "JSON object with the following keys: revenue, growth_rate, customer_acquisition_cost, and retention_rate."
    

## 

​

Common Mistakes to Avoid

Based on lessons learned from real-world implementations, here are the most common pitfalls in agent and task design:

### 

​

1\. Unclear Task Instructions

**Problem:** Tasks lack sufficient detail, making it difficult for agents to execute effectively. **Example of Poor Design:**

Copy

Ask AI
    
    
    research_task:
      description: "Research AI trends."
      expected_output: "A report on AI trends."
    

**Improved Version:**

Copy

Ask AI
    
    
    research_task:
      description: >
        Research the top emerging AI trends for 2024 with a focus on:
        1. Enterprise adoption patterns
        2. Technical breakthroughs in the past 6 months
        3. Regulatory developments affecting implementation
    
        For each trend, identify key companies, technologies, and potential business impacts.
      expected_output: >
        A comprehensive markdown report with:
        - Executive summary (5 bullet points)
        - 5-7 major trends with supporting evidence
        - For each trend: definition, examples, and business implications
        - References to authoritative sources
    

### 

​

2\. “God Tasks” That Try to Do Too Much

**Problem:** Tasks that combine multiple complex operations into one instruction set. **Example of Poor Design:**

Copy

Ask AI
    
    
    comprehensive_task:
      description: "Research market trends, analyze competitor strategies, create a marketing plan, and design a launch timeline."
    

**Improved Version:** Break this into sequential, focused tasks:

Copy

Ask AI
    
    
    # Task 1: Research
    market_research_task:
      description: "Research current market trends in the SaaS project management space."
      expected_output: "A markdown summary of key market trends."
    
    # Task 2: Competitive Analysis
    competitor_analysis_task:
      description: "Analyze strategies of the top 3 competitors based on the market research."
      expected_output: "A comparison table of competitor strategies."
      context: [market_research_task]
    
    # Continue with additional focused tasks...
    

### 

​

3\. Misaligned Description and Expected Output

**Problem:** The task description asks for one thing while the expected output specifies something different. **Example of Poor Design:**

Copy

Ask AI
    
    
    analysis_task:
      description: "Analyze customer feedback to find areas of improvement."
      expected_output: "A marketing plan for the next quarter."
    

**Improved Version:**

Copy

Ask AI
    
    
    analysis_task:
      description: "Analyze customer feedback to identify the top 3 areas for product improvement."
      expected_output: "A report listing the 3 priority improvement areas with supporting customer quotes and data points."
    

### 

​

4\. Not Understanding the Process Yourself

**Problem:** Asking agents to execute tasks that you yourself don’t fully understand. **Solution:**

  1. Try to perform the task manually first
  2. Document your process, decision points, and information sources
  3. Use this documentation as the basis for your task description



### 

​

5\. Premature Use of Hierarchical Structures

**Problem:** Creating unnecessarily complex agent hierarchies where sequential processes would work better. **Solution:** Start with sequential processes and only move to hierarchical models when the workflow complexity truly requires it.

### 

​

6\. Vague or Generic Agent Definitions

**Problem:** Generic agent definitions lead to generic outputs. **Example of Poor Design:**

Copy

Ask AI
    
    
    agent:
      role: "Business Analyst"
      goal: "Analyze business data"
      backstory: "You are good at business analysis."
    

**Improved Version:**

Copy

Ask AI
    
    
    agent:
      role: "SaaS Metrics Specialist focusing on growth-stage startups"
      goal: "Identify actionable insights from business data that can directly impact customer retention and revenue growth"
      backstory: "With 10+ years analyzing SaaS business models, you've developed a keen eye for the metrics that truly matter for sustainable growth. You've helped numerous companies identify the leverage points that turned around their business trajectory. You believe in connecting data to specific, actionable recommendations rather than general observations."
    

## 

​

Advanced Agent Design Strategies

### 

​

Designing for Collaboration

When creating agents that will work together in a crew, consider:

  * **Complementary skills** : Design agents with distinct but complementary abilities
  * **Handoff points** : Define clear interfaces for how work passes between agents
  * **Constructive tension** : Sometimes, creating agents with slightly different perspectives can lead to better outcomes through productive dialogue

For example, a content creation crew might include:

Copy

Ask AI
    
    
    # Research Agent
    role: "Research Specialist for technical topics"
    goal: "Gather comprehensive, accurate information from authoritative sources"
    backstory: "You are a meticulous researcher with a background in library science..."
    
    # Writer Agent
    role: "Technical Content Writer"
    goal: "Transform research into engaging, clear content that educates and informs"
    backstory: "You are an experienced writer who excels at explaining complex concepts..."
    
    # Editor Agent
    role: "Content Quality Editor"
    goal: "Ensure content is accurate, well-structured, and polished while maintaining consistency"
    backstory: "With years of experience in publishing, you have a keen eye for detail..."
    

### 

​

Creating Specialized Tool Users

Some agents can be designed specifically to leverage certain tools effectively:

Copy

Ask AI
    
    
    role: "Data Analysis Specialist"
    goal: "Derive meaningful insights from complex datasets through statistical analysis"
    backstory: "With a background in data science, you excel at working with structured and unstructured data..."
    tools: [PythonREPLTool, DataVisualizationTool, CSVAnalysisTool]
    

### 

​

Tailoring Agents to LLM Capabilities

Different LLMs have different strengths. Design your agents with these capabilities in mind:

Copy

Ask AI
    
    
    # For complex reasoning tasks
    analyst:
      role: "Data Insights Analyst"
      goal: "..."
      backstory: "..."
      llm: openai/gpt-4o
    
    # For creative content
    writer:
      role: "Creative Content Writer"
      goal: "..."
      backstory: "..."
      llm: anthropic/claude-3-opus
    

## 

​

Testing and Iterating on Agent Design

Agent design is often an iterative process. Here’s a practical approach:

  1. **Start with a prototype** : Create an initial agent definition
  2. **Test with sample tasks** : Evaluate performance on representative tasks
  3. **Analyze outputs** : Identify strengths and weaknesses
  4. **Refine the definition** : Adjust role, goal, and backstory based on observations
  5. **Test in collaboration** : Evaluate how the agent performs in a crew setting



## 

​

Conclusion

Crafting effective agents is both an art and a science. By carefully defining roles, goals, and backstories that align with your specific needs, and combining them with well-designed tasks, you can create specialized AI collaborators that produce exceptional results. Remember that agent and task design is an iterative process. Start with these best practices, observe your agents in action, and refine your approach based on what you learn. And always keep in mind the 80/20 rule - focus most of your effort on creating clear, focused tasks to get the best results from your agents.

Congratulations! You now understand the principles and practices of effective agent design. Apply these techniques to create powerful, specialized agents that work together seamlessly to accomplish complex tasks.

## 

​

Next Steps

  * Experiment with different agent configurations for your specific use case
  * Learn about [building your first crew](/en/guides/crews/first-crew) to see how agents work together
  * Explore [CrewAI Flows](/en/guides/flows/first-flow) for more advanced orchestration



Was this page helpful?

YesNo

[Evaluating Use Cases for CrewAIPrevious](/en/guides/concepts/evaluating-use-cases)[Build Your First CrewNext](/en/guides/crews/first-crew)

Ctrl+I

[website](https://crewai.com)[x](https://x.com/crewAIInc)[github](https://github.com/crewAIInc/crewAI)[linkedin](https://www.linkedin.com/company/crewai-inc)[youtube](https://youtube.com/@crewAIInc)[reddit](https://www.reddit.com/r/crewAIInc/)

[Powered by Mintlify](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=crewai)

Assistant

Responses are generated using AI and may contain mistakes.


---

# Source: https://docs.crewai.com/en/guides/crews/first-crew

Skip to main content

[CrewAI home page![light logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)![dark logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)](/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl K

Search...

Navigation

Crews

Build Your First Crew

[Home](/)[Documentation](/en/introduction)[AOP](/en/enterprise/introduction)[API Reference](/en/api-reference/introduction)[Examples](/en/examples/example)[Changelog](/en/changelog)

  * [Website](https://crewai.com)
  * [Forum](https://community.crewai.com)
  * [Blog](https://blog.crewai.com)
  * [CrewGPT](https://chatgpt.com/g/g-qqTuUWsBY-crewai-assistant)



##### Get Started

  * [Introduction](/en/introduction)
  * [Installation](/en/installation)
  * [Quickstart](/en/quickstart)



##### Guides

  * Strategy

  * Agents

  * Crews

    * [Build Your First Crew](/en/guides/crews/first-crew)
  * Flows

  * Advanced




##### Core Concepts

  * [Agents](/en/concepts/agents)
  * [Tasks](/en/concepts/tasks)
  * [Crews](/en/concepts/crews)
  * [Flows](/en/concepts/flows)
  * [Knowledge](/en/concepts/knowledge)
  * [LLMs](/en/concepts/llms)
  * [Processes](/en/concepts/processes)
  * [Collaboration](/en/concepts/collaboration)
  * [Training](/en/concepts/training)
  * [Memory](/en/concepts/memory)
  * [Reasoning](/en/concepts/reasoning)
  * [Planning](/en/concepts/planning)
  * [Testing](/en/concepts/testing)
  * [CLI](/en/concepts/cli)
  * [Tools](/en/concepts/tools)
  * [Event Listeners](/en/concepts/event-listener)



##### MCP Integration

  * [MCP Servers as Tools in CrewAI](/en/mcp/overview)
  * [MCP DSL Integration](/en/mcp/dsl-integration)
  * [Stdio Transport](/en/mcp/stdio)
  * [SSE Transport](/en/mcp/sse)
  * [Streamable HTTP Transport](/en/mcp/streamable-http)
  * [Connecting to Multiple MCP Servers](/en/mcp/multiple-servers)
  * [MCP Security Considerations](/en/mcp/security)



##### Tools

  * [Tools Overview](/en/tools/overview)
  * File & Document

  * Web Scraping & Browsing

  * Search & Research

  * Database & Data

  * AI & Machine Learning

  * Cloud & Storage

  * Integrations

  * Automation




##### Observability

  * [CrewAI Tracing](/en/observability/tracing)
  * [Overview](/en/observability/overview)
  * [Arize Phoenix](/en/observability/arize-phoenix)
  * [Braintrust](/en/observability/braintrust)
  * [Datadog Integration](/en/observability/datadog)
  * [LangDB Integration](/en/observability/langdb)
  * [Langfuse Integration](/en/observability/langfuse)
  * [Langtrace Integration](/en/observability/langtrace)
  * [Maxim Integration](/en/observability/maxim)
  * [MLflow Integration](/en/observability/mlflow)
  * [Neatlogs Integration](/en/observability/neatlogs)
  * [OpenLIT Integration](/en/observability/openlit)
  * [Opik Integration](/en/observability/opik)
  * [Patronus AI Evaluation](/en/observability/patronus-evaluation)
  * [Portkey Integration](/en/observability/portkey)
  * [Weave Integration](/en/observability/weave)
  * [TrueFoundry Integration](/en/observability/truefoundry)



##### Learn

  * [Overview](/en/learn/overview)
  * [Strategic LLM Selection Guide](/en/learn/llm-selection-guide)
  * [Conditional Tasks](/en/learn/conditional-tasks)
  * [Coding Agents](/en/learn/coding-agents)
  * [Create Custom Tools](/en/learn/create-custom-tools)
  * [Custom LLM Implementation](/en/learn/custom-llm)
  * [Custom Manager Agent](/en/learn/custom-manager-agent)
  * [Customize Agents](/en/learn/customizing-agents)
  * [Image Generation with DALL-E](/en/learn/dalle-image-generation)
  * [Force Tool Output as Result](/en/learn/force-tool-output-as-result)
  * [Hierarchical Process](/en/learn/hierarchical-process)
  * [Human Input on Execution](/en/learn/human-input-on-execution)
  * [Human-in-the-Loop (HITL) Workflows](/en/learn/human-in-the-loop)
  * [Kickoff Crew Asynchronously](/en/learn/kickoff-async)
  * [Kickoff Crew for Each](/en/learn/kickoff-for-each)
  * [Connect to any LLM](/en/learn/llm-connections)
  * [Using Multimodal Agents](/en/learn/multimodal-agents)
  * [Replay Tasks from Latest Crew Kickoff](/en/learn/replay-tasks-from-latest-crew-kickoff)
  * [Sequential Processes](/en/learn/sequential-process)
  * [Using Annotations in crew.py](/en/learn/using-annotations)
  * [Execution Hooks Overview](/en/learn/execution-hooks)
  * [LLM Call Hooks](/en/learn/llm-hooks)
  * [Tool Call Hooks](/en/learn/tool-hooks)



##### Telemetry

  * [Telemetry](/en/telemetry)



Crews

# Build Your First Crew

Copy page

Step-by-step tutorial to create a collaborative AI team that works together to solve complex problems.

Copy page

## 

​

Unleashing the Power of Collaborative AI

Imagine having a team of specialized AI agents working together seamlessly to solve complex problems, each contributing their unique skills to achieve a common goal. This is the power of CrewAI - a framework that enables you to create collaborative AI systems that can accomplish tasks far beyond what a single AI could achieve alone. In this guide, we’ll walk through creating a research crew that will help us research and analyze a topic, then create a comprehensive report. This practical example demonstrates how AI agents can collaborate to accomplish complex tasks, but it’s just the beginning of what’s possible with CrewAI.

### 

​

What You’ll Build and Learn

By the end of this guide, you’ll have:

  1. **Created a specialized AI research team** with distinct roles and responsibilities
  2. **Orchestrated collaboration** between multiple AI agents
  3. **Automated a complex workflow** that involves gathering information, analysis, and report generation
  4. **Built foundational skills** that you can apply to more ambitious projects

While we’re building a simple research crew in this guide, the same patterns and techniques can be applied to create much more sophisticated teams for tasks like:

  * Multi-stage content creation with specialized writers, editors, and fact-checkers
  * Complex customer service systems with tiered support agents
  * Autonomous business analysts that gather data, create visualizations, and generate insights
  * Product development teams that ideate, design, and plan implementation

Let’s get started building your first crew!

### 

​

Prerequisites

Before starting, make sure you have:

  1. Installed CrewAI following the [installation guide](/en/installation)
  2. Set up your LLM API key in your environment, following the [LLM setup guide](/en/concepts/llms#setting-up-your-llm)
  3. Basic understanding of Python



## 

​

Step 1: Create a New CrewAI Project

First, let’s create a new CrewAI project using the CLI. This command will set up a complete project structure with all the necessary files, allowing you to focus on defining your agents and their tasks rather than setting up boilerplate code.

Copy

Ask AI
    
    
    crewai create crew research_crew
    cd research_crew
    

This will generate a project with the basic structure needed for your crew. The CLI automatically creates:

  * A project directory with the necessary files
  * Configuration files for agents and tasks
  * A basic crew implementation
  * A main script to run the crew



![CrewAI Framework Overview](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=514fd0b06e4128e62f10728d44601975)

CrewAI Framework Overview

## 

​

Step 2: Explore the Project Structure

Let’s take a moment to understand the project structure created by the CLI. CrewAI follows best practices for Python projects, making it easy to maintain and extend your code as your crews become more complex.

Copy

Ask AI
    
    
    research_crew/
    ├── .gitignore
    ├── pyproject.toml
    ├── README.md
    ├── .env
    └── src/
        └── research_crew/
            ├── __init__.py
            ├── main.py
            ├── crew.py
            ├── tools/
            │   ├── custom_tool.py
            │   └── __init__.py
            └── config/
                ├── agents.yaml
                └── tasks.yaml
    

This structure follows best practices for Python projects and makes it easy to organize your code. The separation of configuration files (in YAML) from implementation code (in Python) makes it easy to modify your crew’s behavior without changing the underlying code.

## 

​

Step 3: Configure Your Agents

Now comes the fun part - defining your AI agents! In CrewAI, agents are specialized entities with specific roles, goals, and backstories that shape their behavior. Think of them as characters in a play, each with their own personality and purpose. For our research crew, we’ll create two agents:

  1. A **researcher** who excels at finding and organizing information
  2. An **analyst** who can interpret research findings and create insightful reports

Let’s modify the `agents.yaml` file to define these specialized agents. Be sure to set `llm` to the provider you are using.

Copy

Ask AI
    
    
    # src/research_crew/config/agents.yaml
    researcher:
      role: >
        Senior Research Specialist for {topic}
      goal: >
        Find comprehensive and accurate information about {topic}
        with a focus on recent developments and key insights
      backstory: >
        You are an experienced research specialist with a talent for
        finding relevant information from various sources. You excel at
        organizing information in a clear and structured manner, making
        complex topics accessible to others.
      llm: provider/model-id  # e.g. openai/gpt-4o, google/gemini-2.0-flash, anthropic/claude...
    
    analyst:
      role: >
        Data Analyst and Report Writer for {topic}
      goal: >
        Analyze research findings and create a comprehensive, well-structured
        report that presents insights in a clear and engaging way
      backstory: >
        You are a skilled analyst with a background in data interpretation
        and technical writing. You have a talent for identifying patterns
        and extracting meaningful insights from research data, then
        communicating those insights effectively through well-crafted reports.
      llm: provider/model-id  # e.g. openai/gpt-4o, google/gemini-2.0-flash, anthropic/claude...
    

Notice how each agent has a distinct role, goal, and backstory. These elements aren’t just descriptive - they actively shape how the agent approaches its tasks. By crafting these carefully, you can create agents with specialized skills and perspectives that complement each other.

## 

​

Step 4: Define Your Tasks

With our agents defined, we now need to give them specific tasks to perform. Tasks in CrewAI represent the concrete work that agents will perform, with detailed instructions and expected outputs. For our research crew, we’ll define two main tasks:

  1. A **research task** for gathering comprehensive information
  2. An **analysis task** for creating an insightful report

Let’s modify the `tasks.yaml` file:

Copy

Ask AI
    
    
    # src/research_crew/config/tasks.yaml
    research_task:
      description: >
        Conduct thorough research on {topic}. Focus on:
        1. Key concepts and definitions
        2. Historical development and recent trends
        3. Major challenges and opportunities
        4. Notable applications or case studies
        5. Future outlook and potential developments
    
        Make sure to organize your findings in a structured format with clear sections.
      expected_output: >
        A comprehensive research document with well-organized sections covering
        all the requested aspects of {topic}. Include specific facts, figures,
        and examples where relevant.
      agent: researcher
    
    analysis_task:
      description: >
        Analyze the research findings and create a comprehensive report on {topic}.
        Your report should:
        1. Begin with an executive summary
        2. Include all key information from the research
        3. Provide insightful analysis of trends and patterns
        4. Offer recommendations or future considerations
        5. Be formatted in a professional, easy-to-read style with clear headings
      expected_output: >
        A polished, professional report on {topic} that presents the research
        findings with added analysis and insights. The report should be well-structured
        with an executive summary, main sections, and conclusion.
      agent: analyst
      context:
        - research_task
      output_file: output/report.md
    

Note the `context` field in the analysis task - this is a powerful feature that allows the analyst to access the output of the research task. This creates a workflow where information flows naturally between agents, just as it would in a human team.

## 

​

Step 5: Configure Your Crew

Now it’s time to bring everything together by configuring our crew. The crew is the container that orchestrates how agents work together to complete tasks. Let’s modify the `crew.py` file:

Copy

Ask AI
    
    
    # src/research_crew/crew.py
    from crewai import Agent, Crew, Process, Task
    from crewai.project import CrewBase, agent, crew, task
    from crewai_tools import SerperDevTool
    from crewai.agents.agent_builder.base_agent import BaseAgent
    from typing import List
    
    @CrewBase
    class ResearchCrew():
        """Research crew for comprehensive topic analysis and reporting"""
    
        agents: List[BaseAgent]
        tasks: List[Task]
    
        @agent
        def researcher(self) -> Agent:
            return Agent(
                config=self.agents_config['researcher'], # type: ignore[index]
                verbose=True,
                tools=[SerperDevTool()]
            )
    
        @agent
        def analyst(self) -> Agent:
            return Agent(
                config=self.agents_config['analyst'], # type: ignore[index]
                verbose=True
            )
    
        @task
        def research_task(self) -> Task:
            return Task(
                config=self.tasks_config['research_task'] # type: ignore[index]
            )
    
        @task
        def analysis_task(self) -> Task:
            return Task(
                config=self.tasks_config['analysis_task'], # type: ignore[index]
                output_file='output/report.md'
            )
    
        @crew
        def crew(self) -> Crew:
            """Creates the research crew"""
            return Crew(
                agents=self.agents,
                tasks=self.tasks,
                process=Process.sequential,
                verbose=True,
            )
    

In this code, we’re:

  1. Creating the researcher agent and equipping it with the SerperDevTool to search the web
  2. Creating the analyst agent
  3. Setting up the research and analysis tasks
  4. Configuring the crew to run tasks sequentially (the analyst will wait for the researcher to finish)

This is where the magic happens - with just a few lines of code, we’ve defined a collaborative AI system where specialized agents work together in a coordinated process.

## 

​

Step 6: Set Up Your Main Script

Now, let’s set up the main script that will run our crew. This is where we provide the specific topic we want our crew to research.

Copy

Ask AI
    
    
    #!/usr/bin/env python
    # src/research_crew/main.py
    import os
    from research_crew.crew import ResearchCrew
    
    # Create output directory if it doesn't exist
    os.makedirs('output', exist_ok=True)
    
    def run():
        """
        Run the research crew.
        """
        inputs = {
            'topic': 'Artificial Intelligence in Healthcare'
        }
    
        # Create and run the crew
        result = ResearchCrew().crew().kickoff(inputs=inputs)
    
        # Print the result
        print("\n\n=== FINAL REPORT ===\n\n")
        print(result.raw)
    
        print("\n\nReport has been saved to output/report.md")
    
    if __name__ == "__main__":
        run()
    

This script prepares the environment, specifies our research topic, and kicks off the crew’s work. The power of CrewAI is evident in how simple this code is - all the complexity of managing multiple AI agents is handled by the framework.

## 

​

Step 7: Set Up Your Environment Variables

Create a `.env` file in your project root with your API keys:

Copy

Ask AI
    
    
    SERPER_API_KEY=your_serper_api_key
    # Add your provider's API key here too.
    

See the [LLM Setup guide](/en/concepts/llms#setting-up-your-llm) for details on configuring your provider of choice. You can get a Serper API key from [Serper.dev](https://serper.dev/).

## 

​

Step 8: Install Dependencies

Install the required dependencies using the CrewAI CLI:

Copy

Ask AI
    
    
    crewai install
    

This command will:

  1. Read the dependencies from your project configuration
  2. Create a virtual environment if needed
  3. Install all required packages



## 

​

Step 9: Run Your Crew

Now for the exciting moment - it’s time to run your crew and see AI collaboration in action!

Copy

Ask AI
    
    
    crewai run
    

When you run this command, you’ll see your crew spring to life. The researcher will gather information about the specified topic, and the analyst will then create a comprehensive report based on that research. You’ll see the agents’ thought processes, actions, and outputs in real-time as they work together to complete their tasks.

## 

​

Step 10: Review the Output

Once the crew completes its work, you’ll find the final report in the `output/report.md` file. The report will include:

  1. An executive summary
  2. Detailed information about the topic
  3. Analysis and insights
  4. Recommendations or future considerations

Take a moment to appreciate what you’ve accomplished - you’ve created a system where multiple AI agents collaborated on a complex task, each contributing their specialized skills to produce a result that’s greater than what any single agent could achieve alone.

## 

​

Exploring Other CLI Commands

CrewAI offers several other useful CLI commands for working with crews:

Copy

Ask AI
    
    
    # View all available commands
    crewai --help
    
    # Run the crew
    crewai run
    
    # Test the crew
    crewai test
    
    # Reset crew memories
    crewai reset-memories
    
    # Replay from a specific task
    crewai replay -t <task_id>
    

## 

​

The Art of the Possible: Beyond Your First Crew

What you’ve built in this guide is just the beginning. The skills and patterns you’ve learned can be applied to create increasingly sophisticated AI systems. Here are some ways you could extend this basic research crew:

### 

​

Expanding Your Crew

You could add more specialized agents to your crew:

  * A **fact-checker** to verify research findings
  * A **data visualizer** to create charts and graphs
  * A **domain expert** with specialized knowledge in a particular area
  * A **critic** to identify weaknesses in the analysis



### 

​

Adding Tools and Capabilities

You could enhance your agents with additional tools:

  * Web browsing tools for real-time research
  * CSV/database tools for data analysis
  * Code execution tools for data processing
  * API connections to external services



### 

​

Creating More Complex Workflows

You could implement more sophisticated processes:

  * Hierarchical processes where manager agents delegate to worker agents
  * Iterative processes with feedback loops for refinement
  * Parallel processes where multiple agents work simultaneously
  * Dynamic processes that adapt based on intermediate results



### 

​

Applying to Different Domains

The same patterns can be applied to create crews for:

  * **Content creation** : Writers, editors, fact-checkers, and designers working together
  * **Customer service** : Triage agents, specialists, and quality control working together
  * **Product development** : Researchers, designers, and planners collaborating
  * **Data analysis** : Data collectors, analysts, and visualization specialists



## 

​

Next Steps

Now that you’ve built your first crew, you can:

  1. Experiment with different agent configurations and personalities
  2. Try more complex task structures and workflows
  3. Implement custom tools to give your agents new capabilities
  4. Apply your crew to different topics or problem domains
  5. Explore [CrewAI Flows](/en/guides/flows/first-flow) for more advanced workflows with procedural programming



Congratulations! You’ve successfully built your first CrewAI crew that can research and analyze any topic you provide. This foundational experience has equipped you with the skills to create increasingly sophisticated AI systems that can tackle complex, multi-stage problems through collaborative intelligence.

Was this page helpful?

YesNo

[Crafting Effective AgentsPrevious](/en/guides/agents/crafting-effective-agents)[Build Your First FlowNext](/en/guides/flows/first-flow)

Ctrl+I

[website](https://crewai.com)[x](https://x.com/crewAIInc)[github](https://github.com/crewAIInc/crewAI)[linkedin](https://www.linkedin.com/company/crewai-inc)[youtube](https://youtube.com/@crewAIInc)[reddit](https://www.reddit.com/r/crewAIInc/)

[Powered by Mintlify](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=crewai)

Assistant

Responses are generated using AI and may contain mistakes.

![CrewAI Framework Overview](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=92b76be34b84b36771e0a8eed8976966)


---

# Source: https://docs.crewai.com/en/guides/flows/first-flow

Skip to main content

[CrewAI home page![light logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)![dark logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)](/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl K

Search...

Navigation

Flows

Build Your First Flow

[Home](/)[Documentation](/en/introduction)[AOP](/en/enterprise/introduction)[API Reference](/en/api-reference/introduction)[Examples](/en/examples/example)[Changelog](/en/changelog)

  * [Website](https://crewai.com)
  * [Forum](https://community.crewai.com)
  * [Blog](https://blog.crewai.com)
  * [CrewGPT](https://chatgpt.com/g/g-qqTuUWsBY-crewai-assistant)



##### Get Started

  * [Introduction](/en/introduction)
  * [Installation](/en/installation)
  * [Quickstart](/en/quickstart)



##### Guides

  * Strategy

  * Agents

  * Crews

  * Flows

    * [Build Your First Flow](/en/guides/flows/first-flow)
    * [Mastering Flow State Management](/en/guides/flows/mastering-flow-state)
  * Advanced




##### Core Concepts

  * [Agents](/en/concepts/agents)
  * [Tasks](/en/concepts/tasks)
  * [Crews](/en/concepts/crews)
  * [Flows](/en/concepts/flows)
  * [Knowledge](/en/concepts/knowledge)
  * [LLMs](/en/concepts/llms)
  * [Processes](/en/concepts/processes)
  * [Collaboration](/en/concepts/collaboration)
  * [Training](/en/concepts/training)
  * [Memory](/en/concepts/memory)
  * [Reasoning](/en/concepts/reasoning)
  * [Planning](/en/concepts/planning)
  * [Testing](/en/concepts/testing)
  * [CLI](/en/concepts/cli)
  * [Tools](/en/concepts/tools)
  * [Event Listeners](/en/concepts/event-listener)



##### MCP Integration

  * [MCP Servers as Tools in CrewAI](/en/mcp/overview)
  * [MCP DSL Integration](/en/mcp/dsl-integration)
  * [Stdio Transport](/en/mcp/stdio)
  * [SSE Transport](/en/mcp/sse)
  * [Streamable HTTP Transport](/en/mcp/streamable-http)
  * [Connecting to Multiple MCP Servers](/en/mcp/multiple-servers)
  * [MCP Security Considerations](/en/mcp/security)



##### Tools

  * [Tools Overview](/en/tools/overview)
  * File & Document

  * Web Scraping & Browsing

  * Search & Research

  * Database & Data

  * AI & Machine Learning

  * Cloud & Storage

  * Integrations

  * Automation




##### Observability

  * [CrewAI Tracing](/en/observability/tracing)
  * [Overview](/en/observability/overview)
  * [Arize Phoenix](/en/observability/arize-phoenix)
  * [Braintrust](/en/observability/braintrust)
  * [Datadog Integration](/en/observability/datadog)
  * [LangDB Integration](/en/observability/langdb)
  * [Langfuse Integration](/en/observability/langfuse)
  * [Langtrace Integration](/en/observability/langtrace)
  * [Maxim Integration](/en/observability/maxim)
  * [MLflow Integration](/en/observability/mlflow)
  * [Neatlogs Integration](/en/observability/neatlogs)
  * [OpenLIT Integration](/en/observability/openlit)
  * [Opik Integration](/en/observability/opik)
  * [Patronus AI Evaluation](/en/observability/patronus-evaluation)
  * [Portkey Integration](/en/observability/portkey)
  * [Weave Integration](/en/observability/weave)
  * [TrueFoundry Integration](/en/observability/truefoundry)



##### Learn

  * [Overview](/en/learn/overview)
  * [Strategic LLM Selection Guide](/en/learn/llm-selection-guide)
  * [Conditional Tasks](/en/learn/conditional-tasks)
  * [Coding Agents](/en/learn/coding-agents)
  * [Create Custom Tools](/en/learn/create-custom-tools)
  * [Custom LLM Implementation](/en/learn/custom-llm)
  * [Custom Manager Agent](/en/learn/custom-manager-agent)
  * [Customize Agents](/en/learn/customizing-agents)
  * [Image Generation with DALL-E](/en/learn/dalle-image-generation)
  * [Force Tool Output as Result](/en/learn/force-tool-output-as-result)
  * [Hierarchical Process](/en/learn/hierarchical-process)
  * [Human Input on Execution](/en/learn/human-input-on-execution)
  * [Human-in-the-Loop (HITL) Workflows](/en/learn/human-in-the-loop)
  * [Kickoff Crew Asynchronously](/en/learn/kickoff-async)
  * [Kickoff Crew for Each](/en/learn/kickoff-for-each)
  * [Connect to any LLM](/en/learn/llm-connections)
  * [Using Multimodal Agents](/en/learn/multimodal-agents)
  * [Replay Tasks from Latest Crew Kickoff](/en/learn/replay-tasks-from-latest-crew-kickoff)
  * [Sequential Processes](/en/learn/sequential-process)
  * [Using Annotations in crew.py](/en/learn/using-annotations)
  * [Execution Hooks Overview](/en/learn/execution-hooks)
  * [LLM Call Hooks](/en/learn/llm-hooks)
  * [Tool Call Hooks](/en/learn/tool-hooks)



##### Telemetry

  * [Telemetry](/en/telemetry)



Flows

# Build Your First Flow

Copy page

Learn how to create structured, event-driven workflows with precise control over execution.

Copy page

## 

​

Taking Control of AI Workflows with Flows

CrewAI Flows represent the next level in AI orchestration - combining the collaborative power of AI agent crews with the precision and flexibility of procedural programming. While crews excel at agent collaboration, flows give you fine-grained control over exactly how and when different components of your AI system interact. In this guide, we’ll walk through creating a powerful CrewAI Flow that generates a comprehensive learning guide on any topic. This tutorial will demonstrate how Flows provide structured, event-driven control over your AI workflows by combining regular code, direct LLM calls, and crew-based processing.

### 

​

What Makes Flows Powerful

Flows enable you to:

  1. **Combine different AI interaction patterns** \- Use crews for complex collaborative tasks, direct LLM calls for simpler operations, and regular code for procedural logic
  2. **Build event-driven systems** \- Define how components respond to specific events and data changes
  3. **Maintain state across components** \- Share and transform data between different parts of your application
  4. **Integrate with external systems** \- Seamlessly connect your AI workflow with databases, APIs, and user interfaces
  5. **Create complex execution paths** \- Design conditional branches, parallel processing, and dynamic workflows



### 

​

What You’ll Build and Learn

By the end of this guide, you’ll have:

  1. **Created a sophisticated content generation system** that combines user input, AI planning, and multi-agent content creation
  2. **Orchestrated the flow of information** between different components of your system
  3. **Implemented event-driven architecture** where each step responds to the completion of previous steps
  4. **Built a foundation for more complex AI applications** that you can expand and customize

This guide creator flow demonstrates fundamental patterns that can be applied to create much more advanced applications, such as:

  * Interactive AI assistants that combine multiple specialized subsystems
  * Complex data processing pipelines with AI-enhanced transformations
  * Autonomous agents that integrate with external services and APIs
  * Multi-stage decision-making systems with human-in-the-loop processes

Let’s dive in and build your first flow!

## 

​

Prerequisites

Before starting, make sure you have:

  1. Installed CrewAI following the [installation guide](/en/installation)
  2. Set up your LLM API key in your environment, following the [LLM setup guide](/en/concepts/llms#setting-up-your-llm)
  3. Basic understanding of Python



## 

​

Step 1: Create a New CrewAI Flow Project

First, let’s create a new CrewAI Flow project using the CLI. This command sets up a scaffolded project with all the necessary directories and template files for your flow.

Copy

Ask AI
    
    
    crewai create flow guide_creator_flow
    cd guide_creator_flow
    

This will generate a project with the basic structure needed for your flow.

![CrewAI Framework Overview](https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=82ea168de2f004553dcea21410cd7d8a)

CrewAI Framework Overview

## 

​

Step 2: Understanding the Project Structure

The generated project has the following structure. Take a moment to familiarize yourself with it, as understanding this structure will help you create more complex flows in the future.

Copy

Ask AI
    
    
    guide_creator_flow/
    ├── .gitignore
    ├── pyproject.toml
    ├── README.md
    ├── .env
    ├── main.py
    ├── crews/
    │   └── poem_crew/
    │       ├── config/
    │       │   ├── agents.yaml
    │       │   └── tasks.yaml
    │       └── poem_crew.py
    └── tools/
        └── custom_tool.py
    

This structure provides a clear separation between different components of your flow:

  * The main flow logic in the `main.py` file
  * Specialized crews in the `crews` directory
  * Custom tools in the `tools` directory

We’ll modify this structure to create our guide creator flow, which will orchestrate the process of generating comprehensive learning guides.

## 

​

Step 3: Add a Content Writer Crew

Our flow will need a specialized crew to handle the content creation process. Let’s use the CrewAI CLI to add a content writer crew:

Copy

Ask AI
    
    
    crewai flow add-crew content-crew
    

This command automatically creates the necessary directories and template files for your crew. The content writer crew will be responsible for writing and reviewing sections of our guide, working within the overall flow orchestrated by our main application.

## 

​

Step 4: Configure the Content Writer Crew

Now, let’s modify the generated files for the content writer crew. We’ll set up two specialized agents - a writer and a reviewer - that will collaborate to create high-quality content for our guide.

  1. First, update the agents configuration file to define our content creation team: Remember to set `llm` to the provider you are using.



Copy

Ask AI
    
    
    # src/guide_creator_flow/crews/content_crew/config/agents.yaml
    content_writer:
      role: >
        Educational Content Writer
      goal: >
        Create engaging, informative content that thoroughly explains the assigned topic
        and provides valuable insights to the reader
      backstory: >
        You are a talented educational writer with expertise in creating clear, engaging
        content. You have a gift for explaining complex concepts in accessible language
        and organizing information in a way that helps readers build their understanding.
      llm: provider/model-id  # e.g. openai/gpt-4o, google/gemini-2.0-flash, anthropic/claude...
    
    content_reviewer:
      role: >
        Educational Content Reviewer and Editor
      goal: >
        Ensure content is accurate, comprehensive, well-structured, and maintains
        consistency with previously written sections
      backstory: >
        You are a meticulous editor with years of experience reviewing educational
        content. You have an eye for detail, clarity, and coherence. You excel at
        improving content while maintaining the original author's voice and ensuring
        consistent quality across multiple sections.
      llm: provider/model-id  # e.g. openai/gpt-4o, google/gemini-2.0-flash, anthropic/claude...
    

These agent definitions establish the specialized roles and perspectives that will shape how our AI agents approach content creation. Notice how each agent has a distinct purpose and expertise.

  2. Next, update the tasks configuration file to define the specific writing and reviewing tasks:



Copy

Ask AI
    
    
    # src/guide_creator_flow/crews/content_crew/config/tasks.yaml
    write_section_task:
      description: >
        Write a comprehensive section on the topic: "{section_title}"
    
        Section description: {section_description}
        Target audience: {audience_level} level learners
    
        Your content should:
        1. Begin with a brief introduction to the section topic
        2. Explain all key concepts clearly with examples
        3. Include practical applications or exercises where appropriate
        4. End with a summary of key points
        5. Be approximately 500-800 words in length
    
        Format your content in Markdown with appropriate headings, lists, and emphasis.
    
        Previously written sections:
        {previous_sections}
    
        Make sure your content maintains consistency with previously written sections
        and builds upon concepts that have already been explained.
      expected_output: >
        A well-structured, comprehensive section in Markdown format that thoroughly
        explains the topic and is appropriate for the target audience.
      agent: content_writer
    
    review_section_task:
      description: >
        Review and improve the following section on "{section_title}":
    
        {draft_content}
    
        Target audience: {audience_level} level learners
    
        Previously written sections:
        {previous_sections}
    
        Your review should:
        1. Fix any grammatical or spelling errors
        2. Improve clarity and readability
        3. Ensure content is comprehensive and accurate
        4. Verify consistency with previously written sections
        5. Enhance the structure and flow
        6. Add any missing key information
    
        Provide the improved version of the section in Markdown format.
      expected_output: >
        An improved, polished version of the section that maintains the original
        structure but enhances clarity, accuracy, and consistency.
      agent: content_reviewer
      context:
        - write_section_task
    

These task definitions provide detailed instructions to our agents, ensuring they produce content that meets our quality standards. Note how the `context` parameter in the review task creates a workflow where the reviewer has access to the writer’s output.

  3. Now, update the crew implementation file to define how our agents and tasks work together:



Copy

Ask AI
    
    
    # src/guide_creator_flow/crews/content_crew/content_crew.py
    from crewai import Agent, Crew, Process, Task
    from crewai.project import CrewBase, agent, crew, task
    from crewai.agents.agent_builder.base_agent import BaseAgent
    from typing import List
    
    @CrewBase
    class ContentCrew():
        """Content writing crew"""
    
        agents: List[BaseAgent]
        tasks: List[Task]
    
        @agent
        def content_writer(self) -> Agent:
            return Agent(
                config=self.agents_config['content_writer'], # type: ignore[index]
                verbose=True
            )
    
        @agent
        def content_reviewer(self) -> Agent:
            return Agent(
                config=self.agents_config['content_reviewer'], # type: ignore[index]
                verbose=True
            )
    
        @task
        def write_section_task(self) -> Task:
            return Task(
                config=self.tasks_config['write_section_task'] # type: ignore[index]
            )
    
        @task
        def review_section_task(self) -> Task:
            return Task(
                config=self.tasks_config['review_section_task'], # type: ignore[index]
                context=[self.write_section_task()]
            )
    
        @crew
        def crew(self) -> Crew:
            """Creates the content writing crew"""
            return Crew(
                agents=self.agents,
                tasks=self.tasks,
                process=Process.sequential,
                verbose=True,
            )
    

This crew definition establishes the relationship between our agents and tasks, setting up a sequential process where the content writer creates a draft and then the reviewer improves it. While this crew can function independently, in our flow it will be orchestrated as part of a larger system.

## 

​

Step 5: Create the Flow

Now comes the exciting part - creating the flow that will orchestrate the entire guide creation process. This is where we’ll combine regular Python code, direct LLM calls, and our content creation crew into a cohesive system. Our flow will:

  1. Get user input for a topic and audience level
  2. Make a direct LLM call to create a structured guide outline
  3. Process each section sequentially using the content writer crew
  4. Combine everything into a final comprehensive document

Let’s create our flow in the `main.py` file:

Copy

Ask AI
    
    
    #!/usr/bin/env python
    import json
    import os
    from typing import List, Dict
    from pydantic import BaseModel, Field
    from crewai import LLM
    from crewai.flow.flow import Flow, listen, start
    from guide_creator_flow.crews.content_crew.content_crew import ContentCrew
    
    # Define our models for structured data
    class Section(BaseModel):
        title: str = Field(description="Title of the section")
        description: str = Field(description="Brief description of what the section should cover")
    
    class GuideOutline(BaseModel):
        title: str = Field(description="Title of the guide")
        introduction: str = Field(description="Introduction to the topic")
        target_audience: str = Field(description="Description of the target audience")
        sections: List[Section] = Field(description="List of sections in the guide")
        conclusion: str = Field(description="Conclusion or summary of the guide")
    
    # Define our flow state
    class GuideCreatorState(BaseModel):
        topic: str = ""
        audience_level: str = ""
        guide_outline: GuideOutline = None
        sections_content: Dict[str, str] = {}
    
    class GuideCreatorFlow(Flow[GuideCreatorState]):
        """Flow for creating a comprehensive guide on any topic"""
    
        @start()
        def get_user_input(self):
            """Get input from the user about the guide topic and audience"""
            print("\n=== Create Your Comprehensive Guide ===\n")
    
            # Get user input
            self.state.topic = input("What topic would you like to create a guide for? ")
    
            # Get audience level with validation
            while True:
                audience = input("Who is your target audience? (beginner/intermediate/advanced) ").lower()
                if audience in ["beginner", "intermediate", "advanced"]:
                    self.state.audience_level = audience
                    break
                print("Please enter 'beginner', 'intermediate', or 'advanced'")
    
            print(f"\nCreating a guide on {self.state.topic} for {self.state.audience_level} audience...\n")
            return self.state
    
        @listen(get_user_input)
        def create_guide_outline(self, state):
            """Create a structured outline for the guide using a direct LLM call"""
            print("Creating guide outline...")
    
            # Initialize the LLM
            llm = LLM(model="openai/gpt-4o-mini", response_format=GuideOutline)
    
            # Create the messages for the outline
            messages = [
                {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
                {"role": "user", "content": f"""
                Create a detailed outline for a comprehensive guide on "{state.topic}" for {state.audience_level} level learners.
    
                The outline should include:
                1. A compelling title for the guide
                2. An introduction to the topic
                3. 4-6 main sections that cover the most important aspects of the topic
                4. A conclusion or summary
    
                For each section, provide a clear title and a brief description of what it should cover.
                """}
            ]
    
            # Make the LLM call with JSON response format
            response = llm.call(messages=messages)
    
            # Parse the JSON response
            outline_dict = json.loads(response)
            self.state.guide_outline = GuideOutline(**outline_dict)
    
            # Ensure output directory exists before saving
            os.makedirs("output", exist_ok=True)
    
            # Save the outline to a file
            with open("output/guide_outline.json", "w") as f:
                json.dump(outline_dict, f, indent=2)
    
            print(f"Guide outline created with {len(self.state.guide_outline.sections)} sections")
            return self.state.guide_outline
    
        @listen(create_guide_outline)
        def write_and_compile_guide(self, outline):
            """Write all sections and compile the guide"""
            print("Writing guide sections and compiling...")
            completed_sections = []
    
            # Process sections one by one to maintain context flow
            for section in outline.sections:
                print(f"Processing section: {section.title}")
    
                # Build context from previous sections
                previous_sections_text = ""
                if completed_sections:
                    previous_sections_text = "# Previously Written Sections\n\n"
                    for title in completed_sections:
                        previous_sections_text += f"## {title}\n\n"
                        previous_sections_text += self.state.sections_content.get(title, "") + "\n\n"
                else:
                    previous_sections_text = "No previous sections written yet."
    
                # Run the content crew for this section
                result = ContentCrew().crew().kickoff(inputs={
                    "section_title": section.title,
                    "section_description": section.description,
                    "audience_level": self.state.audience_level,
                    "previous_sections": previous_sections_text,
                    "draft_content": ""
                })
    
                # Store the content
                self.state.sections_content[section.title] = result.raw
                completed_sections.append(section.title)
                print(f"Section completed: {section.title}")
    
            # Compile the final guide
            guide_content = f"# {outline.title}\n\n"
            guide_content += f"## Introduction\n\n{outline.introduction}\n\n"
    
            # Add each section in order
            for section in outline.sections:
                section_content = self.state.sections_content.get(section.title, "")
                guide_content += f"\n\n{section_content}\n\n"
    
            # Add conclusion
            guide_content += f"## Conclusion\n\n{outline.conclusion}\n\n"
    
            # Save the guide
            with open("output/complete_guide.md", "w") as f:
                f.write(guide_content)
    
            print("\nComplete guide compiled and saved to output/complete_guide.md")
            return "Guide creation completed successfully"
    
    def kickoff():
        """Run the guide creator flow"""
        GuideCreatorFlow().kickoff()
        print("\n=== Flow Complete ===")
        print("Your comprehensive guide is ready in the output directory.")
        print("Open output/complete_guide.md to view it.")
    
    def plot():
        """Generate a visualization of the flow"""
        flow = GuideCreatorFlow()
        flow.plot("guide_creator_flow")
        print("Flow visualization saved to guide_creator_flow.html")
    
    if __name__ == "__main__":
        kickoff()
    

Let’s analyze what’s happening in this flow:

  1. We define Pydantic models for structured data, ensuring type safety and clear data representation
  2. We create a state class to maintain data across different steps of the flow
  3. We implement three main flow steps: 
     * Getting user input with the `@start()` decorator
     * Creating a guide outline with a direct LLM call
     * Processing sections with our content crew
  4. We use the `@listen()` decorator to establish event-driven relationships between steps

This is the power of flows - combining different types of processing (user interaction, direct LLM calls, crew-based tasks) into a coherent, event-driven system.

## 

​

Step 6: Set Up Your Environment Variables

Create a `.env` file in your project root with your API keys. See the [LLM setup guide](/en/concepts/llms#setting-up-your-llm) for details on configuring a provider.

.env

Copy

Ask AI
    
    
    OPENAI_API_KEY=your_openai_api_key
    # or
    GEMINI_API_KEY=your_gemini_api_key
    # or
    ANTHROPIC_API_KEY=your_anthropic_api_key
    

## 

​

Step 7: Install Dependencies

Install the required dependencies:

Copy

Ask AI
    
    
    crewai install
    

## 

​

Step 8: Run Your Flow

Now it’s time to see your flow in action! Run it using the CrewAI CLI:

Copy

Ask AI
    
    
    crewai flow kickoff
    

When you run this command, you’ll see your flow spring to life:

  1. It will prompt you for a topic and audience level
  2. It will create a structured outline for your guide
  3. It will process each section, with the content writer and reviewer collaborating on each
  4. Finally, it will compile everything into a comprehensive guide

This demonstrates the power of flows to orchestrate complex processes involving multiple components, both AI and non-AI.

## 

​

Step 9: Visualize Your Flow

One of the powerful features of flows is the ability to visualize their structure:

Copy

Ask AI
    
    
    crewai flow plot
    

This will create an HTML file that shows the structure of your flow, including the relationships between different steps and the data that flows between them. This visualization can be invaluable for understanding and debugging complex flows.

## 

​

Step 10: Review the Output

Once the flow completes, you’ll find two files in the `output` directory:

  1. `guide_outline.json`: Contains the structured outline of the guide
  2. `complete_guide.md`: The comprehensive guide with all sections

Take a moment to review these files and appreciate what you’ve built - a system that combines user input, direct AI interactions, and collaborative agent work to produce a complex, high-quality output.

## 

​

The Art of the Possible: Beyond Your First Flow

What you’ve learned in this guide provides a foundation for creating much more sophisticated AI systems. Here are some ways you could extend this basic flow:

### 

​

Enhancing User Interaction

You could create more interactive flows with:

  * Web interfaces for input and output
  * Real-time progress updates
  * Interactive feedback and refinement loops
  * Multi-stage user interactions



### 

​

Adding More Processing Steps

You could expand your flow with additional steps for:

  * Research before outline creation
  * Image generation for illustrations
  * Code snippet generation for technical guides
  * Final quality assurance and fact-checking



### 

​

Creating More Complex Flows

You could implement more sophisticated flow patterns:

  * Conditional branching based on user preferences or content type
  * Parallel processing of independent sections
  * Iterative refinement loops with feedback
  * Integration with external APIs and services



### 

​

Applying to Different Domains

The same patterns can be applied to create flows for:

  * **Interactive storytelling** : Create personalized stories based on user input
  * **Business intelligence** : Process data, generate insights, and create reports
  * **Product development** : Facilitate ideation, design, and planning
  * **Educational systems** : Create personalized learning experiences



## 

​

Key Features Demonstrated

This guide creator flow demonstrates several powerful features of CrewAI:

  1. **User interaction** : The flow collects input directly from the user
  2. **Direct LLM calls** : Uses the LLM class for efficient, single-purpose AI interactions
  3. **Structured data with Pydantic** : Uses Pydantic models to ensure type safety
  4. **Sequential processing with context** : Writes sections in order, providing previous sections for context
  5. **Multi-agent crews** : Leverages specialized agents (writer and reviewer) for content creation
  6. **State management** : Maintains state across different steps of the process
  7. **Event-driven architecture** : Uses the `@listen` decorator to respond to events



## 

​

Understanding the Flow Structure

Let’s break down the key components of flows to help you understand how to build your own:

### 

​

1\. Direct LLM Calls

Flows allow you to make direct calls to language models when you need simple, structured responses:

Copy

Ask AI
    
    
    llm = LLM(
        model="model-id-here",  # gpt-4o, gemini-2.0-flash, anthropic/claude...
        response_format=GuideOutline
    )
    response = llm.call(messages=messages)
    

This is more efficient than using a crew when you need a specific, structured output.

### 

​

2\. Event-Driven Architecture

Flows use decorators to establish relationships between components:

Copy

Ask AI
    
    
    @start()
    def get_user_input(self):
        # First step in the flow
        # ...
    
    @listen(get_user_input)
    def create_guide_outline(self, state):
        # This runs when get_user_input completes
        # ...
    

This creates a clear, declarative structure for your application.

### 

​

3\. State Management

Flows maintain state across steps, making it easy to share data:

Copy

Ask AI
    
    
    class GuideCreatorState(BaseModel):
        topic: str = ""
        audience_level: str = ""
        guide_outline: GuideOutline = None
        sections_content: Dict[str, str] = {}
    

This provides a type-safe way to track and transform data throughout your flow.

### 

​

4\. Crew Integration

Flows can seamlessly integrate with crews for complex collaborative tasks:

Copy

Ask AI
    
    
    result = ContentCrew().crew().kickoff(inputs={
        "section_title": section.title,
        # ...
    })
    

This allows you to use the right tool for each part of your application - direct LLM calls for simple tasks and crews for complex collaboration.

## 

​

Next Steps

Now that you’ve built your first flow, you can:

  1. Experiment with more complex flow structures and patterns
  2. Try using `@router()` to create conditional branches in your flows
  3. Explore the `and_` and `or_` functions for more complex parallel execution
  4. Connect your flow to external APIs, databases, or user interfaces
  5. Combine multiple specialized crews in a single flow



Congratulations! You’ve successfully built your first CrewAI Flow that combines regular code, direct LLM calls, and crew-based processing to create a comprehensive guide. These foundational skills enable you to create increasingly sophisticated AI applications that can tackle complex, multi-stage problems through a combination of procedural control and collaborative intelligence.

Was this page helpful?

YesNo

[Build Your First CrewPrevious](/en/guides/crews/first-crew)[Mastering Flow State ManagementNext](/en/guides/flows/mastering-flow-state)

Ctrl+I

[website](https://crewai.com)[x](https://x.com/crewAIInc)[github](https://github.com/crewAIInc/crewAI)[linkedin](https://www.linkedin.com/company/crewai-inc)[youtube](https://youtube.com/@crewAIInc)[reddit](https://www.reddit.com/r/crewAIInc/)

[Powered by Mintlify](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=crewai)

Assistant

Responses are generated using AI and may contain mistakes.

![CrewAI Framework Overview](https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=7900e4cdad93fd37bbcd2f1f2f38b40b)


---

# Source: https://docs.crewai.com/en/guides/flows/mastering-flow-state

Skip to main content

[CrewAI home page![light logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)![dark logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)](/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl K

Search...

Navigation

Flows

Mastering Flow State Management

[Home](/)[Documentation](/en/introduction)[AOP](/en/enterprise/introduction)[API Reference](/en/api-reference/introduction)[Examples](/en/examples/example)[Changelog](/en/changelog)

  * [Website](https://crewai.com)
  * [Forum](https://community.crewai.com)
  * [Blog](https://blog.crewai.com)
  * [CrewGPT](https://chatgpt.com/g/g-qqTuUWsBY-crewai-assistant)



##### Get Started

  * [Introduction](/en/introduction)
  * [Installation](/en/installation)
  * [Quickstart](/en/quickstart)



##### Guides

  * Strategy

  * Agents

  * Crews

  * Flows

    * [Build Your First Flow](/en/guides/flows/first-flow)
    * [Mastering Flow State Management](/en/guides/flows/mastering-flow-state)
  * Advanced




##### Core Concepts

  * [Agents](/en/concepts/agents)
  * [Tasks](/en/concepts/tasks)
  * [Crews](/en/concepts/crews)
  * [Flows](/en/concepts/flows)
  * [Knowledge](/en/concepts/knowledge)
  * [LLMs](/en/concepts/llms)
  * [Processes](/en/concepts/processes)
  * [Collaboration](/en/concepts/collaboration)
  * [Training](/en/concepts/training)
  * [Memory](/en/concepts/memory)
  * [Reasoning](/en/concepts/reasoning)
  * [Planning](/en/concepts/planning)
  * [Testing](/en/concepts/testing)
  * [CLI](/en/concepts/cli)
  * [Tools](/en/concepts/tools)
  * [Event Listeners](/en/concepts/event-listener)



##### MCP Integration

  * [MCP Servers as Tools in CrewAI](/en/mcp/overview)
  * [MCP DSL Integration](/en/mcp/dsl-integration)
  * [Stdio Transport](/en/mcp/stdio)
  * [SSE Transport](/en/mcp/sse)
  * [Streamable HTTP Transport](/en/mcp/streamable-http)
  * [Connecting to Multiple MCP Servers](/en/mcp/multiple-servers)
  * [MCP Security Considerations](/en/mcp/security)



##### Tools

  * [Tools Overview](/en/tools/overview)
  * File & Document

  * Web Scraping & Browsing

  * Search & Research

  * Database & Data

  * AI & Machine Learning

  * Cloud & Storage

  * Integrations

  * Automation




##### Observability

  * [CrewAI Tracing](/en/observability/tracing)
  * [Overview](/en/observability/overview)
  * [Arize Phoenix](/en/observability/arize-phoenix)
  * [Braintrust](/en/observability/braintrust)
  * [Datadog Integration](/en/observability/datadog)
  * [LangDB Integration](/en/observability/langdb)
  * [Langfuse Integration](/en/observability/langfuse)
  * [Langtrace Integration](/en/observability/langtrace)
  * [Maxim Integration](/en/observability/maxim)
  * [MLflow Integration](/en/observability/mlflow)
  * [Neatlogs Integration](/en/observability/neatlogs)
  * [OpenLIT Integration](/en/observability/openlit)
  * [Opik Integration](/en/observability/opik)
  * [Patronus AI Evaluation](/en/observability/patronus-evaluation)
  * [Portkey Integration](/en/observability/portkey)
  * [Weave Integration](/en/observability/weave)
  * [TrueFoundry Integration](/en/observability/truefoundry)



##### Learn

  * [Overview](/en/learn/overview)
  * [Strategic LLM Selection Guide](/en/learn/llm-selection-guide)
  * [Conditional Tasks](/en/learn/conditional-tasks)
  * [Coding Agents](/en/learn/coding-agents)
  * [Create Custom Tools](/en/learn/create-custom-tools)
  * [Custom LLM Implementation](/en/learn/custom-llm)
  * [Custom Manager Agent](/en/learn/custom-manager-agent)
  * [Customize Agents](/en/learn/customizing-agents)
  * [Image Generation with DALL-E](/en/learn/dalle-image-generation)
  * [Force Tool Output as Result](/en/learn/force-tool-output-as-result)
  * [Hierarchical Process](/en/learn/hierarchical-process)
  * [Human Input on Execution](/en/learn/human-input-on-execution)
  * [Human-in-the-Loop (HITL) Workflows](/en/learn/human-in-the-loop)
  * [Kickoff Crew Asynchronously](/en/learn/kickoff-async)
  * [Kickoff Crew for Each](/en/learn/kickoff-for-each)
  * [Connect to any LLM](/en/learn/llm-connections)
  * [Using Multimodal Agents](/en/learn/multimodal-agents)
  * [Replay Tasks from Latest Crew Kickoff](/en/learn/replay-tasks-from-latest-crew-kickoff)
  * [Sequential Processes](/en/learn/sequential-process)
  * [Using Annotations in crew.py](/en/learn/using-annotations)
  * [Execution Hooks Overview](/en/learn/execution-hooks)
  * [LLM Call Hooks](/en/learn/llm-hooks)
  * [Tool Call Hooks](/en/learn/tool-hooks)



##### Telemetry

  * [Telemetry](/en/telemetry)



Flows

# Mastering Flow State Management

Copy page

A comprehensive guide to managing, persisting, and leveraging state in CrewAI Flows for building robust AI applications.

Copy page

## 

​

Understanding the Power of State in Flows

State management is the backbone of any sophisticated AI workflow. In CrewAI Flows, the state system allows you to maintain context, share data between steps, and build complex application logic. Mastering state management is essential for creating reliable, maintainable, and powerful AI applications. This guide will walk you through everything you need to know about managing state in CrewAI Flows, from basic concepts to advanced techniques, with practical code examples along the way.

### 

​

Why State Management Matters

Effective state management enables you to:

  1. **Maintain context across execution steps** \- Pass information seamlessly between different stages of your workflow
  2. **Build complex conditional logic** \- Make decisions based on accumulated data
  3. **Create persistent applications** \- Save and restore workflow progress
  4. **Handle errors gracefully** \- Implement recovery patterns for more robust applications
  5. **Scale your applications** \- Support complex workflows with proper data organization
  6. **Enable conversational applications** \- Store and access conversation history for context-aware AI interactions

Let’s explore how to leverage these capabilities effectively.

## 

​

State Management Fundamentals

### 

​

The Flow State Lifecycle

In CrewAI Flows, the state follows a predictable lifecycle:

  1. **Initialization** \- When a flow is created, its state is initialized (either as an empty dictionary or a Pydantic model instance)
  2. **Modification** \- Flow methods access and modify the state as they execute
  3. **Transmission** \- State is passed automatically between flow methods
  4. **Persistence** (optional) - State can be saved to storage and later retrieved
  5. **Completion** \- The final state reflects the cumulative changes from all executed methods

Understanding this lifecycle is crucial for designing effective flows.

### 

​

Two Approaches to State Management

CrewAI offers two ways to manage state in your flows:

  1. **Unstructured State** \- Using dictionary-like objects for flexibility
  2. **Structured State** \- Using Pydantic models for type safety and validation

Let’s examine each approach in detail.

## 

​

Unstructured State Management

Unstructured state uses a dictionary-like approach, offering flexibility and simplicity for straightforward applications.

### 

​

How It Works

With unstructured state:

  * You access state via `self.state` which behaves like a dictionary
  * You can freely add, modify, or remove keys at any point
  * All state is automatically available to all flow methods



### 

​

Basic Example

Here’s a simple example of unstructured state management:

Copy

Ask AI
    
    
    from crewai.flow.flow import Flow, listen, start
    
    class UnstructuredStateFlow(Flow):
        @start()
        def initialize_data(self):
            print("Initializing flow data")
            # Add key-value pairs to state
            self.state["user_name"] = "Alex"
            self.state["preferences"] = {
                "theme": "dark",
                "language": "English"
            }
            self.state["items"] = []
    
            # The flow state automatically gets a unique ID
            print(f"Flow ID: {self.state['id']}")
    
            return "Initialized"
    
        @listen(initialize_data)
        def process_data(self, previous_result):
            print(f"Previous step returned: {previous_result}")
    
            # Access and modify state
            user = self.state["user_name"]
            print(f"Processing data for {user}")
    
            # Add items to a list in state
            self.state["items"].append("item1")
            self.state["items"].append("item2")
    
            # Add a new key-value pair
            self.state["processed"] = True
    
            return "Processed"
    
        @listen(process_data)
        def generate_summary(self, previous_result):
            # Access multiple state values
            user = self.state["user_name"]
            theme = self.state["preferences"]["theme"]
            items = self.state["items"]
            processed = self.state.get("processed", False)
    
            summary = f"User {user} has {len(items)} items with {theme} theme. "
            summary += "Data is processed." if processed else "Data is not processed."
    
            return summary
    
    # Run the flow
    flow = UnstructuredStateFlow()
    result = flow.kickoff()
    print(f"Final result: {result}")
    print(f"Final state: {flow.state}")
    

### 

​

When to Use Unstructured State

Unstructured state is ideal for:

  * Quick prototyping and simple flows
  * Dynamically evolving state needs
  * Cases where the structure may not be known in advance
  * Flows with simple state requirements

While flexible, unstructured state lacks type checking and schema validation, which can lead to errors in complex applications.

## 

​

Structured State Management

Structured state uses Pydantic models to define a schema for your flow’s state, providing type safety, validation, and better developer experience.

### 

​

How It Works

With structured state:

  * You define a Pydantic model that represents your state structure
  * You pass this model type to your Flow class as a type parameter
  * You access state via `self.state`, which behaves like a Pydantic model instance
  * All fields are validated according to their defined types
  * You get IDE autocompletion and type checking support



### 

​

Basic Example

Here’s how to implement structured state management:

Copy

Ask AI
    
    
    from crewai.flow.flow import Flow, listen, start
    from pydantic import BaseModel, Field
    from typing import List, Dict, Optional
    
    # Define your state model
    class UserPreferences(BaseModel):
        theme: str = "light"
        language: str = "English"
    
    class AppState(BaseModel):
        user_name: str = ""
        preferences: UserPreferences = UserPreferences()
        items: List[str] = []
        processed: bool = False
        completion_percentage: float = 0.0
    
    # Create a flow with typed state
    class StructuredStateFlow(Flow[AppState]):
        @start()
        def initialize_data(self):
            print("Initializing flow data")
            # Set state values (type-checked)
            self.state.user_name = "Taylor"
            self.state.preferences.theme = "dark"
    
            # The ID field is automatically available
            print(f"Flow ID: {self.state.id}")
    
            return "Initialized"
    
        @listen(initialize_data)
        def process_data(self, previous_result):
            print(f"Processing data for {self.state.user_name}")
    
            # Modify state (with type checking)
            self.state.items.append("item1")
            self.state.items.append("item2")
            self.state.processed = True
            self.state.completion_percentage = 50.0
    
            return "Processed"
    
        @listen(process_data)
        def generate_summary(self, previous_result):
            # Access state (with autocompletion)
            summary = f"User {self.state.user_name} has {len(self.state.items)} items "
            summary += f"with {self.state.preferences.theme} theme. "
            summary += "Data is processed." if self.state.processed else "Data is not processed."
            summary += f" Completion: {self.state.completion_percentage}%"
    
            return summary
    
    # Run the flow
    flow = StructuredStateFlow()
    result = flow.kickoff()
    print(f"Final result: {result}")
    print(f"Final state: {flow.state}")
    

### 

​

Benefits of Structured State

Using structured state provides several advantages:

  1. **Type Safety** \- Catch type errors at development time
  2. **Self-Documentation** \- The state model clearly documents what data is available
  3. **Validation** \- Automatic validation of data types and constraints
  4. **IDE Support** \- Get autocomplete and inline documentation
  5. **Default Values** \- Easily define fallbacks for missing data



### 

​

When to Use Structured State

Structured state is recommended for:

  * Complex flows with well-defined data schemas
  * Team projects where multiple developers work on the same code
  * Applications where data validation is important
  * Flows that need to enforce specific data types and constraints



## 

​

The Automatic State ID

Both unstructured and structured states automatically receive a unique identifier (UUID) to help track and manage state instances.

### 

​

How It Works

  * For unstructured state, the ID is accessible as `self.state["id"]`
  * For structured state, the ID is accessible as `self.state.id`
  * This ID is generated automatically when the flow is created
  * The ID remains the same throughout the flow’s lifecycle
  * The ID can be used for tracking, logging, and retrieving persisted states

This UUID is particularly valuable when implementing persistence or tracking multiple flow executions.

## 

​

Dynamic State Updates

Regardless of whether you’re using structured or unstructured state, you can update state dynamically throughout your flow’s execution.

### 

​

Passing Data Between Steps

Flow methods can return values that are then passed as arguments to listening methods:

Copy

Ask AI
    
    
    from crewai.flow.flow import Flow, listen, start
    
    class DataPassingFlow(Flow):
        @start()
        def generate_data(self):
            # This return value will be passed to listening methods
            return "Generated data"
    
        @listen(generate_data)
        def process_data(self, data_from_previous_step):
            print(f"Received: {data_from_previous_step}")
            # You can modify the data and pass it along
            processed_data = f"{data_from_previous_step} - processed"
            # Also update state
            self.state["last_processed"] = processed_data
            return processed_data
    
        @listen(process_data)
        def finalize_data(self, processed_data):
            print(f"Received processed data: {processed_data}")
            # Access both the passed data and state
            last_processed = self.state.get("last_processed", "")
            return f"Final: {processed_data} (from state: {last_processed})"
    

This pattern allows you to combine direct data passing with state updates for maximum flexibility.

## 

​

Persisting Flow State

One of CrewAI’s most powerful features is the ability to persist flow state across executions. This enables workflows that can be paused, resumed, and even recovered after failures.

### 

​

The @persist() Decorator

The `@persist()` decorator automates state persistence, saving your flow’s state at key points in execution.

#### 

​

Class-Level Persistence

When applied at the class level, `@persist()` saves state after every method execution:

Copy

Ask AI
    
    
    from crewai.flow.flow import Flow, listen, start
    from crewai.flow.persistence import persist
    from pydantic import BaseModel
    
    class CounterState(BaseModel):
        value: int = 0
    
    @persist()  # Apply to the entire flow class
    class PersistentCounterFlow(Flow[CounterState]):
        @start()
        def increment(self):
            self.state.value += 1
            print(f"Incremented to {self.state.value}")
            return self.state.value
    
        @listen(increment)
        def double(self, value):
            self.state.value = value * 2
            print(f"Doubled to {self.state.value}")
            return self.state.value
    
    # First run
    flow1 = PersistentCounterFlow()
    result1 = flow1.kickoff()
    print(f"First run result: {result1}")
    
    # Second run - state is automatically loaded
    flow2 = PersistentCounterFlow()
    result2 = flow2.kickoff()
    print(f"Second run result: {result2}")  # Will be higher due to persisted state
    

#### 

​

Method-Level Persistence

For more granular control, you can apply `@persist()` to specific methods:

Copy

Ask AI
    
    
    from crewai.flow.flow import Flow, listen, start
    from crewai.flow.persistence import persist
    
    class SelectivePersistFlow(Flow):
        @start()
        def first_step(self):
            self.state["count"] = 1
            return "First step"
    
        @persist()  # Only persist after this method
        @listen(first_step)
        def important_step(self, prev_result):
            self.state["count"] += 1
            self.state["important_data"] = "This will be persisted"
            return "Important step completed"
    
        @listen(important_step)
        def final_step(self, prev_result):
            self.state["count"] += 1
            return f"Complete with count {self.state['count']}"
    

## 

​

Advanced State Patterns

### 

​

Conditional starts and resumable execution

Flows support conditional `@start()` and resumable execution for HITL/cyclic scenarios:

Copy

Ask AI
    
    
    from crewai.flow.flow import Flow, start, listen, and_, or_
    
    class ResumableFlow(Flow):
        @start()  # unconditional start
        def init(self):
            ...
    
        # Conditional start: run after "init" or external trigger name
        @start("init")
        def maybe_begin(self):
            ...
    
        @listen(and_(init, maybe_begin))
        def proceed(self):
            ...
    

  * Conditional `@start()` accepts a method name, a router label, or a callable condition.
  * During resume, listeners continue from prior checkpoints; cycle/router branches honor resumption flags.



### 

​

State-Based Conditional Logic

You can use state to implement complex conditional logic in your flows:

Copy

Ask AI
    
    
    from crewai.flow.flow import Flow, listen, router, start
    from pydantic import BaseModel
    
    class PaymentState(BaseModel):
        amount: float = 0.0
        is_approved: bool = False
        retry_count: int = 0
    
    class PaymentFlow(Flow[PaymentState]):
        @start()
        def process_payment(self):
            # Simulate payment processing
            self.state.amount = 100.0
            self.state.is_approved = self.state.amount < 1000
            return "Payment processed"
    
        @router(process_payment)
        def check_approval(self, previous_result):
            if self.state.is_approved:
                return "approved"
            elif self.state.retry_count < 3:
                return "retry"
            else:
                return "rejected"
    
        @listen("approved")
        def handle_approval(self):
            return f"Payment of ${self.state.amount} approved!"
    
        @listen("retry")
        def handle_retry(self):
            self.state.retry_count += 1
            print(f"Retrying payment (attempt {self.state.retry_count})...")
            # Could implement retry logic here
            return "Retry initiated"
    
        @listen("rejected")
        def handle_rejection(self):
            return f"Payment of ${self.state.amount} rejected after {self.state.retry_count} retries."
    

### 

​

Handling Complex State Transformations

For complex state transformations, you can create dedicated methods:

Copy

Ask AI
    
    
    from crewai.flow.flow import Flow, listen, start
    from pydantic import BaseModel
    from typing import List, Dict
    
    class UserData(BaseModel):
        name: str
        active: bool = True
        login_count: int = 0
    
    class ComplexState(BaseModel):
        users: Dict[str, UserData] = {}
        active_user_count: int = 0
    
    class TransformationFlow(Flow[ComplexState]):
        @start()
        def initialize(self):
            # Add some users
            self.add_user("alice", "Alice")
            self.add_user("bob", "Bob")
            self.add_user("charlie", "Charlie")
            return "Initialized"
    
        @listen(initialize)
        def process_users(self, _):
            # Increment login counts
            for user_id in self.state.users:
                self.increment_login(user_id)
    
            # Deactivate one user
            self.deactivate_user("bob")
    
            # Update active count
            self.update_active_count()
    
            return f"Processed {len(self.state.users)} users"
    
        # Helper methods for state transformations
        def add_user(self, user_id: str, name: str):
            self.state.users[user_id] = UserData(name=name)
            self.update_active_count()
    
        def increment_login(self, user_id: str):
            if user_id in self.state.users:
                self.state.users[user_id].login_count += 1
    
        def deactivate_user(self, user_id: str):
            if user_id in self.state.users:
                self.state.users[user_id].active = False
                self.update_active_count()
    
        def update_active_count(self):
            self.state.active_user_count = sum(
                1 for user in self.state.users.values() if user.active
            )
    

This pattern of creating helper methods keeps your flow methods clean while enabling complex state manipulations.

## 

​

State Management with Crews

One of the most powerful patterns in CrewAI is combining flow state management with crew execution.

### 

​

Passing State to Crews

You can use flow state to parameterize crews:

Copy

Ask AI
    
    
    from crewai.flow.flow import Flow, listen, start
    from crewai import Agent, Crew, Process, Task
    from pydantic import BaseModel
    
    class ResearchState(BaseModel):
        topic: str = ""
        depth: str = "medium"
        results: str = ""
    
    class ResearchFlow(Flow[ResearchState]):
        @start()
        def get_parameters(self):
            # In a real app, this might come from user input
            self.state.topic = "Artificial Intelligence Ethics"
            self.state.depth = "deep"
            return "Parameters set"
    
        @listen(get_parameters)
        def execute_research(self, _):
            # Create agents
            researcher = Agent(
                role="Research Specialist",
                goal=f"Research {self.state.topic} in {self.state.depth} detail",
                backstory="You are an expert researcher with a talent for finding accurate information."
            )
    
            writer = Agent(
                role="Content Writer",
                goal="Transform research into clear, engaging content",
                backstory="You excel at communicating complex ideas clearly and concisely."
            )
    
            # Create tasks
            research_task = Task(
                description=f"Research {self.state.topic} with {self.state.depth} analysis",
                expected_output="Comprehensive research notes in markdown format",
                agent=researcher
            )
    
            writing_task = Task(
                description=f"Create a summary on {self.state.topic} based on the research",
                expected_output="Well-written article in markdown format",
                agent=writer,
                context=[research_task]
            )
    
            # Create and run crew
            research_crew = Crew(
                agents=[researcher, writer],
                tasks=[research_task, writing_task],
                process=Process.sequential,
                verbose=True
            )
    
            # Run crew and store result in state
            result = research_crew.kickoff()
            self.state.results = result.raw
    
            return "Research completed"
    
        @listen(execute_research)
        def summarize_results(self, _):
            # Access the stored results
            result_length = len(self.state.results)
            return f"Research on {self.state.topic} completed with {result_length} characters of results."
    

### 

​

Handling Crew Outputs in State

When a crew completes, you can process its output and store it in your flow state:

Copy

Ask AI
    
    
    @listen(execute_crew)
    def process_crew_results(self, _):
        # Parse the raw results (assuming JSON output)
        import json
        try:
            results_dict = json.loads(self.state.raw_results)
            self.state.processed_results = {
                "title": results_dict.get("title", ""),
                "main_points": results_dict.get("main_points", []),
                "conclusion": results_dict.get("conclusion", "")
            }
            return "Results processed successfully"
        except json.JSONDecodeError:
            self.state.error = "Failed to parse crew results as JSON"
            return "Error processing results"
    

## 

​

Best Practices for State Management

### 

​

1\. Keep State Focused

Design your state to contain only what’s necessary:

Copy

Ask AI
    
    
    # Too broad
    class BloatedState(BaseModel):
        user_data: Dict = {}
        system_settings: Dict = {}
        temporary_calculations: List = []
        debug_info: Dict = {}
        # ...many more fields
    
    # Better: Focused state
    class FocusedState(BaseModel):
        user_id: str
        preferences: Dict[str, str]
        completion_status: Dict[str, bool]
    

### 

​

2\. Use Structured State for Complex Flows

As your flows grow in complexity, structured state becomes increasingly valuable:

Copy

Ask AI
    
    
    # Simple flow can use unstructured state
    class SimpleGreetingFlow(Flow):
        @start()
        def greet(self):
            self.state["name"] = "World"
            return f"Hello, {self.state['name']}!"
    
    # Complex flow benefits from structured state
    class UserRegistrationState(BaseModel):
        username: str
        email: str
        verification_status: bool = False
        registration_date: datetime = Field(default_factory=datetime.now)
        last_login: Optional[datetime] = None
    
    class RegistrationFlow(Flow[UserRegistrationState]):
        # Methods with strongly-typed state access
    

### 

​

3\. Document State Transitions

For complex flows, document how state changes throughout the execution:

Copy

Ask AI
    
    
    @start()
    def initialize_order(self):
        """
        Initialize order state with empty values.
    
        State before: {}
        State after: {order_id: str, items: [], status: 'new'}
        """
        self.state.order_id = str(uuid.uuid4())
        self.state.items = []
        self.state.status = "new"
        return "Order initialized"
    

### 

​

4\. Handle State Errors Gracefully

Implement error handling for state access:

Copy

Ask AI
    
    
    @listen(previous_step)
    def process_data(self, _):
        try:
            # Try to access a value that might not exist
            user_preference = self.state.preferences.get("theme", "default")
        except (AttributeError, KeyError):
            # Handle the error gracefully
            self.state.errors = self.state.get("errors", [])
            self.state.errors.append("Failed to access preferences")
            user_preference = "default"
    
        return f"Used preference: {user_preference}"
    

### 

​

5\. Use State for Progress Tracking

Leverage state to track progress in long-running flows:

Copy

Ask AI
    
    
    class ProgressTrackingFlow(Flow):
        @start()
        def initialize(self):
            self.state["total_steps"] = 3
            self.state["current_step"] = 0
            self.state["progress"] = 0.0
            self.update_progress()
            return "Initialized"
    
        def update_progress(self):
            """Helper method to calculate and update progress"""
            if self.state.get("total_steps", 0) > 0:
                self.state["progress"] = (self.state.get("current_step", 0) /
                                        self.state["total_steps"]) * 100
                print(f"Progress: {self.state['progress']:.1f}%")
    
        @listen(initialize)
        def step_one(self, _):
            # Do work...
            self.state["current_step"] = 1
            self.update_progress()
            return "Step 1 complete"
    
        # Additional steps...
    

### 

​

6\. Use Immutable Operations When Possible

Especially with structured state, prefer immutable operations for clarity:

Copy

Ask AI
    
    
    # Instead of modifying lists in place:
    self.state.items.append(new_item)  # Mutable operation
    
    # Consider creating new state:
    from pydantic import BaseModel
    from typing import List
    
    class ItemState(BaseModel):
        items: List[str] = []
    
    class ImmutableFlow(Flow[ItemState]):
        @start()
        def add_item(self):
            # Create new list with the added item
            self.state.items = [*self.state.items, "new item"]
            return "Item added"
    

## 

​

Debugging Flow State

### 

​

Logging State Changes

When developing, add logging to track state changes:

Copy

Ask AI
    
    
    import logging
    logging.basicConfig(level=logging.INFO)
    
    class LoggingFlow(Flow):
        def log_state(self, step_name):
            logging.info(f"State after {step_name}: {self.state}")
    
        @start()
        def initialize(self):
            self.state["counter"] = 0
            self.log_state("initialize")
            return "Initialized"
    
        @listen(initialize)
        def increment(self, _):
            self.state["counter"] += 1
            self.log_state("increment")
            return f"Incremented to {self.state['counter']}"
    

### 

​

State Visualization

You can add methods to visualize your state for debugging:

Copy

Ask AI
    
    
    def visualize_state(self):
        """Create a simple visualization of the current state"""
        import json
        from rich.console import Console
        from rich.panel import Panel
    
        console = Console()
    
        if hasattr(self.state, "model_dump"):
            # Pydantic v2
            state_dict = self.state.model_dump()
        elif hasattr(self.state, "dict"):
            # Pydantic v1
            state_dict = self.state.dict()
        else:
            # Unstructured state
            state_dict = dict(self.state)
    
        # Remove id for cleaner output
        if "id" in state_dict:
            state_dict.pop("id")
    
        state_json = json.dumps(state_dict, indent=2, default=str)
        console.print(Panel(state_json, title="Current Flow State"))
    

## 

​

Conclusion

Mastering state management in CrewAI Flows gives you the power to build sophisticated, robust AI applications that maintain context, make complex decisions, and deliver consistent results. Whether you choose unstructured or structured state, implementing proper state management practices will help you create flows that are maintainable, extensible, and effective at solving real-world problems. As you develop more complex flows, remember that good state management is about finding the right balance between flexibility and structure, making your code both powerful and easy to understand.

You’ve now mastered the concepts and practices of state management in CrewAI Flows! With this knowledge, you can create robust AI workflows that effectively maintain context, share data between steps, and build sophisticated application logic.

## 

​

Next Steps

  * Experiment with both structured and unstructured state in your flows
  * Try implementing state persistence for long-running workflows
  * Explore [building your first crew](/en/guides/crews/first-crew) to see how crews and flows can work together
  * Check out the [Flow reference documentation](/en/concepts/flows) for more advanced features



Was this page helpful?

YesNo

[Build Your First FlowPrevious](/en/guides/flows/first-flow)[Customizing PromptsNext](/en/guides/advanced/customizing-prompts)

Ctrl+I

[website](https://crewai.com)[x](https://x.com/crewAIInc)[github](https://github.com/crewAIInc/crewAI)[linkedin](https://www.linkedin.com/company/crewai-inc)[youtube](https://youtube.com/@crewAIInc)[reddit](https://www.reddit.com/r/crewAIInc/)

[Powered by Mintlify](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=crewai)

Assistant

Responses are generated using AI and may contain mistakes.


---

# Source: https://docs.crewai.com/en/guides/advanced/customizing-prompts

Skip to main content

[CrewAI home page![light logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)![dark logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)](/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl K

Search...

Navigation

Advanced

Customizing Prompts

[Home](/)[Documentation](/en/introduction)[AOP](/en/enterprise/introduction)[API Reference](/en/api-reference/introduction)[Examples](/en/examples/example)[Changelog](/en/changelog)

  * [Website](https://crewai.com)
  * [Forum](https://community.crewai.com)
  * [Blog](https://blog.crewai.com)
  * [CrewGPT](https://chatgpt.com/g/g-qqTuUWsBY-crewai-assistant)



##### Get Started

  * [Introduction](/en/introduction)
  * [Installation](/en/installation)
  * [Quickstart](/en/quickstart)



##### Guides

  * Strategy

  * Agents

  * Crews

  * Flows

  * Advanced

    * [Customizing Prompts](/en/guides/advanced/customizing-prompts)
    * [Fingerprinting](/en/guides/advanced/fingerprinting)



##### Core Concepts

  * [Agents](/en/concepts/agents)
  * [Tasks](/en/concepts/tasks)
  * [Crews](/en/concepts/crews)
  * [Flows](/en/concepts/flows)
  * [Knowledge](/en/concepts/knowledge)
  * [LLMs](/en/concepts/llms)
  * [Processes](/en/concepts/processes)
  * [Collaboration](/en/concepts/collaboration)
  * [Training](/en/concepts/training)
  * [Memory](/en/concepts/memory)
  * [Reasoning](/en/concepts/reasoning)
  * [Planning](/en/concepts/planning)
  * [Testing](/en/concepts/testing)
  * [CLI](/en/concepts/cli)
  * [Tools](/en/concepts/tools)
  * [Event Listeners](/en/concepts/event-listener)



##### MCP Integration

  * [MCP Servers as Tools in CrewAI](/en/mcp/overview)
  * [MCP DSL Integration](/en/mcp/dsl-integration)
  * [Stdio Transport](/en/mcp/stdio)
  * [SSE Transport](/en/mcp/sse)
  * [Streamable HTTP Transport](/en/mcp/streamable-http)
  * [Connecting to Multiple MCP Servers](/en/mcp/multiple-servers)
  * [MCP Security Considerations](/en/mcp/security)



##### Tools

  * [Tools Overview](/en/tools/overview)
  * File & Document

  * Web Scraping & Browsing

  * Search & Research

  * Database & Data

  * AI & Machine Learning

  * Cloud & Storage

  * Integrations

  * Automation




##### Observability

  * [CrewAI Tracing](/en/observability/tracing)
  * [Overview](/en/observability/overview)
  * [Arize Phoenix](/en/observability/arize-phoenix)
  * [Braintrust](/en/observability/braintrust)
  * [Datadog Integration](/en/observability/datadog)
  * [LangDB Integration](/en/observability/langdb)
  * [Langfuse Integration](/en/observability/langfuse)
  * [Langtrace Integration](/en/observability/langtrace)
  * [Maxim Integration](/en/observability/maxim)
  * [MLflow Integration](/en/observability/mlflow)
  * [Neatlogs Integration](/en/observability/neatlogs)
  * [OpenLIT Integration](/en/observability/openlit)
  * [Opik Integration](/en/observability/opik)
  * [Patronus AI Evaluation](/en/observability/patronus-evaluation)
  * [Portkey Integration](/en/observability/portkey)
  * [Weave Integration](/en/observability/weave)
  * [TrueFoundry Integration](/en/observability/truefoundry)



##### Learn

  * [Overview](/en/learn/overview)
  * [Strategic LLM Selection Guide](/en/learn/llm-selection-guide)
  * [Conditional Tasks](/en/learn/conditional-tasks)
  * [Coding Agents](/en/learn/coding-agents)
  * [Create Custom Tools](/en/learn/create-custom-tools)
  * [Custom LLM Implementation](/en/learn/custom-llm)
  * [Custom Manager Agent](/en/learn/custom-manager-agent)
  * [Customize Agents](/en/learn/customizing-agents)
  * [Image Generation with DALL-E](/en/learn/dalle-image-generation)
  * [Force Tool Output as Result](/en/learn/force-tool-output-as-result)
  * [Hierarchical Process](/en/learn/hierarchical-process)
  * [Human Input on Execution](/en/learn/human-input-on-execution)
  * [Human-in-the-Loop (HITL) Workflows](/en/learn/human-in-the-loop)
  * [Kickoff Crew Asynchronously](/en/learn/kickoff-async)
  * [Kickoff Crew for Each](/en/learn/kickoff-for-each)
  * [Connect to any LLM](/en/learn/llm-connections)
  * [Using Multimodal Agents](/en/learn/multimodal-agents)
  * [Replay Tasks from Latest Crew Kickoff](/en/learn/replay-tasks-from-latest-crew-kickoff)
  * [Sequential Processes](/en/learn/sequential-process)
  * [Using Annotations in crew.py](/en/learn/using-annotations)
  * [Execution Hooks Overview](/en/learn/execution-hooks)
  * [LLM Call Hooks](/en/learn/llm-hooks)
  * [Tool Call Hooks](/en/learn/tool-hooks)



##### Telemetry

  * [Telemetry](/en/telemetry)



Advanced

# Customizing Prompts

Copy page

Dive deeper into low-level prompt customization for CrewAI, enabling super custom and complex use cases for different models and languages.

Copy page

## 

​

Why Customize Prompts?

Although CrewAI’s default prompts work well for many scenarios, low-level customization opens the door to significantly more flexible and powerful agent behavior. Here’s why you might want to take advantage of this deeper control:

  1. **Optimize for specific LLMs** – Different models (such as GPT-4, Claude, or Llama) thrive with prompt formats tailored to their unique architectures.
  2. **Change the language** – Build agents that operate exclusively in languages beyond English, handling nuances with precision.
  3. **Specialize for complex domains** – Adapt prompts for highly specialized industries like healthcare, finance, or legal.
  4. **Adjust tone and style** – Make agents more formal, casual, creative, or analytical.
  5. **Support super custom use cases** – Utilize advanced prompt structures and formatting to meet intricate, project-specific requirements.

This guide explores how to tap into CrewAI’s prompts at a lower level, giving you fine-grained control over how agents think and interact.

## 

​

Understanding CrewAI’s Prompt System

Under the hood, CrewAI employs a modular prompt system that you can customize extensively:

  * **Agent templates** – Govern each agent’s approach to their assigned role.
  * **Prompt slices** – Control specialized behaviors such as tasks, tool usage, and output structure.
  * **Error handling** – Direct how agents respond to failures, exceptions, or timeouts.
  * **Tool-specific prompts** – Define detailed instructions for how tools are invoked or utilized.

Check out the [original prompt templates in CrewAI’s repository](https://github.com/crewAIInc/crewAI/blob/main/src/crewai/translations/en.json) to see how these elements are organized. From there, you can override or adapt them as needed to unlock advanced behaviors.

## 

​

Understanding Default System Instructions

**Production Transparency Issue** : CrewAI automatically injects default instructions into your prompts that you might not be aware of. This section explains what’s happening under the hood and how to gain full control.

When you define an agent with `role`, `goal`, and `backstory`, CrewAI automatically adds additional system instructions that control formatting and behavior. Understanding these default injections is crucial for production systems where you need full prompt transparency.

### 

​

What CrewAI Automatically Injects

Based on your agent configuration, CrewAI adds different default instructions:

#### 

​

For Agents Without Tools

Copy

Ask AI
    
    
    "I MUST use these formats, my job depends on it!"
    

#### 

​

For Agents With Tools

Copy

Ask AI
    
    
    "IMPORTANT: Use the following format in your response:
    
    Thought: you should always think about what to do
    Action: the action to take, only one name of [tool_names]
    Action Input: the input to the action, just a simple JSON object...
    

#### 

​

For Structured Outputs (JSON/Pydantic)

Copy

Ask AI
    
    
    "Ensure your final answer contains only the content in the following format: {output_format}
    Ensure the final output does not include any code block markers like ```json or ```python."
    

### 

​

Viewing the Complete System Prompt

To see exactly what prompt is being sent to your LLM, you can inspect the generated prompt:

Copy

Ask AI
    
    
    from crewai import Agent, Crew, Task
    from crewai.utilities.prompts import Prompts
    
    # Create your agent
    agent = Agent(
        role="Data Analyst",
        goal="Analyze data and provide insights",
        backstory="You are an expert data analyst with 10 years of experience.",
        verbose=True
    )
    
    # Create a sample task
    task = Task(
        description="Analyze the sales data and identify trends",
        expected_output="A detailed analysis with key insights and trends",
        agent=agent
    )
    
    # Create the prompt generator
    prompt_generator = Prompts(
        agent=agent,
        has_tools=len(agent.tools) > 0,
        use_system_prompt=agent.use_system_prompt
    )
    
    # Generate and inspect the actual prompt
    generated_prompt = prompt_generator.task_execution()
    
    # Print the complete system prompt that will be sent to the LLM
    if "system" in generated_prompt:
        print("=== SYSTEM PROMPT ===")
        print(generated_prompt["system"])
        print("\n=== USER PROMPT ===")
        print(generated_prompt["user"])
    else:
        print("=== COMPLETE PROMPT ===")
        print(generated_prompt["prompt"])
    
    # You can also see how the task description gets formatted
    print("\n=== TASK CONTEXT ===")
    print(f"Task Description: {task.description}")
    print(f"Expected Output: {task.expected_output}")
    

### 

​

Overriding Default Instructions

You have several options to gain full control over the prompts:

#### 

​

Option 1: Custom Templates (Recommended)

Copy

Ask AI
    
    
    from crewai import Agent
    
    # Define your own system template without default instructions
    custom_system_template = """You are {role}. {backstory}
    Your goal is: {goal}
    
    Respond naturally and conversationally. Focus on providing helpful, accurate information."""
    
    custom_prompt_template = """Task: {input}
    
    Please complete this task thoughtfully."""
    
    agent = Agent(
        role="Research Assistant",
        goal="Help users find accurate information",
        backstory="You are a helpful research assistant.",
        system_template=custom_system_template,
        prompt_template=custom_prompt_template,
        use_system_prompt=True  # Use separate system/user messages
    )
    

#### 

​

Option 2: Custom Prompt File

Create a `custom_prompts.json` file to override specific prompt slices:

Copy

Ask AI
    
    
    {
      "slices": {
        "no_tools": "\nProvide your best answer in a natural, conversational way.",
        "tools": "\nYou have access to these tools: {tools}\n\nUse them when helpful, but respond naturally.",
        "formatted_task_instructions": "Format your response as: {output_format}"
      }
    }
    

Then use it in your crew:

Copy

Ask AI
    
    
    crew = Crew(
        agents=[agent],
        tasks=[task],
        prompt_file="custom_prompts.json",
        verbose=True
    )
    

#### 

​

Option 3: Disable System Prompts for o1 Models

Copy

Ask AI
    
    
    agent = Agent(
        role="Analyst",
        goal="Analyze data",
        backstory="Expert analyst",
        use_system_prompt=False  # Disables system prompt separation
    )
    

### 

​

Debugging with Observability Tools

For production transparency, integrate with observability platforms to monitor all prompts and LLM interactions. This allows you to see exactly what prompts (including default instructions) are being sent to your LLMs. See our [Observability documentation](/en/observability/overview) for detailed integration guides with various platforms including Langfuse, MLflow, Weights & Biases, and custom logging solutions.

### 

​

Best Practices for Production

  1. **Always inspect generated prompts** before deploying to production
  2. **Use custom templates** when you need full control over prompt content
  3. **Integrate observability tools** for ongoing prompt monitoring (see [Observability docs](/en/observability/overview))
  4. **Test with different LLMs** as default instructions may work differently across models
  5. **Document your prompt customizations** for team transparency



The default instructions exist to ensure consistent agent behavior, but they can interfere with domain-specific requirements. Use the customization options above to maintain full control over your agent’s behavior in production systems.

## 

​

Best Practices for Managing Prompt Files

When engaging in low-level prompt customization, follow these guidelines to keep things organized and maintainable:

  1. **Keep files separate** – Store your customized prompts in dedicated JSON files outside your main codebase.
  2. **Version control** – Track changes within your repository, ensuring clear documentation of prompt adjustments over time.
  3. **Organize by model or language** – Use naming schemes like `prompts_llama.json` or `prompts_es.json` to quickly identify specialized configurations.
  4. **Document changes** – Provide comments or maintain a README detailing the purpose and scope of your customizations.
  5. **Minimize alterations** – Only override the specific slices you genuinely need to adjust, keeping default functionality intact for everything else.



## 

​

The Simplest Way to Customize Prompts

One straightforward approach is to create a JSON file for the prompts you want to override and then point your Crew at that file:

  1. Craft a JSON file with your updated prompt slices.
  2. Reference that file via the `prompt_file` parameter in your Crew.

CrewAI then merges your customizations with the defaults, so you don’t have to redefine every prompt. Here’s how:

### 

​

Example: Basic Prompt Customization

Create a `custom_prompts.json` file with the prompts you want to modify. Ensure you list all top-level prompts it should contain, not just your changes:

Copy

Ask AI
    
    
    {
      "slices": {
        "format": "When responding, follow this structure:\n\nTHOUGHTS: Your step-by-step thinking\nACTION: Any tool you're using\nRESULT: Your final answer or conclusion"
      }
    }
    

Then integrate it like so:

Copy

Ask AI
    
    
    from crewai import Agent, Crew, Task, Process
    
    # Create agents and tasks as normal
    researcher = Agent(
        role="Research Specialist",
        goal="Find information on quantum computing",
        backstory="You are a quantum physics expert",
        verbose=True
    )
    
    research_task = Task(
        description="Research quantum computing applications",
        expected_output="A summary of practical applications",
        agent=researcher
    )
    
    # Create a crew with your custom prompt file
    crew = Crew(
        agents=[researcher],
        tasks=[research_task],
        prompt_file="path/to/custom_prompts.json",
        verbose=True
    )
    
    # Run the crew
    result = crew.kickoff()
    

With these few edits, you gain low-level control over how your agents communicate and solve tasks.

## 

​

Optimizing for Specific Models

Different models thrive on differently structured prompts. Making deeper adjustments can significantly boost performance by aligning your prompts with a model’s nuances.

### 

​

Example: Llama 3.3 Prompting Template

For instance, when dealing with Meta’s Llama 3.3, deeper-level customization may reflect the recommended structure described at: <https://www.llama.com/docs/model-cards-and-prompt-formats/llama3_1/#prompt-template> Here’s an example to highlight how you might fine-tune an Agent to leverage Llama 3.3 in code:

Copy

Ask AI
    
    
    from crewai import Agent, Crew, Task, Process
    from crewai_tools import DirectoryReadTool, FileReadTool
    
    # Define templates for system, user (prompt), and assistant (response) messages
    system_template = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>{{ .System }}<|eot_id|>"""
    prompt_template = """<|start_header_id|>user<|end_header_id|>{{ .Prompt }}<|eot_id|>"""
    response_template = """<|start_header_id|>assistant<|end_header_id|>{{ .Response }}<|eot_id|>"""
    
    # Create an Agent using Llama-specific layouts
    principal_engineer = Agent(
        role="Principal Engineer",
        goal="Oversee AI architecture and make high-level decisions",
        backstory="You are the lead engineer responsible for critical AI systems",
        verbose=True,
        llm="groq/llama-3.3-70b-versatile",  # Using the Llama 3 model
        system_template=system_template,
        prompt_template=prompt_template,
        response_template=response_template,
        tools=[DirectoryReadTool(), FileReadTool()]
    )
    
    # Define a sample task
    engineering_task = Task(
        description="Review AI implementation files for potential improvements",
        expected_output="A summary of key findings and recommendations",
        agent=principal_engineer
    )
    
    # Create a Crew for the task
    llama_crew = Crew(
        agents=[principal_engineer],
        tasks=[engineering_task],
        process=Process.sequential,
        verbose=True
    )
    
    # Execute the crew
    result = llama_crew.kickoff()
    print(result.raw)
    

Through this deeper configuration, you can exercise comprehensive, low-level control over your Llama-based workflows without needing a separate JSON file.

## 

​

Conclusion

Low-level prompt customization in CrewAI opens the door to super custom, complex use cases. By establishing well-organized prompt files (or direct inline templates), you can accommodate various models, languages, and specialized domains. This level of flexibility ensures you can craft precisely the AI behavior you need, all while knowing CrewAI still provides reliable defaults when you don’t override them.

You now have the foundation for advanced prompt customizations in CrewAI. Whether you’re adapting for model-specific structures or domain-specific constraints, this low-level approach lets you shape agent interactions in highly specialized ways.

Was this page helpful?

YesNo

[Mastering Flow State ManagementPrevious](/en/guides/flows/mastering-flow-state)[FingerprintingNext](/en/guides/advanced/fingerprinting)

Ctrl+I

[website](https://crewai.com)[x](https://x.com/crewAIInc)[github](https://github.com/crewAIInc/crewAI)[linkedin](https://www.linkedin.com/company/crewai-inc)[youtube](https://youtube.com/@crewAIInc)[reddit](https://www.reddit.com/r/crewAIInc/)

[Powered by Mintlify](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=crewai)

Assistant

Responses are generated using AI and may contain mistakes.


---

# Source: https://docs.crewai.com/en/guides/advanced/fingerprinting

Skip to main content

[CrewAI home page![light logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)![dark logo](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f)](/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl K

Search...

Navigation

Advanced

Fingerprinting

[Home](/)[Documentation](/en/introduction)[AOP](/en/enterprise/introduction)[API Reference](/en/api-reference/introduction)[Examples](/en/examples/example)[Changelog](/en/changelog)

  * [Website](https://crewai.com)
  * [Forum](https://community.crewai.com)
  * [Blog](https://blog.crewai.com)
  * [CrewGPT](https://chatgpt.com/g/g-qqTuUWsBY-crewai-assistant)



##### Get Started

  * [Introduction](/en/introduction)
  * [Installation](/en/installation)
  * [Quickstart](/en/quickstart)



##### Guides

  * Strategy

  * Agents

  * Crews

  * Flows

  * Advanced

    * [Customizing Prompts](/en/guides/advanced/customizing-prompts)
    * [Fingerprinting](/en/guides/advanced/fingerprinting)



##### Core Concepts

  * [Agents](/en/concepts/agents)
  * [Tasks](/en/concepts/tasks)
  * [Crews](/en/concepts/crews)
  * [Flows](/en/concepts/flows)
  * [Knowledge](/en/concepts/knowledge)
  * [LLMs](/en/concepts/llms)
  * [Processes](/en/concepts/processes)
  * [Collaboration](/en/concepts/collaboration)
  * [Training](/en/concepts/training)
  * [Memory](/en/concepts/memory)
  * [Reasoning](/en/concepts/reasoning)
  * [Planning](/en/concepts/planning)
  * [Testing](/en/concepts/testing)
  * [CLI](/en/concepts/cli)
  * [Tools](/en/concepts/tools)
  * [Event Listeners](/en/concepts/event-listener)



##### MCP Integration

  * [MCP Servers as Tools in CrewAI](/en/mcp/overview)
  * [MCP DSL Integration](/en/mcp/dsl-integration)
  * [Stdio Transport](/en/mcp/stdio)
  * [SSE Transport](/en/mcp/sse)
  * [Streamable HTTP Transport](/en/mcp/streamable-http)
  * [Connecting to Multiple MCP Servers](/en/mcp/multiple-servers)
  * [MCP Security Considerations](/en/mcp/security)



##### Tools

  * [Tools Overview](/en/tools/overview)
  * File & Document

  * Web Scraping & Browsing

  * Search & Research

  * Database & Data

  * AI & Machine Learning

  * Cloud & Storage

  * Integrations

  * Automation




##### Observability

  * [CrewAI Tracing](/en/observability/tracing)
  * [Overview](/en/observability/overview)
  * [Arize Phoenix](/en/observability/arize-phoenix)
  * [Braintrust](/en/observability/braintrust)
  * [Datadog Integration](/en/observability/datadog)
  * [LangDB Integration](/en/observability/langdb)
  * [Langfuse Integration](/en/observability/langfuse)
  * [Langtrace Integration](/en/observability/langtrace)
  * [Maxim Integration](/en/observability/maxim)
  * [MLflow Integration](/en/observability/mlflow)
  * [Neatlogs Integration](/en/observability/neatlogs)
  * [OpenLIT Integration](/en/observability/openlit)
  * [Opik Integration](/en/observability/opik)
  * [Patronus AI Evaluation](/en/observability/patronus-evaluation)
  * [Portkey Integration](/en/observability/portkey)
  * [Weave Integration](/en/observability/weave)
  * [TrueFoundry Integration](/en/observability/truefoundry)



##### Learn

  * [Overview](/en/learn/overview)
  * [Strategic LLM Selection Guide](/en/learn/llm-selection-guide)
  * [Conditional Tasks](/en/learn/conditional-tasks)
  * [Coding Agents](/en/learn/coding-agents)
  * [Create Custom Tools](/en/learn/create-custom-tools)
  * [Custom LLM Implementation](/en/learn/custom-llm)
  * [Custom Manager Agent](/en/learn/custom-manager-agent)
  * [Customize Agents](/en/learn/customizing-agents)
  * [Image Generation with DALL-E](/en/learn/dalle-image-generation)
  * [Force Tool Output as Result](/en/learn/force-tool-output-as-result)
  * [Hierarchical Process](/en/learn/hierarchical-process)
  * [Human Input on Execution](/en/learn/human-input-on-execution)
  * [Human-in-the-Loop (HITL) Workflows](/en/learn/human-in-the-loop)
  * [Kickoff Crew Asynchronously](/en/learn/kickoff-async)
  * [Kickoff Crew for Each](/en/learn/kickoff-for-each)
  * [Connect to any LLM](/en/learn/llm-connections)
  * [Using Multimodal Agents](/en/learn/multimodal-agents)
  * [Replay Tasks from Latest Crew Kickoff](/en/learn/replay-tasks-from-latest-crew-kickoff)
  * [Sequential Processes](/en/learn/sequential-process)
  * [Using Annotations in crew.py](/en/learn/using-annotations)
  * [Execution Hooks Overview](/en/learn/execution-hooks)
  * [LLM Call Hooks](/en/learn/llm-hooks)
  * [Tool Call Hooks](/en/learn/tool-hooks)



##### Telemetry

  * [Telemetry](/en/telemetry)



Advanced

# Fingerprinting

Copy page

Learn how to use CrewAI’s fingerprinting system to uniquely identify and track components throughout their lifecycle.

Copy page

## 

​

Overview

Fingerprints in CrewAI provide a way to uniquely identify and track components throughout their lifecycle. Each `Agent`, `Crew`, and `Task` automatically receives a unique fingerprint when created, which cannot be manually overridden. These fingerprints can be used for:

  * Auditing and tracking component usage
  * Ensuring component identity integrity
  * Attaching metadata to components
  * Creating a traceable chain of operations



## 

​

How Fingerprints Work

A fingerprint is an instance of the `Fingerprint` class from the `crewai.security` module. Each fingerprint contains:

  * A UUID string: A unique identifier for the component that is automatically generated and cannot be manually set
  * A creation timestamp: When the fingerprint was generated, automatically set and cannot be manually modified
  * Metadata: A dictionary of additional information that can be customized

Fingerprints are automatically generated and assigned when a component is created. Each component exposes its fingerprint through a read-only property.

## 

​

Basic Usage

### 

​

Accessing Fingerprints

Copy

Ask AI
    
    
    from crewai import Agent, Crew, Task
    
    # Create components - fingerprints are automatically generated
    agent = Agent(
        role="Data Scientist",
        goal="Analyze data",
        backstory="Expert in data analysis"
    )
    
    crew = Crew(
        agents=[agent],
        tasks=[]
    )
    
    task = Task(
        description="Analyze customer data",
        expected_output="Insights from data analysis",
        agent=agent
    )
    
    # Access the fingerprints
    agent_fingerprint = agent.fingerprint
    crew_fingerprint = crew.fingerprint
    task_fingerprint = task.fingerprint
    
    # Print the UUID strings
    print(f"Agent fingerprint: {agent_fingerprint.uuid_str}")
    print(f"Crew fingerprint: {crew_fingerprint.uuid_str}")
    print(f"Task fingerprint: {task_fingerprint.uuid_str}")
    

### 

​

Working with Fingerprint Metadata

You can add metadata to fingerprints for additional context:

Copy

Ask AI
    
    
    # Add metadata to the agent's fingerprint
    agent.security_config.fingerprint.metadata = {
        "version": "1.0",
        "department": "Data Science",
        "project": "Customer Analysis"
    }
    
    # Access the metadata
    print(f"Agent metadata: {agent.fingerprint.metadata}")
    

## 

​

Fingerprint Persistence

Fingerprints are designed to persist and remain unchanged throughout a component’s lifecycle. If you modify a component, the fingerprint remains the same:

Copy

Ask AI
    
    
    original_fingerprint = agent.fingerprint.uuid_str
    
    # Modify the agent
    agent.goal = "New goal for analysis"
    
    # The fingerprint remains unchanged
    assert agent.fingerprint.uuid_str == original_fingerprint
    

## 

​

Deterministic Fingerprints

While you cannot directly set the UUID and creation timestamp, you can create deterministic fingerprints using the `generate` method with a seed:

Copy

Ask AI
    
    
    from crewai.security import Fingerprint
    
    # Create a deterministic fingerprint using a seed string
    deterministic_fingerprint = Fingerprint.generate(seed="my-agent-id")
    
    # The same seed always produces the same fingerprint
    same_fingerprint = Fingerprint.generate(seed="my-agent-id")
    assert deterministic_fingerprint.uuid_str == same_fingerprint.uuid_str
    
    # You can also set metadata
    custom_fingerprint = Fingerprint.generate(
        seed="my-agent-id",
        metadata={"version": "1.0"}
    )
    

## 

​

Advanced Usage

### 

​

Fingerprint Structure

Each fingerprint has the following structure:

Copy

Ask AI
    
    
    from crewai.security import Fingerprint
    
    fingerprint = agent.fingerprint
    
    # UUID string - the unique identifier (auto-generated)
    uuid_str = fingerprint.uuid_str  # e.g., "123e4567-e89b-12d3-a456-426614174000"
    
    # Creation timestamp (auto-generated)
    created_at = fingerprint.created_at  # A datetime object
    
    # Metadata - for additional information (can be customized)
    metadata = fingerprint.metadata  # A dictionary, defaults to {}
    

Was this page helpful?

YesNo

[Customizing PromptsPrevious](/en/guides/advanced/customizing-prompts)[AgentsNext](/en/concepts/agents)

Ctrl+I

[website](https://crewai.com)[x](https://x.com/crewAIInc)[github](https://github.com/crewAIInc/crewAI)[linkedin](https://www.linkedin.com/company/crewai-inc)[youtube](https://youtube.com/@crewAIInc)[reddit](https://www.reddit.com/r/crewAIInc/)

[Powered by Mintlify](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=crewai)

Assistant

Responses are generated using AI and may contain mistakes.


---