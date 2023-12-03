function solve() {
  let input = document.getElementsByTagName("textarea")[0];
  let output = document.getElementsByTagName("textarea")[1];
  const generateButton = document.getElementsByTagName("button")[0];
  const buyButton = document.getElementsByTagName("button")[1];
  const tbody = document.getElementsByTagName("tbody")[0];

  buyButton.addEventListener("click", (e) => {
    const allElements = tbody.children;
    let furnitures = [];
    let totalPrice = 0;
    let decFactor = 0;

    for (const element of allElements) {
      const elementCheckbox = element.getElementsByTagName("input")[0];
      let [elName, elPrice, elFactor] = element.getElementsByTagName("p");
      elName = elName.textContent; elPrice = elPrice.textContent; elFactor = elFactor.textContent;

      if (elementCheckbox.checked) {
        furnitures.push(elName);
        totalPrice += Number(elPrice);
        decFactor += Number(elFactor);
      }
    }

    let result = [];

    result.push(`Bought furniture: ${furnitures.join(", ")}`);
    result.push(`Total price: ${totalPrice.toFixed(2)}`);
    result.push(`Average decoration factor: ${decFactor / furnitures.length}`);

    output.value = result.join("\n");
  });

  generateButton.addEventListener("click", (e) => {
    let inputValue = input.value;
    inputValue = inputValue.split("");
    inputValue.splice(0, 1);
    inputValue.splice(inputValue.length - 1, 1);
    inputValue = inputValue.join("");

    inputObject = JSON.parse(inputValue);

    const htmlAsString = `<tr>
    <td>
        <img src="${inputObject.img}">
    </td>
    <td>
        <p>${inputObject.name}</p>
    </td>
    <td>
        <p>${inputObject.price}</p>
    </td>
    <td>
        <p>${inputObject.decFactor}</p>
    </td>
    <td>
        <input type="checkbox" />
    </td>
</tr>`

    tbody.innerHTML += htmlAsString;
  });
}