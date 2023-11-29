function sumTable() {
    const sumElement = document.getElementById("sum");
    const trElements = document.querySelectorAll("tr");
    let trElementsArray = Array.from(trElements);
    trElementsArray.shift();
    trElementsArray.pop();

    let sum = 0;

    for (let tr of trElementsArray) {
        const tdPriceElement = tr.querySelectorAll("td")[1];
        sum += Number(tdPriceElement.textContent);
    }

    sumElement.textContent = String(sum);
}