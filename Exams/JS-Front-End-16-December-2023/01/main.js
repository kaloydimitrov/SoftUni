function cafeteria(input) {
    const n = Number(input.shift());
    const baristas = {};

    for (let i = 0; i < n; i++) {
        const [name, shift, drinks] = input[i].split(' ');
        baristas[name] = {
            shift,
            drinks: drinks.split(',')
        };
    }

    let index = n;
    while (input[index] !== 'Closed') {
        const command = input[index];
        const [action, name, ...args] = command.split(' / ');

        switch (action) {
            case 'Prepare':
                const shift = args[0];
                const coffeeType = args[1];
                if (baristas[name].shift === shift && baristas[name].drinks.includes(coffeeType)) {
                    console.log(`${name} has prepared a ${coffeeType} for you!`);
                } else {
                    console.log(`${name} is not available to prepare a ${coffeeType}.`);
                }
                break;

            case 'Change Shift':
                const newShift = args[0];
                baristas[name].shift = newShift;
                console.log(`${name} has updated his shift to: ${newShift}`);
                break;

            case 'Learn':
                const newCoffeeType = args[0];
                if (baristas[name].drinks.includes(newCoffeeType)) {
                    console.log(`${name} knows how to make ${newCoffeeType}.`);
                } else {
                    baristas[name].drinks.push(newCoffeeType);
                    console.log(`${name} has learned a new coffee type: ${newCoffeeType}.`);
                }
                break;

            default:
                console.log('Invalid command');
        }

        index++;
    }

    for (const [name, info] of Object.entries(baristas)) {
        const { shift, drinks } = info;
        console.log(`Barista: ${name}, Shift: ${shift}, Drinks: ${drinks.join(', ')}`);
    }
}

cafeteria([
    '3',
    'Alice day Espresso,Cappuccino',
    'Bob night Latte,Mocha',
    'Carol day Americano,Mocha',
    'Prepare / Alice / day / Espresso',
    'Change Shift / Bob / night',
    'Learn / Carol / Latte',
    'Learn / Bob / Latte',
    'Prepare / Bob / night / Latte',
    'Closed'
]);

cafeteria([
    '4',
    'Alice day Espresso,Cappuccino',
    'Bob night Latte,Mocha',
    'Carol day Americano,Mocha',
    'David night Espresso',
    'Prepare / Alice / day / Espresso',
    'Change Shift / Bob / day',
    'Learn / Carol / Latte',
    'Prepare / Bob / night / Latte',
    'Learn / David / Cappuccino',
    'Prepare / Carol / day / Cappuccino',
    'Change Shift / Alice / night',
    'Learn / Bob / Mocha',
    'Prepare / David / night / Espresso',
    'Closed'
]);