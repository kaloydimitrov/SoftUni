function piccolo(inputArray) {
    l = [];

    function findIndex(number) {
        for (let i = 0; i < l.length; i++) {
            if (l[i] == number) {
                return i;
            }
        }
    }

    for (let currentCommand of inputArray) {
        let [command, number] = currentCommand.split(", ");

        if (command == "IN") {
            l.push(number);
        } else {
            l.splice(findIndex(number), 1);
        }
    }

    l.sort();

    if (l.length == 0) {
        console.log("Parking Lot is Empty");
    } else {
        for (let n of l) { console.log(n); }
    }
}

piccolo(['IN, CA2844AA', 'IN, CA1234TA', 'OUT, CA2844AA', 'IN, CA9999TT', 'IN, CA2866HI', 'OUT, CA1234TA', 'IN, CA2844AA', 'OUT, CA2866HI', 'IN, CA9876HH', 'IN, CA2822UU']);