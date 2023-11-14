function addAndSubtract(n1, n2, n3) {
    function sum(n1, n2) {
        return n1 + n2;
    }

    function subtract(sum, n3) {
        return sum - n3;
    }

    console.log(subtract(sum(n1, n2), n3));
}

addAndSubtract(42, 58, 100);