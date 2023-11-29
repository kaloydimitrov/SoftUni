function editElement(element, text, replaceText) {
    let elementText = element.textContent;
    elementText = elementText.replace(text, replaceText);
    element.textContent = elementText;
}