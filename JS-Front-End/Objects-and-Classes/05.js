function phoneBook(array) {
    let phoneBookObject = {}

    for (let item of array) {
        let [key, value] = item.split(" ");

        phoneBookObject[key] = value;
    }

    for (let [key, value] of Object.entries(phoneBookObject)) {
        console.log(`${key} -> ${value}`);
    }
}

phoneBook(['Tim 0834212554', 'Peter 0877547887', 'Bill 0896543112', 'Tim 0876566344']);