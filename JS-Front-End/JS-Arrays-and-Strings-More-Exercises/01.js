function login(input) {
    function reverseString(str) {
        let splitString = str.split("");
        let reverseArray = splitString.reverse();

        return reverseArray.join("");
    }

    let password = input.shift();

    for (let i = 0; i < input.length; i++) {
        if (reverseString(input[i]) == password) {
            console.log(`User ${password} logged in.`);
            break;
        }
        else if (i == 3) {
            console.log(`User ${password} blocked!`);
            break;
        }

        console.log("Incorrect password. Try again.");
    }
}

login(['sunny','rainy','cloudy','sunny','not sunny']);