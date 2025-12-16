# Agent Efficiency & Cost Optimization

## The ReAct Loop Cost
In standard agent frameworks (CrewAI, LangChain), the execution model is typically:
1.  **Thought (LLM Call)**: The model reasons about what to do.
2.  **Action (Tool Call)**: The model generates a tool call (e.g., `click(selector)`).
3.  **Observation (Tool Output)**: The system executes the tool and feeds the result back to the model.
4.  **Repeat**.

**Implication**: Every single action (click, type, scroll) incurs an LLM API cost and latency.

## Optimization Strategies

### 1. "Macro" Tools (The Playwright Way)
Instead of 5 separate calls (`click`, `wait`, `type`, `wait`, `click`), use **one** powerful call that does it all.
*   **Tool**: `evaluate(expression)`
*   **Concept**: Send a block of JavaScript to the browser to execute multiple actions on the client side.
*   **Efficiency**: 1 LLM Call -> N Browser Actions.

**Example**:
```javascript
// Instead of 3 agent steps, run this once:
document.querySelector('#search').value = 'CrewAI';
document.querySelector('#submit').click();
```

### 2. CrewAI Flows (Batching)
Use **Flows** to chain tasks deterministically where "thinking" isn't required.
*   **Pattern**: Task 1 (Planning) decides the high-level goal -> Task 2 (Execution) runs a script.
*   **Training**: You can "train" the Crew to prefer specific efficient paths or tools.

### 3. Playwright-MCP Alignment
The official `playwright-mcp` encourages robust selectors and occasional `evaluate` for complex state extraction, but generally relies on the LLM's speed.
*   **Recommendation**: Use `evaluate` for scraping dense data (to avoid sending raw HTML back and forth).
*   **Recommendation**: Use specific selectors to avoid "retry" loops.

## Streaming
Streaming reduces *perceived* latency for the user but does not reduce token cost. CrewAI supports streaming for text output, and our Bridge supports partial updates via logs, but the tool execution itself is atomic.
