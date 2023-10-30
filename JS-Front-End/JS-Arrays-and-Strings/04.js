function substring(text, n1, n2) {
    let textArray = text.split("");
    let splicedArray = textArray.slice(n1, n2 + 1);
    console.log(splicedArray.join(""));
}

substring('SkipWord', 4, 7);