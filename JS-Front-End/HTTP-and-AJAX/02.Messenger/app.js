function attachEvents() {
    const name = document.getElementsByTagName("input")[0];
    const message = document.getElementsByTagName("input")[1];
    const buttonSend = document.getElementsByTagName("input")[2];
    const buttonRefresh = document.getElementsByTagName("input")[3];

    const textarea = document.querySelector("textarea");

    const baseURL = "http://localhost:3030/jsonstore/messenger";

    buttonSend.addEventListener("click", () => {
        const authorName = name.value;
        const msgText = message.value;

        let messageObject = {
            author: authorName,
            content: msgText,
        };

        fetch(baseURL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(messageObject),
        })
    });

    buttonRefresh.addEventListener("click", () => {
        let messagesArray = [];

        fetch(baseURL)
            .then((res) => res.json())
            .then((messages) => {
                for (const message of Object.values(messages)) {
                    const name = Object.values(message)[0];
                    const msg = Object.values(message)[1];

                    messagesArray.push(`${name}: ${msg}`);
                }
  
                textarea.textContent = messagesArray.join("\n");
            })
    });
}

attachEvents();