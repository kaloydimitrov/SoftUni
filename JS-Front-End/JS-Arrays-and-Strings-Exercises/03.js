function sortAlph(array) {
    let sortedArray = array.sort();
    
    for (let i = 0; i < sortedArray.length; i++) {
        console.log(`${i + 1}.${sortedArray[i]}`);
    }
}

sortAlph(["John", "Bob", "Christina", "Ema", "A", "BA"]);