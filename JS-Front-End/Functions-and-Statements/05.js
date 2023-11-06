function simpleCalculator(num1, num2, action) {
    let result = 0;

    switch(action) {
        case "multiply":
            result = num1 * num2;
            break;
        case "divide":
            result = num1 / num2;
            break;
        case "add":
            result = num1 + num2;
            break;
        case "subtract":
            result = num1 - num2;
            break;
    }

    console.log(result);
}

simpleCalculator(50, 13, 'subtract');