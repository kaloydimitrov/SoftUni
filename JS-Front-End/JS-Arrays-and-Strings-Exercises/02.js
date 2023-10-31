function printNthElement(array, step) {
    newArray = [];
    
    for (let i = 0; i < array.length; i += step) {
        newArray.push(array[i]);
    }

    console.log(newArray);

    // for (let i = 0; i < newArray.length; i++) {
    //     console.log(newArray[i]);
    // }
}

printNthElement(['dsa', 'asd', 'test', 'tset'], 2);