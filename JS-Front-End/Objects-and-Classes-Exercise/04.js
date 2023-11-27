function movies(moviesArray) {
    let movieObjects = [];

    for (let movieString of moviesArray) {
        if (movieString.includes("addMovie")) {
            let [blank, movieName] = movieString.split("addMovie ");

            movieObjects.push({ name: movieName });
        } else if (movieString.includes("directedBy")) {
            let [movieName, director] = movieString.split(" directedBy ");
            
            for (let movieObject of movieObjects) {
                if (movieObject.name == movieName) {
                    movieObject.director = director;
                }
            }
        } else if (movieString.includes("onDate")) {
            let [movieName, date] = movieString.split(" onDate ");

            for (let movieObject of movieObjects) {
                if (movieObject.name == movieName) {
                    movieObject.date = date;
                }
            }
        }
    }

    for (let object of movieObjects) {
        if (Object.keys(object).length == 3) {
            console.log(JSON.stringify(object));
        }
    }
}

movies(['addMovie Fast and Furious', 'addMovie Godfather', 'Inception directedBy Christopher Nolan', 'Godfather directedBy Francis Ford Coppola', 'Godfather onDate 29.07.2018', 'Fast and Furious onDate 30.07.2018', 'Batman onDate 01.08.2018', 'Fast and Furious directedBy Rob Cohen']);