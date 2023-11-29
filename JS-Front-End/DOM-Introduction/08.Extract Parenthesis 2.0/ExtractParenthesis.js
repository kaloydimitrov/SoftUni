function extract(content) {
    const pTagText = document.getElementById("content").textContent;

    let regex = /\(([^)]+)\)/g;
    let matches = [];
    let match;

    while ((match = regex.exec(pTagText)) !== null) {
        matches.push(match[1]);
    }

    const result = matches.join("; ");
    console.log(result);
    return result;
}