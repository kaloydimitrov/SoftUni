function addItem() {
    const input = document.getElementById("newItemText").value;
    const items = document.getElementById("items");
    
    const li = document.createElement("li");
    const a = document.createElement("a");
    a.textContent = "[Delete]";
    a.href = "#";

    a.addEventListener("click", (e) => {
        let parentElement = e.currentTarget.parentNode;
        parentElement.remove();
    });

    li.textContent = input;
    li.appendChild(a);

    items.appendChild(li);
}