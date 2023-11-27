function employees(inputArray) {
    for (let employee of inputArray) {
        console.log(`Name: ${employee} -- Personal Number: ${employee.length}`);
    }
}

employees(['Silas Butler', 'Adnaan Buckley', 'Juan Peterson', 'Brendan Villarreal']);