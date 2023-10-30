function countString(input, word) {
    inputArray = input.split(" ");
    wordCounter = 0;

    for (let i = 0; i < inputArray.length; i++) {
        if (inputArray[i] == word) {
            wordCounter += 1;
        }
    }

    console.log(wordCounter);
}

countString('softuni is great place for learning new programming languages', 'softuni');