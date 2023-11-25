function songs(array) {
    class Song {
        constructor(type, name, time) {
            this.type = type;
            this.name = name;
            this.time = time;
        }
    }

    let songObjects = []; 
    let songsArray = array;
    
    songsArray.shift();
    let songType = songsArray.pop();

    for (let item of songsArray) {
        let [type, name, time] = item.split("_");
        songObjects.push(new Song(type, name, time));
    }

    if (songType == "all") {
        for (let object of songObjects) {
            console.log(object.name);
        }
    }
    else {
        for (let object of songObjects) {
            if (object.type == songType) {
                console.log(object.name);
            }
        }
    }
}

songs([3, 'favourite_DownTown_3:14', 'favourite_Kiss_4:16', 'favourite_Smooth Criminal_4:01', 'favourite']);