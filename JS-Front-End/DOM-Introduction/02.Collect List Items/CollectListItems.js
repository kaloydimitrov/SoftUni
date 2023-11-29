function extractText() {
    const textAreaElement = document.getElementById("result");
    const itemElements = document.getElementById("items").children;
    const arrayElements = Array.from(itemElements);
    const arrayTextElements = [];

    for (let element of arrayElements) { arrayTextElements.push(element.textContent); }

    textAreaElement.textContent = arrayTextElements.join("\n");
}