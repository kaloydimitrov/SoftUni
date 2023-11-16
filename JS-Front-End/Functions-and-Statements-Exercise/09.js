function loadingBar(percent) {
    let loadingBarArray = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."];
    let number = percent / 10;

    if (number == 10) {
        console.log("100% Complete!");
        console.log("[%%%%%%%%%%]");
    }
    else {
        for (let i = 0; i < number; i++) {
            loadingBarArray[i] = "%";
        }

        console.log(`${percent}% [${loadingBarArray.join("")}]`);
        console.log("Still loading...");
    }
}

loadingBar(90);