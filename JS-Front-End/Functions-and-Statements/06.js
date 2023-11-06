function signCheck(numOne, numTwo, numThree) {
    let result = numOne * numTwo * numThree;
    
    if (result > 0) {
        console.log("Positive");
    }
    else {
        console.log("Negative");
    }
}

signCheck(-1, -2, -3);