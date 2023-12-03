function addItem() {
    const text = document.getElementById("newItemText");
    const value = document.getElementById("newItemValue");
    const menu = document.getElementById("menu");

    const newSection = document.createElement("option");
    newSection.textContent = text.value;
    newSection.value = value.value;

    menu.appendChild(newSection);

    text.value = "";
    value.value = "";
}