function oddAndEvenSum(number) {
    let stringNumber = String(number);
    let oddSum = 0;
    let evenSum = 0;

    for (let i = 0; i < stringNumber.length; i++) {
        let currentNumber = Number(stringNumber[i]);

        if (currentNumber % 2 == 0) {
            evenSum += currentNumber;
        }
        else {
            oddSum += currentNumber;
        }
    }

    console.log(`Odd sum = ${oddSum}, Even sum = ${evenSum}`);
}

oddAndEvenSum(3495892137259234);