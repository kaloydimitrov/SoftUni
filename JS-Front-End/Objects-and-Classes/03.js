function jsonToObject(json) {
    let jsonObject = JSON.parse(json);

    for (let [key, value] of Object.entries(jsonObject)) {
        console.log(`${key}: ${value}`);
    }
}

jsonToObject('{"name": "George", "age": 40, "town": "Sofia"}');