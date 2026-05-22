let micMode = false;

async function sendMessage() {

    let input =
        document.getElementById("user-input");

    let message = input.value;

    if (message.trim() === "") return;

    let chatBox =
        document.getElementById("chat-box");

   chatBox.innerHTML +=
`<p style="white-space: pre-wrap;">
<b>You:</b><br>${message}
</p>`;


    input.value = "";

    const response = await fetch("/chat", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            message: message
        })
    });

    const data = await response.json();

   chatBox.innerHTML +=
`<p style="white-space: pre-wrap;">
<b>AI:</b><br>${data.reply}
</p>`;

    chatBox.scrollTop =
        chatBox.scrollHeight;

    // 🔊 only for mic
    if (micMode) {

        const speech =
            new SpeechSynthesisUtterance(
                data.reply
            );

        speechSynthesis.speak(speech);

        micMode = false;
    }
}

// 🎤 mic
function startListening() {

    micMode = true;

    const recognition =
        new webkitSpeechRecognition();

    recognition.lang = "en-US";

    recognition.start();

    recognition.onresult =
        function(event) {

        let text =
            event.results[0][0].transcript;

        document.getElementById(
            "user-input"
        ).value = text;

        sendMessage();
    };
}

// ⌨️ enter key
document
.getElementById("user-input")
.addEventListener("keydown",

function(event) {

    if (event.key === "Enter") {

        sendMessage();
    }
});

