# Crewight Roadmap

## Phase 1: Core Stability (Current)
- [x] **Parasitic Bridge**: Stable WebSocket connection between Agent and Extension.
- [x] **Basic Tools**: `navigate`, `get_page_content`, `click_element`, `type_text`.
- [x] **Detection Evasion**: Inherit user session (cookies/storage).

## Phase 2: Enhanced Interactivity (Next)
- [ ] **Element Highlighting**: When the agent "looks" at an element (selector), highlight it in Red for the user to see.
- [ ] **Multi-Tab Support**: Allow agent to open/close tabs and switch context `switch_tab(tab_id)`.
- [ ] **Visual Debugger**: A sidebar in the Extension showing the Agent's "Thought Process".

## Phase 3: Headless "Theft"
- [ ] **Cookie Export**: Tool to extract cookies from the Extension and "hand off" to a headless Playwright instance for background processing.
- [ ] **Session Cloning**: Replicate the browser state to a Docker container.

## Phase 4: Enterprise
- [ ] **RBAC**: Allowlist/Blocklist specific domains the agent can access.
- [ ] **Audit Logs**: Record every click and keystroke for compliance.
