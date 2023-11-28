function oddOccurrences(inputString) {
    let inputArray = inputString.split(" ");

    let dictionary = {};

    for (let word of inputArray) {
        let wordToLower = word.toLowerCase();

        if (!dictionary.hasOwnProperty(wordToLower)) {
            dictionary[wordToLower] = 0;
        }

        dictionary[wordToLower] += 1;
    }

    let resultArray = [];

    for (let [key, value] of Object.entries(dictionary)) {
        if (value % 2 != 0) {
            resultArray.push(key);
        }
    }

    console.log(resultArray.join(" "));
}

oddOccurrences('Cake IS SWEET is Soft CAKE sweet Food');