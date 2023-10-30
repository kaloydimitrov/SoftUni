function censoredWords(input, word) {
    inputArray = input.split(" ");
    wordIndex = inputArray.indexOf(word);
    newWord = "";

    for (let i = 0; i < word.length; i++) {
        newWord += "*";
    }

    inputArray[wordIndex] = newWord;
    console.log(inputArray.join(" "));
}

censoredWords('Find the hidden word', 'hidden');