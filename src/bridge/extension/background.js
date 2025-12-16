// background.js
let socket = null;
const SERVER_URL = "ws://localhost:8765";

function connect() {
    console.log("Connecting to CrewAI Bridge...");
    socket = new WebSocket(SERVER_URL);

    socket.onopen = () => {
        console.log("Connected to CrewAI Bridge!");
        chrome.action.setBadgeText({ text: "ON" });
        chrome.action.setBadgeBackgroundColor({ color: "#4CAF50" });
    };

    socket.onmessage = async (event) => {
        const message = JSON.parse(event.data);
        console.log("Received command:", message);

        try {
            await handleCommand(message);
        } catch (error) {
            console.error("Command execution failed:", error);
            sendResponse(message.id, { status: "error", error: error.message });
        }
    };

    socket.onclose = () => {
        console.log("Disconnected. Retrying in 5s...");
        chrome.action.setBadgeText({ text: "OFF" });
        chrome.action.setBadgeBackgroundColor({ color: "#F44336" });
        setTimeout(connect, 5000);
    };

    socket.onerror = (err) => {
        console.error("WebSocket Error:", err);
        socket.close();
    };
}

async function handleCommand(msg) {
    if (msg.method === "navigate") {
        // Create a promise that resolves when the tab finishes loading
        const navigationComplete = new Promise((resolve) => {
            const listener = (tabId, changeInfo, tab) => {
                if (changeInfo.status === 'complete') {
                    chrome.tabs.onUpdated.removeListener(listener);
                    resolve();
                }
            };
            chrome.tabs.onUpdated.addListener(listener);
            // Timeout fallback (10s) to avoid hanging
            setTimeout(() => {
                chrome.tabs.onUpdated.removeListener(listener);
                resolve();
            }, 10000);
        });

        await chrome.tabs.update({ url: msg.params.url });
        await navigationComplete;

        sendResponse(msg.id, { status: "success", result: "Navigated to " + msg.params.url });

    } else if (msg.method === "get_page_content" || msg.method === "click_element" || msg.method === "type_text") {
        // Execute in the active tab
        const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
        if (!tab) {
            sendResponse(msg.id, { status: "error", error: "No active tab found" });
            return;
        }

        // Send message to content script
        try {
            const response = await chrome.tabs.sendMessage(tab.id, msg);
            sendResponse(msg.id, response);
        } catch (e) {
            console.error("Content script error", e);
            sendResponse(msg.id, { status: "error", error: "Could not communicate with page content. Try reloading." });
        }
    } else {
        sendResponse(msg.id, { status: "error", error: "Unknown method: " + msg.method });
    }
}

function sendResponse(id, result) {
    if (socket && socket.readyState === WebSocket.OPEN) {
        socket.send(JSON.stringify({ id: id, result: result }));
    }
}

// Start connection
connect();
