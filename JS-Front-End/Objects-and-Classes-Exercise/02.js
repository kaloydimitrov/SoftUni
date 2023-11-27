function towns(array) {
    for (let item of array) {
        let [town, latitude, longitude] = item.split(" | ");
        latitude = Number(latitude).toFixed(2);
        longitude = Number(longitude).toFixed(2);

        let currentObject = {
            town,
            latitude,
            longitude
        }

        console.log(currentObject);
    }
}