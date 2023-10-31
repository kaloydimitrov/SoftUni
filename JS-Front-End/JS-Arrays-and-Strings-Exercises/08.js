console.log("------------ Version 1 ------------");

function pascalSplitter(text) {
    let textArray = [];
    let currentWord = text[0];
    let index = 0;

    while(true) {
        index++;

        if (index == text.length - 1) {
            textArray.push(currentWord + text[text.length - 1]);
            break;
        }
        else if (text[index].toUpperCase() == text[index]) {
            textArray.push(currentWord);
            currentWord = text[index];
            continue;
        }

        currentWord += text[index];
    }

    console.log(textArray.join(", "));
}

pascalSplitter('SplitMeIfYouCanHaHaYouCantOrYouCan');

console.log("------------ Version 2 ------------");

function pascalSplitter(text) {
    let textArray = [];
    let currentWord = text[0];

    for (let index = 1; index < text.length; index++) {
        if (text[index].toUpperCase() === text[index]) {
            textArray.push(currentWord);
            currentWord = text[index];
        }
        else {
            currentWord += text[index];
        }
    }

    textArray.push(currentWord);
    console.log(textArray.join(", "));
}

pascalSplitter('SplitMeIfYouCanHaHaYouCantOrYouCan');