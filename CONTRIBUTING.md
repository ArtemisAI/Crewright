# Contributing to Crewight

We love your input! We want to make contributing to Crewight as easy and transparent as possible.

## Development Setup

### 1. Fork & Clone
```bash
git clone https://github.com/your-username/crewight.git
cd crewight
```

### 2. Extension Dev
The extension source is in `src/bridge/extension`.
*   Load it in Chrome as "Unpacked".
*   Reload the extension after making changes to `.js` files.

### 3. Server Dev
The MCP server is in `src/bridge`.
```bash
cd src/bridge
npm install
npm run watch  # Auto-rebuilds on change
```

## Pull Requests
1.  Fork the repo and create your branch from `main`.
2.  If you've added code that should be tested, add tests.
3.  Ensure the test suite passes (`npm test`).
4.  Make sure your code lints.

## License
By contributing, you agree that your contributions will be licensed under its MIT License.
