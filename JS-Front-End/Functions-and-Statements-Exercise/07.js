function NxNMatrix(n) {
    for (let i = 0; i < n; i++) {
        let currentRow = [];

        for (let i = 0; i < n; i++) {
            currentRow.push(n);
        }

        console.log(currentRow.join(" "));
    }
}

NxNMatrix(7);