function lockedProfile() {
    const profiles = Array.from(document.getElementsByClassName("profile"));

    for (const profile of profiles) {
        const button =  profile.querySelector("button");

        button.addEventListener("click", (e) => {
            const currentElement = e.currentTarget;
            const parentElement = currentElement.parentElement;
            const userFields = parentElement.getElementsByTagName("div")[0];
            const radioLock = parentElement.querySelector("input");

            if (radioLock.checked) {
                return;
            }

            if (currentElement.textContent == "Hide it") {
                currentElement.textContent = "Show more";
                userFields.style.display = "none";
            } else {
                currentElement.textContent = "Hide it";
                userFields.style.display = "block";
            }
        });
    }
}