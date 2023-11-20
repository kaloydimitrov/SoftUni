function pointsValidation(inputArray) {
    function formula(x1, y1, x2, y2) {
        return Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2);
    }

    x1 = inputArray[0]; y1 = inputArray[1]; x2 = inputArray[2]; y2 = inputArray[3];

    if (formula(x1, y1, 0, 0) % 1 == 0) {
        console.log(`{${x1}, ${y1}} to {0, 0} is valid`);
    }
    else {
        console.log(`{${x1}, ${y1}} to {0, 0} is invalid`);
    }

    if (formula(x2, y2, 0, 0) % 1 == 0) {
        console.log(`{${x2}, ${y2}} to {0, 0} is valid`);
    }
    else {
        console.log(`{${x2}, ${y2}} to {0, 0} is invalid`);
    }

    if (formula(x1, y1, x2, y2) % 1 == 0) {
        console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is valid`);
    }
    else {
        console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is invalid`);
    }
}

pointsValidation([3, 0, 0, 4]);