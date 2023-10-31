function sortArray(array) {
    let newArray = [];
    let sortedArray = array.sort(function(a, b) { return a - b });
    
    while (sortedArray.length != 0) {
        newArray.push(sortedArray.shift());
        newArray.push(sortedArray.pop());
    }

    console.log(newArray);
}

sortAlph([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]);