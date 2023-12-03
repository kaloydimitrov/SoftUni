function encodeAndDecodeMessages() {
    const [decodedTextarea, encodedTextarea] = document.getElementsByTagName("textarea");
    const [firstButton, secondButton] = document.getElementsByTagName("button");
    
    firstButton.addEventListener("click", (e) => {
        const value = decodedTextarea.value;
        let newValue = "";

        for (const char of value) {
            const nextChar = String.fromCharCode(char.charCodeAt(0) + 1);
            newValue += nextChar;
        }

        decodedTextarea.value = "";
        encodedTextarea.value = newValue;
    });

    secondButton.addEventListener("click", (e) => {
        const value = encodedTextarea.value;
        let newValue = "";

        for (const char of value) {
            const previousChar = String.fromCharCode(char.charCodeAt(0) - 1);
            newValue += previousChar;
        }

        encodedTextarea.value = "";
        decodedTextarea.value = newValue;
    });
}