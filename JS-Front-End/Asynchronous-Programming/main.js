const urlEndpoint = 'https://catfact.ninja/fact';

// ------------------------- First Way -------------------------

fetch(urlEndpoint)
    .then((res) => res.json())
    .then((factObject) => {
        console.log(`(Length: ${Object.values(factObject)[1]}) Fact: ${Object.values(factObject)[0]}`);
    })
    .catch((err) => console.log(err))

// ------------------------- Second Way -------------------------

async function getFact() {
    try {
        const res = await (await fetch(urlEndpoint));
        const factObject = await res.json();

        console.log(`(Length: ${Object.values(factObject)[1]}) Fact: ${Object.values(factObject)[0]}`);
    } catch (err) {
        console.log(err);
    }
}

getFact();