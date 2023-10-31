function timesHashTag(text) {
    let regex = /^[a-zA-Z]+$/; 
    
    let textArray = text.split(" ");
    
    for (let wrdIndex = 0; wrdIndex < textArray.length; wrdIndex++) {
        if (textArray[wrdIndex].includes("#")) {
            let word = textArray[wrdIndex].substring(1);

            if (regex.test(word) && word.length > 0) {
                console.log(word);
            }
        }
    }
}

timesHashTag('The symbol # is known #variously in English-speaking #regions as the #number sign');