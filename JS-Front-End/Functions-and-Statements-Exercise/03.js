function charactersInRange(firstChar, secondChar) {
    let firstCharCode = firstChar.charCodeAt(0);
    let secondCharCode = secondChar.charCodeAt(0);

    if (secondCharCode < firstCharCode) {
        firstCharCode = secondChar.charCodeAt(0);
        secondCharCode = firstChar.charCodeAt(0);
    }

    let chars = [];

    for (let i = firstCharCode + 1; i < secondCharCode; i++) {
        chars.push(String.fromCharCode(i));
    }

    console.log(chars.join(" "));
}

charactersInRange("C", "#");
