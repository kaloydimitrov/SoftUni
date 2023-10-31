function revealWords(words, text) {
    let wordsArray = words.split(", ");
    let textArray = text.split(" ");
    
    for (let i = 0; i < textArray.length; i++) {
        for (let w = 0; w < wordsArray.length; w++) {
            if (textArray[i].length == wordsArray[w].length && !textArray.includes(wordsArray[w])) {
                textArray[i] = wordsArray[w];
            }
        }
    }

    console.log(textArray.join(" "));
}

revealWords('great, learning', 'softuni is ***** place for ******** new programming languages');