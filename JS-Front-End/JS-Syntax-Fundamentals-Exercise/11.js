function solve(speed, area) {
    let speedLimit = 0;

    switch(area) {
        case "motorway":
            speedLimit = 130;
            break;
        case "interstate":
            speedLimit = 90;
            break;
        case "city":
            speedLimit = 50;
            break;
        case "residential":
            speedLimit = 20;
            break;
    }

    if (speed > speedLimit) {
        let status = "reckless driving";
        
        if (speed <= speedLimit + 20) {
            status = "speeding";
        }
        else if (speed <= speedLimit + 40) {
            status = "excessive speeding";
        }

        console.log(`The speed is ${speed - speedLimit} km/h faster than the allowed speed of ${speedLimit} - ${status}`);
    }
    else {
        console.log(`Driving ${speed} km/h in a ${speedLimit} zone`);
    }
}

solve(120, "interstate");