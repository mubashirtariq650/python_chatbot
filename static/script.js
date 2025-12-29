let messages = [];
const chatBox = document.getElementById("chat");
const inputBox = document.getElementById("input");
const sendBtn = document.getElementById("send-btn");
const deleteBtn = document.getElementById("delete-btn");

async function sendMessage() {
    if (!inputBox.value) return;

    const userMsg = inputBox.value;
    messages.push({ role: "user", content: userMsg });
    chatBox.innerHTML += `<div class="chat-bubble user-msg">${userMsg}</div>`;
    inputBox.value = "";
    chatBox.scrollTop = chatBox.scrollHeight;

    // Typing indicator
    const typingDiv = document.createElement("div");
    typingDiv.className = "chat-bubble bot-msg";
    typingDiv.innerHTML = `<div class="typing"><span></span><span></span><span></span></div>`;
    chatBox.appendChild(typingDiv);
    chatBox.scrollTop = chatBox.scrollHeight;

    const res = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ messages })
    });

    const data = await res.json();
    messages.push({ role: "assistant", content: data.reply });
    typingDiv.remove();
    chatBox.innerHTML += `<div class="chat-bubble bot-msg">${data.reply}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Delete chats
function deleteChats() {
    chatBox.innerHTML = "";
    messages = [];
}

// Enter key + send button
inputBox.addEventListener("keydown", e => { if(e.key === "Enter"){e.preventDefault(); sendMessage();} });
sendBtn.addEventListener("click", sendMessage);
deleteBtn.addEventListener("click", deleteChats);
