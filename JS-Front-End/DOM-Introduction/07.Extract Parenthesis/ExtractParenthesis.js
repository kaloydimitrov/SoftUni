function extract(content) {
    const pTagText = document.getElementById("content").textContent;

    let assemblingWord = false;
    let currentWord = "";
    let wordArray = [];

    for (let letter of pTagText) {
        if (letter == "(") {
            assemblingWord = true;
            continue;
        } else if (letter == ")") {
            assemblingWord = false
            wordArray.push(currentWord);
            currentWord = "";
            continue;
        }

        if (assemblingWord) {
            currentWord += letter;
        }
    }

    const result = wordArray.join("; ");
    console.log(result);
    return result;
}