function arrayNumbers(number, array) {
     let newArray = [];

     for (let i = 0; i < number; i++) {
        newArray.unshift(array[i]);
     }

     console.log(newArray.join(" "));
}

arrayNumbers(3, [10, 20, 30, 40, 50]);