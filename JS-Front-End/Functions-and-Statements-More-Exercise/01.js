function carWash(inputArray) {
    let totalPercentige = 0;
    
    for (let i = 0; i < inputArray.length; i++) {
        switch(inputArray[i]) {
            case "soap":
                totalPercentige += 10;
                break;
            case "water":
                totalPercentige *= 1.20;
                break;
            case "vacuum cleaner":
                totalPercentige *= 1.25;
                break;
            case "mud":
                totalPercentige *= 0.90;
                break;
        }
    }

    console.log(`The car is ${totalPercentige.toFixed(2)}% clean.`);
}

carWash(["soap", "water", "mud", "mud", "water", "mud", "vacuum cleaner"]);