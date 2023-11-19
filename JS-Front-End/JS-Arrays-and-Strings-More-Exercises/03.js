function thePyramidOfKingDjoser(base, increment) {
    let currentStep = 1;

    let stone = 0; // Inner Layer
    let marble = 0; // Outer Layer
    let lapisLazuli = 0;
    let gold = 0;

    for (let i = base; i > 0; i -= 2) {
        let area = i * i;
        let outerLayer = i * 4 - 4;
        let innerLayer = area - outerLayer;

        if (i == 1 || i == 2) {
            gold += (i * i) * increment;
        }
        else if (currentStep % 5 == 0) {
            stone += innerLayer * increment;
            lapisLazuli += outerLayer * increment;
        }
        else {
            stone += innerLayer * increment;
            marble += outerLayer * increment;
        }

        currentStep += 1;
    }

    console.log(`Stone required: ${Math.ceil(stone)}`);
    console.log(`Marble required: ${Math.ceil(marble)}`);
    console.log(`Lapis Lazuli required: ${Math.ceil(lapisLazuli)}`);
    console.log(`Gold required: ${Math.ceil(gold)}`);
    console.log(`Final pyramid height: ${Math.floor((currentStep - 1) * increment)}`);
}

thePyramidOfKingDjoser(23, 0.5);