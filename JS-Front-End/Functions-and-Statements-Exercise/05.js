function palindromeIntegers(inputArray) {
    for (let i = 0; i < inputArray.length; i++) {
        let numberArray = String(inputArray[i]).split("");
        let reversedNumberArray = numberArray.slice().reverse();
        
        if (numberArray.join("") == reversedNumberArray.join("")) {
            console.log(true);
        }
        else {
            console.log(false);
        }
    }
}

palindromeIntegers([123,323,421,121]);