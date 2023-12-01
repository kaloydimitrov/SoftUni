function solve() {
  const text = document.getElementById("text").value.toLowerCase().split(" ");
  const namingConvention = document.getElementById("naming-convention").value;
  const result = document.getElementById("result");

  let finalArray = [];

  for (let word of text) {
    currentWord = word.split("");
    currentWord[0] = currentWord[0].toUpperCase();
    finalArray.push(currentWord.join(""));
  }

  if (namingConvention == "Camel Case") {
    wordToFix = finalArray[0];
    wordToArray = wordToFix.split("");
    wordToArray[0] = wordToArray[0].toLowerCase();
    finalArray[0] = wordToArray.join("");
  }

  if (namingConvention != "Camel Case" && namingConvention != "Pascal Case") {
    result.textContent = "Error!"
  }
  else {
    result.textContent = finalArray.join("");
  }
}