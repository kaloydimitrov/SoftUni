function wordsTracker(arrayInput) {
    let array = arrayInput;
    let [firstWord, secondWord] = array.shift().split(" ");

    let wordCounter = {
        [firstWord]: 0,
        [secondWord]: 0
    }

    for (let word of array) {
        if (word == firstWord) {
            wordCounter[firstWord] += 1;
        } else if (word == secondWord) {
            wordCounter[secondWord] += 1;
        }
    }

    if (wordCounter[firstWord] > wordCounter[secondWord]) {
        console.log(`${firstWord} - ${wordCounter[firstWord]}`);
        console.log(`${secondWord} - ${wordCounter[secondWord]}`);
    } else {
        console.log(`${secondWord} - ${wordCounter[secondWord]}`);
        console.log(`${firstWord} - ${wordCounter[firstWord]}`);
    }
    
}

wordsTracker(['this sentence',
    'In', 'this', 'sentence', 'you', 'have',
    'to', 'count', 'the', 'occurrences', 'of',
    'the', 'words', 'this', 'and', 'sentence',
    'because', 'this', 'is', 'your', 'task']);