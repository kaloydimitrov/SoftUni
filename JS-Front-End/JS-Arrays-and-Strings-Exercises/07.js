function stringSubstring(word, text) {
    let textArray = text.split(" ");
    let wordNotFound = true;

    for (let i = 0; i < textArray.length; i++) {
        let wordLowercase = textArray[i].toLowerCase();
        
        if (wordLowercase == word) {
            wordNotFound = false;
            console.log(word);
        }
    }

    if (wordNotFound) {
        console.log(`${word} not found!`);
    }
}

stringSubstring('python', 'JavaScript is the best programming language');