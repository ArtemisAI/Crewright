# Language Analysis for Stealth Bridge

## Summary
For this specific project (CrewAI + Chrome Extension Bridge), **Python** is valid for cohesion, but **TypeScript (Node.js)** is technically superior for the bridge component due to its native handling of WebSockets and async operations. **Rust/Go** are excellent for performance but introduce unnecessary complexity for this scale.

## Comparison

### 1. Python (Current Choice)
*   **Pros**:
    *   **Unified Stack**: CrewAI is Python; implementing the bridge in Python keeps the codebase in one language.
    *   **Simplifies Dev**: User only needs `pip install`. No need for `npm`, `cargo`, etc.
*   **Cons**:
    *   **Concurrency**: Python's `asyncio` + `threading` (GIL) can be flaky on Windows (as seen with the Stdio issues).
    *   **WebSockets**: Not as "native" as in Node.js.

### 2. TypeScript / Node.js (Recommended Alternative)
*   **Pros**:
    *   **Best for I/O**: Node.js was built for exactly this: keeping many WebSocket connections open and passing JSON messages.
    *   **Stability**: `stdio` in Node.js is rock-solid on all platforms.
    *   **Extension Synergy**: The Chrome Extension is already JS; writing the server in JS reduces context switching.
*   **Cons**:
    *   **Toolchain**: Requires user to have `Node.js` installed.
    *   **Integration**: CrewAI needs to call `command="node", args=["server.js"]`.

### 3. Rust / Go (Performant Alternative)
*   **Pros**:
    *   **Single Binary**: You can compile the bridge to a `.exe`. Zero dependencies for the user.
    *   **Speed**: Extremely fast, low memory footprint.
*   **Cons**:
    *   **Development Speed**: Slower to iterate than Python/JS.
    *   **Overkill**: We are just passing text messages; infinite scale is not a requirement.

## Conclusion
We are sticking with **Python** to keep the user's setup simple (one `pip install`), but we are pivoting to **HTTP/SSE** to bypass the Python Stdio instability on Windows.
