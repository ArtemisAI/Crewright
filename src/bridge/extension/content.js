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
        else if (msg.method === "click") {
            const el = document.querySelector(msg.params.selector);
            if (!el) return { status: "error", error: "Element not found: " + msg.params.selector };

            // Trusted event simulation
            el.focus();
            ['mouseover', 'mousedown', 'mouseup', 'click'].forEach(evt => {
                el.dispatchEvent(new MouseEvent(evt, { bubbles: true, cancelable: true, view: window }));
            });

            return { status: "success", result: "Clicked " + msg.params.selector };
        }
        else if (msg.method === "fill") {
            const el = document.querySelector(msg.params.selector);
            if (!el) return { status: "error", error: "Element not found: " + msg.params.selector };

            el.focus();
            el.value = msg.params.value; // Playwright uses 'fill' with 'value'
            el.dispatchEvent(new Event('input', { bubbles: true }));
            el.dispatchEvent(new Event('change', { bubbles: true }));

            return { status: "success", result: "Filled " + msg.params.selector };
        }
        else if (msg.method === "hover") {
            const el = document.querySelector(msg.params.selector);
            if (!el) return { status: "error", error: "Element not found: " + msg.params.selector };

            el.focus();
            ['mouseenter', 'mouseover', 'mousemove'].forEach(evt => {
                el.dispatchEvent(new MouseEvent(evt, { bubbles: true, cancelable: true, view: window }));
            });
            return { status: "success", result: "Hovered over " + msg.params.selector };
        }
        else if (msg.method === "press") {
            // If checking specific element focus, maybe useful, but often keys are global or on active element
            const el = document.activeElement || document.body;
            const key = msg.params.key;

            const eventParams = {
                key: key,
                code: key,
                keyCode: 0, // Deprecated but sometimes needed
                view: window,
                bubbles: true,
                cancelable: true
            };

            el.dispatchEvent(new KeyboardEvent('keydown', eventParams));
            el.dispatchEvent(new KeyboardEvent('keypress', eventParams));
            el.dispatchEvent(new KeyboardEvent('keyup', eventParams));

            return { status: "success", result: "Pressed key: " + key };
        }

        else if (msg.method === "scroll") {
            const direction = msg.params.direction;
            if (direction === "top") window.scrollTo(0, 0);
            else if (direction === "bottom") window.scrollTo(0, document.body.scrollHeight);
            else if (direction === "up") window.scrollBy(0, -500);
            else if (direction === "down") window.scrollBy(0, 500);

            return { status: "success", result: "Scrolled " + direction };
        }
    } catch (e) {
        return { status: "error", error: e.toString() };
    }
}
