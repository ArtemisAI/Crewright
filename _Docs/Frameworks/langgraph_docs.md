# LangGraph Documentation

## Overview
LangGraph is a library for building stateful, multi-actor applications with LLMs, used to create agent and multi-agent workflows.

## Install
```bash
pip install -U langgraph
```

## Core Benefits
1. **Durable Execution**: Build agents that persist through failures and resume.
2. **Human-in-the-loop**: Incorporate human oversight to inspect and modify state.
3. **Comprehensive Memory**: Manage short-term and long-term memory.
4. **Debugging with LangSmith**: Trace execution paths and capture state transitions.
5. **Production-ready Deployment**: Deploy scalable agent systems.

## Basic Example
```python
from langgraph.graph import StateGraph, MessagesState, START, END

def mock_llm(state: MessagesState):
    return {"messages": [{"role": "ai", "content": "hello world"}]}

graph = StateGraph(MessagesState)
graph.add_node(mock_llm)
graph.add_edge(START, "mock_llm")
graph.add_edge("mock_llm", END)
graph = graph.compile()
graph.invoke({"messages": [{"role": "user", "content": "hi!"}]})
```

[Source: https://docs.langchain.com/oss/python/langgraph/overview]
