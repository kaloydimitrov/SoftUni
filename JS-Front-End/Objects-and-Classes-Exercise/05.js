function inventory(inputArray) {
    let heros = [];

    for (let inputString of inputArray) {
        let [Hero, level, items] = inputString.split(" / ");
        heros.unshift({ Hero, level, items });
    }

    heros.sort(function(a, b) {
        return a.level - b.level;
    });

    for (let hero of heros) {
        console.log(`Hero: ${hero.Hero}`);
        console.log(`level => ${hero.level}`);
        console.log(`items => ${hero.items}`);
    }
}

inventory(['Batman / 2 / Banana, Gun', 'Superman / 18 / Sword', 'Poppy / 28 / Sentinel, Antara']);