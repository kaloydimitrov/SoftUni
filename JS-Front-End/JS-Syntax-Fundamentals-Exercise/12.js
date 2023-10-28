function solve(number, com1, com2, com3, com4, com5) {
    currentNumber = Number(number);
    
    let commands = [com1, com2, com3, com4, com5];

    for (let i = 0; i < commands.length; i++) {
        if (commands[i] == "chop") {
            currentNumber /= 2;
        }
        else if (commands[i] == "dice") {
            currentNumber = Math.sqrt(currentNumber);
        }
        else if (commands[i] == "spice") {
            currentNumber += 1;
        }
        else if (commands[i] == "bake") {
            currentNumber *= 3;
        }
        else if (commands[i] == "fillet") {
            currentNumber *= 0.80;
        }

        console.log(currentNumber);
    }
}

solve('9', 'dice', 'spice', 'chop', 'bake', 'fillet');