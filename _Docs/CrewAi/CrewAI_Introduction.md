# Introduction

Build AI agent teams that work together to tackle complex tasks

## What is CrewAI?

CrewAI is a lean, lightning-fast Python framework built entirely from scratch—completely independent of LangChain or other agent frameworks.

CrewAI empowers developers with both high-level simplicity and precise low-level control, ideal for creating autonomous AI agents tailored to any scenario:

- **CrewAI Crews**: Optimize for autonomy and collaborative intelligence, enabling you to create AI teams where each agent has specific roles, tools, and goals.
- **CrewAI Flows**: Enable granular, event-driven control, single LLM calls for precise task orchestration and supports Crews natively.

With over 100,000 developers certified through our community courses, CrewAI is rapidly becoming the standard for enterprise-ready AI automation.

## How Crews Work

Just like a company has departments (Sales, Engineering, Marketing) working together under leadership to achieve business goals, CrewAI helps you create an organization of AI agents with specialized roles collaborating to accomplish complex tasks.

![CrewAI Framework Overview](https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3ef573e6215967af1bb2975a58d0d859)

| Component | Description |
|-----------|-------------|
| Crew | The top-level organization that manages AI agent teams, oversees workflows, ensures collaboration, and delivers outcomes |
| AI Agents | Specialized team members with specific roles (researcher, writer), designated tools, delegation capabilities, and autonomous decision-making |
| Process | Workflow management system that defines collaboration patterns, controls task assignments, manages interactions, and ensures efficient execution |
| Tasks | Individual assignments with clear objectives, specific tools, workflow integration, and actionable results |

### How It All Works Together

1. The Crew organizes the overall operation
2. AI Agents work on their specialized tasks
3. The Process ensures smooth collaboration
4. Tasks get completed to achieve the goal

## Key Features

### Role-Based Agents

Create specialized agents with defined roles, expertise, and goals - from researchers to analysts to writers

### Flexible Tools

Equip agents with custom tools and APIs to interact with external services and data sources

### Intelligent Collaboration

Agents work together, sharing insights and coordinating tasks to achieve complex objectives

### Task Management

Define sequential or parallel workflows, with agents automatically handling task dependencies

## How Flows Work

While Crews excel at autonomous collaboration, Flows provide structured automations, offering granular control over workflow execution. Flows ensure tasks are executed reliably, securely, and efficiently, handling conditional logic, loops, and dynamic state management with precision. Flows integrate seamlessly with Crews, enabling you to balance high autonomy with exacting control.

![CrewAI Framework Overview](https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=a83fa78165e93bc1d988a30ebc33889a)

| Component | Description |
|-----------|-------------|
| Flow | Structured workflow orchestration that manages execution paths, handles state transitions, controls task sequencing, and ensures reliable execution |
| Events | Triggers for workflow actions that initiate specific processes, enable dynamic responses, support conditional branching, and allow for real-time adaptation |
| States | Workflow execution contexts that maintain execution data, enable persistence, support resumability, and ensure execution integrity |
| Crew Support | Enhances workflow automation by injecting pockets of agency when needed, complements structured workflows, balances automation with intelligence, and enables adaptive decision-making |

### Key Capabilities

### Event-Driven Orchestration

Define precise execution paths responding dynamically to events

### Fine-Grained Control

Manage workflow states and conditional execution securely and efficiently

### Native Crew Integration

Effortlessly combine with Crews for enhanced autonomy and intelligence

### Deterministic Execution

Ensure predictable outcomes with explicit control flow and error handling

## When to Use Crews vs. Flows

Understanding when to use Crews versus Flows is key to maximizing the potential of CrewAI in your applications.

| Scenario | Recommended Approach | Reason |
|----------|----------------------|--------|
| Open-ended research | Crews | When tasks require creative thinking, exploration, and adaptation |
| Content generation | Crews | For collaborative creation of articles, reports, or marketing materials |
| Decision workflows | Flows | When you need predictable, auditable decision paths with precise control |
| API orchestration | Flows | For reliable integration with multiple external services in a specific sequence |
| Hybrid applications | Combined approach | Use Flows to orchestrate overall process with Crews handling complex subtasks |

### Decision Framework

Choose **Crews** when: You need autonomous problem-solving, creative collaboration, or exploratory tasks

Choose **Flows** when: You require deterministic outcomes, auditability, or precise control over execution

Combine both when: Your application needs both structured processes and pockets of autonomous intelligence

## Why Choose CrewAI?

- 🧠 **Autonomous Operation**: Agents make intelligent decisions based on their roles and available tools
- 📝 **Natural Interaction**: Agents communicate and collaborate like human team members
- 🛠️ **Extensible Design**: Easy to add new tools, roles, and capabilities
- 🚀 **Production Ready**: Built for reliability and scalability in real-world applications
- 🔒 **Security-Focused**: Designed with enterprise security requirements in mind
- 💰 **Cost-Efficient**: Optimized to minimize token usage and API calls

## Ready to Start Building?

- **[Build Your First Crew](https://docs.crewai.com/en/guides/crews/first-crew)**: Step-by-step tutorial to create a collaborative AI team that works together to solve complex problems
- **[Build Your First Flow](https://docs.crewai.com/en/guides/flows/first-flow)**: Learn how to create structured, event-driven workflows with precise control over execution
- **[Install CrewAI](https://docs.crewai.com/en/installation)**: Get started with CrewAI in your development environment
- **[Quick Start](https://docs.crewai.com/en/quickstart)**: Follow our quickstart guide to create your first CrewAI agent and get hands-on experience
- **[Join the Community](https://community.crewai.com/)**: Connect with other developers, get help, and share your CrewAI experiences