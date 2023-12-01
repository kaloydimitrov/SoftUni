function subtract() {
    const firstInputValue = document.getElementById("firstNumber").value;
    const secondInputValue = document.getElementById("secondNumber").value;
    const resultField = document.getElementById("result");

    resultField.textContent = Number(firstInputValue) - Number(secondInputValue);
}