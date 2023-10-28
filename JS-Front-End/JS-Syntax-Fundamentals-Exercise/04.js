function solve(n, m) {
    let l = []
    let sum = 0;

    for (let i = n; i <= m; i++) {
        l.push(i);
        sum += i;
    }

    console.log(l.join(' '));
    console.log(`Sum: ${sum}`);
}

solve(5, 10);