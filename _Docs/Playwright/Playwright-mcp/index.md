# Playwright MCP Documentation Index

This folder contains organized documentation and analysis of the **Microsoft Playwright MCP** project.

## Core Documentation
- **[README](./README.md)**: The official project overview, installation guide, and usage instructions. (Fetched from repo)
- **[package.json](./package.json)**: Dependency and script definitions.

## Analysis & Reports
- **[Timeline](./timeline.md)**: Chronological history of releases and key events.
- **[Code Analysis](./code_analysis.md)**: Technical deep-dive into the repository structure, specifically the Chrome Extension architecture and the wrapper design.
- **[Evolution](./evolution.md)**: Analysis of how the project and its architecture have changed over time.

## Missing Data
> **Note**: `issues.md` and detailed `releases.md` (changelogs) were not available in the source repository. The timeline was reconstructed from git tags.

## Project Summary
The **Playwright MCP** server enables AI agents to control web browsers. It uses a "wrapper" architecture where this repository provides the CLI and a Chrome Extension, while the heavy lifting is done by the core `playwright` library.

### Key Components
1.  **MCP Server**: Exposes browser control tools to LLMs.
2.  **Chrome Extension**: Bridges the server to *existing* browser windows via WebSocket.
3.  **Docker Image**: Provides a sandboxed environment for safe execution.
