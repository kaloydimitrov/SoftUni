function passwordValidator(password) {
    function onlyLettersAndNumbers(str) {
        return /^[A-Za-z0-9]*$/.test(str);
    }

    function digitsCounter(str) {
        let count = 0;
        
        for (let i = 0; i < str.length; i++) {
            if (!isNaN(str[i])) {
                count++;
            }
        }

        return count;
    }
    
    let isValid = true;

    if (password.length < 6 || password.length > 10) {
        console.log("Password must be between 6 and 10 characters");
        isValid = false;
    }
    if (!onlyLettersAndNumbers(password)) {
        console.log("Password must consist only of letters and digits");
        isValid = false;
    }
    if (digitsCounter(password) < 2) {
        console.log("Password must have at least 2 digits");
        isValid = false;
    }

    if (isValid) {
        console.log("Password is valid");
    }
}

passwordValidator('Pa$s$s');