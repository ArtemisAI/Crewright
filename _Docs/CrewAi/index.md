# CrewAI Documentation Index

This directory contains comprehensive documentation for CrewAI, a powerful framework for building and orchestrating AI agents. The documentation is organized into logical sections covering all aspects of CrewAI from basic concepts to advanced integrations.

## 📚 Documentation Overview

CrewAI is a Python framework that enables you to create, manage, and orchestrate AI agents that can work together to accomplish complex tasks. This documentation provides everything you need to get started and build sophisticated multi-agent systems.

---

## 🚀 Getting Started

### [CrewAI Introduction](CrewAI_Introduction.md)
- Overview of CrewAI framework and concepts
- Understanding crews vs flows
- Key features and capabilities
- When to use CrewAI

### [CrewAI Installation](CrewAI_Installation.md)
- Installation with uv package manager
- Project scaffolding and setup
- Enterprise deployment options
- Requirements and dependencies

### [CrewAI Quickstart](CrewAI_Quickstart.md)
- Build your first AI agent in under 5 minutes
- Complete example with research and reporting agents
- Step-by-step tutorial with code examples
- Deployment options (including CrewAI AOP)

### [CrewAI AOP (Agent Operations Platform)](CrewAI_AOP.md)
- Enterprise platform for production deployments
- Crew deployment, monitoring, and scaling
- Automation triggers and integrations
- API access and webhook streaming
- Crew Studio no-code interface

---

## 🏗️ Core Concepts

### [Agents](CrewAI_Agents.md)
- What are agents and how they work
- Agent configuration and parameters
- Built-in tools and custom tool creation
- Agent memory, delegation, and caching
- Best practices for agent design

### [Tasks](CrewAI_Tasks.md)
- Task creation and configuration
- Dependencies and context management
- Output handling (files, JSON, Pydantic)
- Callbacks and human input
- Task execution patterns and best practices

### [Tools Overview](CrewAI_Tools_Overview.md)
- Built-in tools (SerperDev, ScrapeWebsite, FileRead, etc.)
- Custom tool development
- Tool integration with agents
- Tool categories and use cases
- Performance optimization and security

### [Web Scraping & Browsing Tools](Web_Scraping/index.md)
- Comprehensive guide to all scraping tools
- Basic content extraction (ScrapeWebsiteTool, ScrapeElementFromWebsiteTool)
- Advanced scraping services (Firecrawl, ScrapFly, ScrapeGraph)
- Browser automation (Selenium, BrowserBase, Hyperbrowser, Stagehand)
- Enterprise scrapers (Oxylabs, Bright Data)
- Tool selection guide and best practices

### [Observability](../Observability/index.md)
- Monitoring and tracing for CrewAI agents
- Built-in tracing with CrewAI AOP platform
- Third-party observability tools integration
- Performance metrics and debugging
- Quality assurance and evaluation platforms

### [Flows](CrewAI_Flows.md)
- Dynamic workflow orchestration
- Conditional logic and loops
- Flow vs Crew comparison
- State management and event handling
- Advanced patterns and best practices

---

## 🔗 MCP Integration

CrewAI supports the Model Context Protocol (MCP) for seamless integration with external tools and services.

### [MCP Servers Overview](../MCP_Servers.md)
- Introduction to MCP in CrewAI
- Server types and use cases
- Configuration examples
- Security considerations

### [DSL Integration](MCP_DSL_Integration.md)
- MCP configuration in YAML
- Server definition and parameters
- Multiple transport types
- Advanced configuration patterns

### Transport Protocols

#### [Stdio Transport](MCP_Stdio_Transport.md)
- Process-based communication
- Local MCP server integration
- Security and isolation
- Custom server development

#### [SSE Transport](MCP_SSE_Transport.md)
- Real-time event streaming
- Server-Sent Events implementation
- Connection management and reconnection
- Event filtering and processing

#### [Streamable HTTP Transport](MCP_Streamable_HTTP_Transport.md)
- Request-response communication
- HTTP API integration
- Streaming support
- Authentication and security

---

## 📖 Additional Resources

### [CrewAI Repositories](CrewAI_Repos.md)
- Official CrewAI repositories
- Community projects and examples
- Related tools and integrations

### Legacy Documentation
- [CrewAI Docs](crewai_docs.md) - Original documentation
- [CrewAI Full Docs](crewai_full_docs.md) - Comprehensive reference

---


## 🗂️ Directory Structure


```
CrewAi/
├── 📄 CrewAI_Introduction.md          # Framework overview
├── 📄 CrewAI_Installation.md          # Setup and installation
├── 📄 CrewAI_Quickstart.md            # Getting started tutorial
├── 📄 CrewAI_AOP.md                   # Enterprise platform documentation
├── 📄 CrewAI_Agents.md                # Agent concepts and usage
├── 📄 CrewAI_Tasks.md                 # Task management
├── 📄 CrewAI_Tools_Overview.md        # Tools and integrations
├── 📁 Web_Scraping/                   # Web scraping tools documentation
│   └── ...                            # (see Web_Scraping/index.md)
├── 📁 Observability/                  # Observability and tracing
│   └── ...                            # (see Observability/index.md)
├── 📁 MCP/                            # MCP integration guides
│   └── ...                            # (see MCP_DSL_Integration.md)
├── 📁 Advanced/                       # Advanced patterns and use cases
│   ├── 📄 index.md                    # Advanced docs index
│   ├── 📄 CrewAI_Use_Cases_Evaluation.md   # Use cases & evaluation
│   ├── 📄 CrewAI_Advanced_Patterns.md      # Advanced patterns & best practices
│   ├── 📄 CrewAI_Error_Handling.md         # (Planned) Error handling
│   ├── 📄 CrewAI_Performance_Optimization.md # (Planned) Performance optimization
│   └── 📄 CrewAI_Testing_Frameworks.md     # (Planned) Testing frameworks
├── 📁 Enterprise/                     # (Planned) Enterprise features and guides
│   ├── 📄 index.md                    # Enterprise docs index (planned)
│   ├── 📄 CrewAI_Production_Deployment.md  # (Planned) Deployment guide
│   ├── 📄 CrewAI_Team_Collaboration.md     # (Planned) Team collaboration
│   └── 📄 CrewAI_Security_Guide.md         # (Planned) Security & compliance
├── 📄 CrewAI_Flows.md                 # Dynamic workflows
├── 📄 MCP_DSL_Integration.md          # MCP configuration
├── 📄 MCP_Stdio_Transport.md          # Local MCP servers
├── 📄 MCP_SSE_Transport.md            # Real-time MCP
├── 📄 MCP_Streamable_HTTP_Transport.md # HTTP-based MCP
├── 📄 CrewAI_Repos.md                 # Repository references
├── 📄 crewai_docs.md                  # Legacy docs
└── 📄 crewai_full_docs.md             # Full documentation
```

---


## 🎯 Quick Navigation

| I want to... | Start here |
|--------------|------------|
| Get started with CrewAI | [Quickstart](CrewAI_Quickstart.md) |
| Understand core concepts | [Introduction](CrewAI_Introduction.md) |
| Build my first agent | [Agents](CrewAI_Agents.md) + [Tasks](CrewAI_Tasks.md) |
| Add external tools | [Tools Overview](CrewAI_Tools_Overview.md) |
| Scrape websites | [Web Scraping Tools](Web_Scraping/index.md) |
| Monitor agent performance | [Observability](../Observability/index.md) |
| Create complex workflows | [Flows](CrewAI_Flows.md) |
| Integrate MCP servers | [DSL Integration](MCP_DSL_Integration.md) |
| Explore advanced patterns | [Advanced Docs](Advanced/index.md) |
| Deploy to production | [CrewAI AOP](CrewAI_AOP.md) |
| Use enterprise features | [Enterprise Docs](Enterprise/index.md) *(coming soon)* |
| Set up development environment | [Installation](CrewAI_Installation.md) |

---

## 📋 Prerequisites

Before diving into CrewAI, ensure you have:

- **Python 3.8+** installed
- **uv package manager** (recommended) or pip
- **API keys** for LLM providers (OpenAI, Anthropic, etc.)
- **Basic understanding** of AI agents and orchestration concepts

---

## 🤝 Contributing

This documentation is maintained as part of the LinkedAI project. To contribute:

1. Follow the project's documentation standards
2. Update this index when adding new documents
3. Ensure cross-references are accurate
4. Test all links and examples

---

## 📞 Support

- **CrewAI Official Docs**: https://docs.crewai.com
- **CrewAI Community**: https://community.crewai.com
- **CrewAI AOP**: https://app.crewai.com (Enterprise platform)

---

*Last updated: December 15, 2025*

---

## 🔍 Search Tips

- Use your editor's search function (Ctrl+F/Cmd+F) to find specific topics
- Check the table of contents in each document for detailed sections
- Code examples are highlighted and runnable
- Configuration examples include both YAML and Python formats

---

**Ready to build your first CrewAI agent? Start with the [Quickstart Guide](CrewAI_Quickstart.md)!**