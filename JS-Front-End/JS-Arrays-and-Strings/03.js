function EvenOddSubtraction(input) {
    evenSum = 0;
    oddSum = 0;

    for (let i = 0; i < input.length; i++) {
        if (input[i] % 2 == 0) {
            evenSum += input[i];
        }
        else {
            oddSum += input[i];
        }
    }

    console.log(evenSum - oddSum);
}

EvenOddSubtraction([3,5,7,9]);