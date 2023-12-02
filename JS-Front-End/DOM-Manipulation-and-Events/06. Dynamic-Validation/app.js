function validate() {
    const input = document.getElementById("email");

    input.addEventListener("change", (e) => {
        const currentElement = e.currentTarget;

        if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(currentElement.value)) {
            currentElement.classList.remove("error");
        } else {
            currentElement.className = "error";
        }
    });
}