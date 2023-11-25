function meetings(array) {
    let meeetingObject = {};
    
    for (let element of array) {
        let [key, value] = element.split(" ");

        if (meeetingObject.hasOwnProperty(key)) {
            console.log(`Conflict on ${key}!`);
            continue;
        }

        meeetingObject[key] = value;
        console.log(`Scheduled for ${key}`);
    }

    for (let [key, value] of Object.entries(meeetingObject)) {
        console.log(`${key} -> ${value}`);
    }
}

meetings(['Monday Peter', 'Wednesday Bill', 'Monday Tim', 'Friday Tim']);