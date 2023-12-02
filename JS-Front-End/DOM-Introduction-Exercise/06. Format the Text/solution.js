function solve() {
  const inputText = document.getElementById("input").value;
  let allSentences = inputText.split(".");
  allSentences.pop();
  const outputElement = document.getElementById("output");

  for (const sentenceIndex in allSentences) {
    allSentences[sentenceIndex] = allSentences[sentenceIndex] + ".";
  }

  let currentSentences = [];

  for (const sentenceIndex in allSentences) {
    if (currentSentences.length % 3 == 0) {
      let newElement = document.createElement("p");
      newElement.textContent = currentSentences.join("").trimStart();
      outputElement.appendChild(newElement);

      currentSentences = [];
    }

    currentSentences.push(allSentences[sentenceIndex]);
  }

  if (currentSentences.length > 0) {
    let newElement = document.createElement("p");
    newElement.textContent = currentSentences.join(" ").trimStart();
    outputElement.appendChild(newElement);
  }
}