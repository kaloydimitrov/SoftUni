function colorize() {
    const trElements = document.querySelectorAll("tr");
    let trElementsArray = Array.from(trElements);
    trElementsArray.shift();

    for (let trIndex in trElementsArray) {
        console.log(`${trIndex}: ${trElementsArray[trIndex]}`);

        if (trIndex % 2 == 0) {
            const tdElements = trElementsArray[trIndex].querySelectorAll("td");

            for (td of tdElements) {
                td.style.backgroundColor = "teal";
            }
        }
    }
}