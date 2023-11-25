console.log("-------------- Objects --------------");

let firstObject = {
    firstName: "Kaloyan",
    secondName: "Dimitrov",
    age: 23,

    sound: function(text) {
        return `Whoom! ${text}`;
    },

    info: function() { return `INFO: ${this.firstName}; ${this.secondName}; ${this.age}` }
}

let secondObject = Object.create(firstObject);
secondObject.firstName = "Georgi";
secondObject.secondName = "Dimitrov";
secondObject.age = 12;
secondObject.sound = (text) => `Broom! ${text}`;
secondObject.sex = "Male";
secondObject["sex"] = "Female";
console.log(firstObject.hasOwnProperty("sex"));
console.log(secondObject.hasOwnProperty("sex"));

console.log(firstObject, firstObject.sound("gsrthd"));
console.log(secondObject, secondObject.sound("hsrth"));

for (let key in secondObject) {
    console.log(`${key}: ${secondObject[key]}`);
}

for (const entry of Object.entries(secondObject)) {
    console.log(entry);
}

console.log(firstObject.info());
console.log(secondObject.info());

console.log("Delete property:");
let thirdObject = {
    name: "Gosho",
    age: 22
}

console.log(thirdObject);

delete thirdObject.age;

console.log(thirdObject);

delete thirdObject["name"];

console.log(thirdObject);

console.log("-------------- Classes --------------");

class People {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    getInfo() {
        return `Name: ${this.name}` + "\n" + `Age: ${this.age}`;
    }
}

let p1 = new People("Kaloyan", 12);
console.log(p1.name);
console.log(p1.age);
console.log(p1.getInfo());

console.log("-------------- Lists --------------");

l = [1, 2, 3, 4, 5];

console.log("For-of:");
for (let item of l) {
    console.log(item);
}

console.log("For-in:");
for (let item in l) {
    console.log(item);
}

console.log("For-each:");
l.forEach((item) => console.log(item ** 2));