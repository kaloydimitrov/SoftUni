from project.movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):
    def test_init(self):
        movie = Movie("The Matrix", 1999, 9)
        self.assertEqual(movie.name, "The Matrix")
        self.assertEqual(movie.year, 1999)
        self.assertEqual(movie.rating, 9)

    def test_name_exception(self):
        movie = Movie("The Matrix", 1999, 9)
        with self.assertRaises(Exception) as ex:
            movie.name = ""
        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test_year_exception(self):
        movie = Movie("The Matrix", 1999, 9)
        with self.assertRaises(Exception) as ex:
            movie.year = 1
        self.assertEqual("Year is not valid!", str(ex.exception))

    def test_add_actor_append(self):
        movie = Movie("The Matrix", 1999, 9)
        movie.actors.append("Some Dude")
        movie.add_actor("Jim Carry")

        self.assertListEqual(movie.actors, ["Some Dude", "Jim Carry"])

    def test_add_actor_append_message(self):
        movie = Movie("The Matrix", 1999, 9)
        movie.actors.append("Some Dude")

        self.assertEqual(movie.add_actor("Some Dude"), "Some Dude is already added in the list of actors!")

    def test_thunder_method(self):
        movie1 = Movie("The Matrix", 1999, 9)
        movie2 = Movie("The Matrix: part 2", 2006, 7)

        self.assertEqual(movie1 > movie2, '"The Matrix" is better than "The Matrix: part 2"')

    def test_thunder_method_reverse(self):
        movie1 = Movie("The Matrix", 1999, 9)
        movie2 = Movie("The Matrix: part 2", 2006, 10)

        self.assertEqual(movie1 > movie2, '"The Matrix: part 2" is better than "The Matrix"')

    def test_repr(self):
        movie = Movie("The Matrix", 1999, 9)
        movie.actors.append("Jim Carry")
        movie.actors.append("Some Dude")

        expected = f"Name: The Matrix\n" \
                   f"Year of Release: 1999\n" \
                   f"Rating: 9.00\n" \
                   f"Cast: Jim Carry, Some Dude"

        self.assertEqual(expected, str(movie))


if __name__ == "__main__":
    main()
