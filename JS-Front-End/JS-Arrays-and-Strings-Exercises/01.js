function arrayRotation(array, rotations) {
    for (let i = 0; i < rotations; i++) {
        let firstItem = array.shift();
        array.push(firstItem);
    }

    console.log(array.join(" "));
}

arrayRotation([32, 21, 61, 1], 4);