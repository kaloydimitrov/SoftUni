function factorialDivision(firstNumber, secondNumber) {
    function findFactorial(number) {
        let sum = 1;

        for (let i = 1; i <= number; i++) {
            sum *= i;
        }

        return sum;
    }

    let firstNumberFactorial = findFactorial(firstNumber);
    let secondNumberFactorial = findFactorial(secondNumber);
    let result = firstNumberFactorial / secondNumberFactorial;

    console.log(result.toFixed(2));
}

factorialDivision(6, 2);