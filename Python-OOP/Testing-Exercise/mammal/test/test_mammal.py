from project.mammal import Mammal
from unittest import TestCase, main


class TestMammal(TestCase):
    def test_init(self):
        cow = Mammal("Boris", "Cow", "Moo")
        self.assertEqual("Boris", cow.name)
        self.assertEqual("Cow", cow.type)
        self.assertEqual("Moo", cow.sound)
        self.assertEqual("animals", cow.get_kingdom())

    def test_make_sound_method(self):
        cow = Mammal("Boris", "Cow", "Moo")
        self.assertEqual("Boris makes Moo", cow.make_sound())

    def test_get_kingdom_method(self):
        cow = Mammal("Boris", "Cow", "Moo")
        self.assertEqual("animals", cow.get_kingdom())

    def test_info_method(self):
        cow = Mammal("Boris", "Cow", "Moo")
        self.assertEqual("Boris is of type Cow", cow.info())


if __name__ == "__main__":
    main()
