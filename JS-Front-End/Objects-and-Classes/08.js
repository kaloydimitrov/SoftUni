function cats(array) {
    class cat {
        constructor(name, age) {
            this.name = name;
            this.age = age;
        }

        meow() {
            console.log(`${this.name}, age ${this.age} says Meow`);
        }
    }

    let objects = [];

    for (let item of array) {
        let [name, age] = item.split(" ");
        objects.push(new cat(name, age));
    }

    for (let object of objects) {
        object.meow();
    }
}

cats(['Mellow 2', 'Tom 5']);