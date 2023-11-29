function calc() {
    const firstInput = document.getElementById("num1");
    const secondInput = document.getElementById("num2");
    let resultInput = document.getElementById("sum");

    resultInput.value = Number(firstInput.value) + Number(secondInput.value);
}
