// content.js
console.log("CrewAI Stealth Bridge Content Script Loaded");

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    console.log("Content script received:", request);
    processMessage(request).then(sendResponse);
    return true; // Keep channel open for async response
});

async function processMessage(msg) {
    try {
        if (msg.method === "get_page_content") {
            // Simplified markdown-like dump
            return { status: "success", result: document.body.innerText.substring(0, 5000) };
        }
        else if (msg.method === "click_element") {
            const el = document.querySelector(msg.params.selector);
            if (!el) return { status: "error", error: "Element not found: " + msg.params.selector };

            // Trusted event simulation
            el.focus();
            ['mouseover', 'mousedown', 'mouseup', 'click'].forEach(evt => {
                el.dispatchEvent(new MouseEvent(evt, { bubbles: true, cancelable: true, view: window }));
            });

            return { status: "success", result: "Clicked " + msg.params.selector };
        }
        else if (msg.method === "type_text") {
            const el = document.querySelector(msg.params.selector);
            if (!el) return { status: "error", error: "Element not found: " + msg.params.selector };

            el.focus();
            el.value = msg.params.text; // Simple value set for now (React might reject this, but start simple)
            el.dispatchEvent(new Event('input', { bubbles: true }));
            el.dispatchEvent(new Event('change', { bubbles: true }));

            return { status: "success", result: "Typed into " + msg.params.selector };
        }
    } catch (e) {
        return { status: "error", error: e.toString() };
    }
}
