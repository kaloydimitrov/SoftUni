function numberModification(number) {
    let stringNumber = String(number);
    let numberArray = stringNumber.split("");


    while (true) {
        let numbersSum = 0;

        for (i = 0; i < numberArray.length; i++) {
            numbersSum += Number(numberArray[i]);
        }

        if ((numbersSum / numberArray.length) > 5) {
            break;
        }

        numberArray.push("9");
    }


    console.log(numberArray.join(""));
}

numberModification(101);