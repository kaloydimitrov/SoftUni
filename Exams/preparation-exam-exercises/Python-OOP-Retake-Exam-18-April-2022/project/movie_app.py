from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def __find_user_by_username(self, username):
        for user in self.users_collection:
            if user.username == username:
                return user

    def __user_not_the_owner(self, user, movie):
        if user in self.users_collection and movie.owner != user:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")

    def __movie_not_uploaded(self, movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

    def check_if_user_exists(self, username):
        for user in self.users_collection:
            if user.username == username:
                return True
        return False

    def check_if_movie_exists(self, title):
        for movie in self.movies_collection:
            if movie.title == title:
                return True
        return False

    def check_if_user_liked_movie(self, username, movie_title):
        for user in self.users_collection:
            if user.username == username:
                for movie in user.movies_liked:
                    if movie.title == movie_title:
                        return True
                return False

    def register_user(self, username: str, age: int):
        if username in [u.username for u in self.users_collection]:
            raise Exception("User already exists!")

        user = User(username, age)
        self.users_collection.append(user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = self.__find_user_by_username(username)

        if user not in self.users_collection:
            raise Exception("This user does not exist!")
        self.__user_not_the_owner(user, movie)
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = self.__find_user_by_username(username)

        self.__movie_not_uploaded(movie)
        self.__user_not_the_owner(user, movie)

        for key, value in kwargs.items():
            if key == "title":
                movie.title = value
            if key == "year":
                movie.year = value
            if key == "age_restriction":
                movie.age_restriction = value

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = self.__find_user_by_username(username)

        self.__movie_not_uploaded(movie)
        self.__user_not_the_owner(user, movie)

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.__find_user_by_username(username)

        if movie.owner == user:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.__find_user_by_username(username)

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):

        if not self.movies_collection:
            return "No movies found."

        result = ""

        sort = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))

        for movie in sort:
            result += movie.details() + "\n"

        return result.strip()

    def __str__(self):
        result = ""

        if not self.users_collection:
            result += "All users: No users." + "\n"
        else:
            result += f"All users: {', '.join([u.username for u in self.users_collection])}" + "\n"
        if not self.movies_collection:
            result += "All movies: No movies." + "\n"
        else:
            result += f"All movies: {', '.join([m.title for m in self.movies_collection])}" + "\n"

        return result.strip()
