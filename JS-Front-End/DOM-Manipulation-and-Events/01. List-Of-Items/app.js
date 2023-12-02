function addItem() {
    let items = document.getElementById("items");
    let value = document.getElementById("newItemText").value;

    let li = document.createElement("li");
    li.textContent = value;

    items.appendChild(li);
}