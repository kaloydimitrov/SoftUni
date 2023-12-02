function deleteByEmail() {
    const tdElements = document.querySelectorAll("tbody tr td:nth-child(2)");
    const value = document.querySelector("label input").value;
    const result = document.getElementById("result");

    let found = false;

    for (td of tdElements) {
        if (td.textContent == value) {
            td.parentNode.remove();
            found = true;
        }
    }

    if (found) {
        result.textContent = "Deleted.";
    } else {
        result.textContent = "Not found.";
    }
}