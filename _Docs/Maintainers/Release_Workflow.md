# 🚀 Crewright Development & Release Workflow

**Audience**: Maintainers & Core Contributors
**Goal**: Ensure quality, stability, and "Zero Broken Releases" on NPM.

---

## 1. 🛠️ Loop 1: Local Development (The "Grind")
*Work hard locally. Break things here, not in production.*

*   **Code Location**: `src/bridge/` (TypeScript), `src/agents/` (Python Agents)
*   **Watch Mode**:
    ```bash
    cd src/bridge
    npm run watch  # Recompiles TS on save
    ```
*   **Dev Testing**:
    *   Use `tests/bridge_dev_server.py` to point agents at your *local* `src/bridge/dist/index.js` (dev artifact).
    *   Run `python src/agents/test_agent_robust.py` frequently.
*   **Validation Rule**: Do not proceed until `test_agent_robust.py` passes the "Google Navigation -> Fill -> Press" flow reliably.

## 2. 💾 Loop 2: Commit to GitHub
*Sync with the team. Code must be clean.*

*   **Pre-Commit Check**:
    *   **Secrets**: Ensure no `.env` or keys are in `git status`.
    *   **Cleanup**: Remove temp scripts unless moved to `tests/`.
    *   **Docs**: Update `Progress.md` and `Issues.md` if you fixed/found bugs.
*   **Commit**:
    ```bash
    git add .
    git commit -m "feat: description of changes"
    git push
    ```

## 3. 🏗️ Loop 3: Build & Release Verification (The "Gatekeeper")
*The Critical Step. Never publish what you haven't run.*

### A. Fresh Build
Ensure you are testing the **exact artifact** that will go to NPM.
```bash
cd src/bridge
rm -rf dist/       # Clean old build
npm install        # Clean deps
npm run build      # Production Compile
```

### B. Artifact Verification
Do not trust `npm run watch` artifacts. Test the `dist/` folder explicitly.
1.  **Version Check**: Ensure `package.json` version is bumped (e.g., `1.0.1`).
2.  **Run Verification Script**:
    Use a dedicated script like `tests/verify_pkg_v1.0.1.py` that loads `dist/index.js`.
    ```bash
    python tests/verify_pkg_v1_0_1.py
    ```
    *   **Success Criteria**: Script must verify the *Package Version* matches the *Directory* and successfully execute a tool call (e.g., `navigate` to `https://www.google.com`).
    *   *Tip*: Use resilient targets like Google.com to avoid false negatives from test-site downtime.

## 4. 📦 Loop 4: Publication (Review & Push)
*Go live.*

*   **Final Sanity Check**:
    ```bash
    npm pack --dry-run  # See exactly what files will be verified
    ```
    *   *Check*: Does it include `dist/`? Does it exclude `src/` (if desired) and `tests/`?
*   **Publish**:
    ```bash
    npm login
    npm publish --access public
    ```
*   **Post-Release**:
    *   Tag the release in Git: `git tag v1.0.1 && git push --tags`.
    *   Update `CHANGELOG.md`.

---

## 🧪 Testing Policy

| Level | Script | Frequency |
| :--- | :--- | :--- |
| **Unit/Dev** | `test_agent_robust.py` | *Daily* / Before Commit |
| **Build Integrity** | `tests/verify_pkg_v*.py` | *Mandatory* Before Publish |
| **End-to-End** | `npx @crew-ai/crewright` | *Post-Publish* Sanity Check |

> **Golden Rule**: If the `verify_pkg` script fails, **DO NOT PUBLISH**. Fix the build, not the test.
> **A/B Consistency**: Ensure `test_release` (NPX) and `verify_pkg` (Local Build) use identical logic/targets to guarantee the artifact behaves exactly as the published package will.
