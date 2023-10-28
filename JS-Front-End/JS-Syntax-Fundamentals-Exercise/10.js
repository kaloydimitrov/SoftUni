function solve(input) {
    function allEqual(input) {
        return input.split('').every(char => char === input[0]);
    }

    let stringInput = input.toString();
    let sum = 0;

    if (allEqual(stringInput)) {
        console.log("true");
    }
    else {
        console.log("false");
    }

    for (i = 0; i < stringInput.length; i++) {
        sum += Number(stringInput[i]);
    }

    console.log(sum);
}

solve(1234);