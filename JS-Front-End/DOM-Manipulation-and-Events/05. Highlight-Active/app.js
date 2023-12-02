function focused() {
    const inputElements = document.querySelectorAll("input");

    for (const element of inputElements) {
        element.addEventListener("focus", (e) => {
            let currentElement = e.currentTarget.parentNode;
            currentElement.className = "focused";
        });

        element.addEventListener("blur", (e) => {
            let currentElement = e.currentTarget.parentNode;
            currentElement.classList.remove("focused");
        });
    }
}