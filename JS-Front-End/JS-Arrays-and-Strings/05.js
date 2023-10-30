function censoredWords(input, word) {
    newWord = "";

    for (let i = 0; i < word.length; i++) {
        newWord += "*";
    }

    console.log(input.replace(word, newWord));
}

censoredWords('Find the hidden word', 'word');