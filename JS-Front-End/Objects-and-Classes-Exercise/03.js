function storeProvision(firstArray, secondArray) {
    let storeObject = {};

    function toStoreObject(array) {
        let currentArray = array;

        while (array.length > 0) {
            let arrayKey = currentArray.shift();
            let arrayValue = Number(currentArray.shift());

            if (storeObject.hasOwnProperty(arrayKey)) {
                storeObject[arrayKey] += arrayValue;
                continue;
            }

            storeObject[arrayKey] = arrayValue;
        }
    }

    toStoreObject(firstArray);
    toStoreObject(secondArray);

    for (let [key, value] of Object.entries(storeObject)) {
        console.log(`${key} -> ${value}`);
    }
}