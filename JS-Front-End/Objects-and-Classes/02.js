function city(object) {
    for (let key in object) {
        console.log(`${key} -> ${object[key]}`);
    }
}

let person = {
    name: "Kaloyan",
    age: 22
}

city(person);