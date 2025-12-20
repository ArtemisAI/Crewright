
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
import { WebSocketServer, WebSocket } from "ws";
import { randomUUID } from "crypto";

// --- Global State ---
let activeSocket: WebSocket | null = null;
const responseMap = new Map<string, (result: any) => void>();

// --- WebSocket Server ---
const WSS_PORT = 8765;
const wss = new WebSocketServer({ port: WSS_PORT, host: "0.0.0.0" });

console.error(`[Bridge] Starting WebSocket Server on 0.0.0.0:${WSS_PORT}...`);

wss.on("connection", (ws) => {
    console.error("[Bridge] Extension Connected!");
    activeSocket = ws;

    ws.on("message", (data) => {
        try {
            const message = JSON.parse(data.toString());
            if (message.id && responseMap.has(message.id)) {
                const resolve = responseMap.get(message.id);
                if (resolve) {
                    resolve(message.result || message.error);
                    responseMap.delete(message.id);
                }
            }
        } catch (e) {
            console.error("[Bridge] Error parsing message:", e);
        }
    });

    ws.on("close", () => {
        console.error("[Bridge] Extension Disconnected.");
        activeSocket = null;
    });

    ws.on("error", (e) => {
        console.error("[Bridge] WebSocket Error:", e);
    });
});

// --- Helper: Send to Extension ---
async function sendToExtension(method: string, params: any) {
    // Wait for connection logic
    // Wait for connection logic (Copilot Optimization)
    if (!activeSocket || activeSocket.readyState !== WebSocket.OPEN) {
        console.error("[Bridge] Waiting for extension to connect...");

        await new Promise<void>((resolve, reject) => {
            const timeout = setTimeout(() => {
                cleanup();
                reject(new Error("Timeout waiting for extension to connect"));
            }, 15000);

            function checkAndResolve() {
                if (activeSocket && activeSocket.readyState === WebSocket.OPEN) {
                    cleanup();
                    resolve();
                }
            }

            function onConnection(ws: WebSocket) {
                // The global handler (line 18) sets activeSocket first.
                // But we listen here to trigger immediate resolution.
                ws.once("open", checkAndResolve);
                checkAndResolve();
            }

            function cleanup() {
                clearTimeout(timeout);
                wss.off("connection", onConnection);
            }

            wss.on("connection", onConnection);
            // Also check immediately in case the socket is already open
            checkAndResolve();
        });
    }

    if (!activeSocket || activeSocket.readyState !== WebSocket.OPEN) {
        throw new Error("No browser connected. Please install the extension and ensure it is active.");
    }

    const id = randomUUID();
    const payload = { id, method, params };

    return new Promise((resolve, reject) => {
        // Timeout of 30s
        const timeout = setTimeout(() => {
            responseMap.delete(id);
            reject(new Error("Timeout waiting for browser response"));
        }, 30000);

        responseMap.set(id, (result) => {
            clearTimeout(timeout);
            resolve(result);
        });

        activeSocket?.send(JSON.stringify(payload));
    });
}

// --- MCP Server ---
const server = new McpServer({
    name: "stealth-bridge",
    version: "1.0.0",
});

server.tool(
    "navigate",
    "Navigates the active tab to the specified URL.",
    { url: z.string() },
    async ({ url }) => {
        const result = await sendToExtension("navigate", { url });
        return { content: [{ type: "text", text: JSON.stringify(result) }] };
    }
);

server.tool(
    "get_page_content",
    "Returns the text content of the current page.",
    {},
    async () => {
        const result = await sendToExtension("get_page_content", {});
        return { content: [{ type: "text", text: typeof result === 'string' ? result : JSON.stringify(result) }] };
    }
);

server.tool(
    "click",
    "Clicks an element defined by the CSS selector.",
    { selector: z.string() },
    async ({ selector }) => {
        const result = await sendToExtension("click", { selector });
        return { content: [{ type: "text", text: JSON.stringify(result) }] };
    }
);

server.tool(
    "fill",
    "Fills an input defined by the CSS selector with the specified value.",
    { selector: z.string(), value: z.string() },
    async ({ selector, value }) => {
        const result = await sendToExtension("fill", { selector, value });
        return { content: [{ type: "text", text: JSON.stringify(result) }] };
    }
);

server.tool(
    "ask_human",
    "Pauses execution and asks the human operator for help via the console.",
    { question: z.string() },
    async ({ question }) => {
        console.error(`\n[AGENT NEEDS HELP] ${question}`);
        return { content: [{ type: "text", text: "Please alert the user manually. (Stdio input not supported in this mode)" }] };
    }
);

server.tool(
    "screenshot",
    "Captures a screenshot of the current visible tab.",
    { width: z.number().optional() },
    async () => {
        const result = await sendToExtension("screenshot", {});
        // result should be a base64 string
        return {
            content: [
                { type: "text", text: "Screenshot captured" },
                { type: "image", data: result as string, mimeType: "image/png" }
            ]
        };
    }
);

server.tool(
    "hover",
    "Hovers over an element defined by the CSS selector.",
    { selector: z.string() },
    async ({ selector }) => {
        const result = await sendToExtension("hover", { selector });
        return { content: [{ type: "text", text: JSON.stringify(result) }] };
    }
);

server.tool(
    "press",
    "Simulates pressing a keyboard key (e.g., 'Enter', 'Escape').",
    { key: z.string() },
    async ({ key }) => {
        const result = await sendToExtension("press", { key });
        return { content: [{ type: "text", text: JSON.stringify(result) }] };
    }
);

server.tool(
    "evaluate",
    "Executes custom JavaScript in the page context.",
    { expression: z.string() },
    async ({ expression }) => {
        const result = await sendToExtension("evaluate", { expression });
        return { content: [{ type: "text", text: JSON.stringify(result) }] };
    }
);

server.tool(
    "scroll",
    "Scrolls the page. Direction can be 'up', 'down', 'top', or 'bottom'.",
    { direction: z.enum(["up", "down", "top", "bottom"]) },
    async ({ direction }) => {
        const result = await sendToExtension("scroll", { direction });
        return { content: [{ type: "text", text: JSON.stringify(result) }] };
    }
);

// --- Start Server ---
async function main() {
    const transport = new StdioServerTransport();
    await server.connect(transport);
    console.error("[Bridge] MCP Server running on Stdio...");
}

main().catch((error) => {
    console.error("[Bridge] Fatal Error:", error);
    process.exit(1);
});
