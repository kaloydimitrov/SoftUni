function solve(fruit, weight, price) {
    let newWeight = weight * 0.001;

    console.log(`I need $${(newWeight * price).toFixed(2)} to buy ${newWeight.toFixed(2)} kilograms ${fruit}.`);
}

solve("apple", 1563, 2.35);