# Crewright Roadmap

## Phase 1: Core Stability (Current)
- [x] **Parasitic Bridge**: Stable WebSocket connection between Agent and Extension.
- [x] **Basic Tools**: `navigate`, `get_page_content`, `click_element`, `type_text`.
- [x] **Detection Evasion**: Inherit user session (cookies/storage).

## Phase 2: Enhanced Interactivity (Complete)
- [x] **Screenshot**: `screenshot()` - Capture visual state (Base64).
- [x] **Hover**: `hover(selector)` - Trigger dropdowns/tooltips.
- [x] **Key Press**: `press(key)` - Interact with specialized inputs (Enter, Esc, Arrows).
- [x] **Execute Script**: `evaluate(expression)` - Run custom JS extraction.
- [x] **Scroll**: `scroll(direction)` - Handle infinite feeds.

## Phase 3: Robustness & Alignment (Current)
- [ ] **Playwright Alignment**: Rename tools (`click`, `fill`, `press`, `evaluate`).
- [x] **Robust Testing**: Handle latency and wait conditions.
- [x] **Model Benchmarking**: Test with local LLMs (Mistral/Kimi) - *Deferred (Ollama Env)*
- [x] **Efficiency Optimization**: Implement "Macro" tools (bulk actions) and investigate Flow-based batching.
- [x] **Browser Strategy Analysis**: Document pros/cons of ChromeTools vs Playwright vs Browser-Use.

## Phase 4: Headless "Theft"
- [ ] **Cookie Export**: `get_cookies()` - Steal auth tokens for HTTP requests.
- [ ] **DOM Observer**: Push updates to agent when page changes (MutationObserver).
- [ ] **Visual Debugger**: Real-time highlighting of elements the agent is "looking" at.

## Phase 4: Enterprise
- [ ] **RBAC**: Allowlist/Blocklist specific domains the agent can access.
- [ ] **Audit Logs**: Record every click and keystroke for compliance.
