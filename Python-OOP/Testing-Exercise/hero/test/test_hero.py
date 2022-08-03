from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def test_init(self):
        hero = Hero("KD", 121, 100, 20)
        self.assertEqual(hero.username, "KD")
        self.assertEqual(hero.level, 121)
        self.assertEqual(hero.health, 100)
        self.assertEqual(hero.damage, 20)

    def test_battle_error1(self):
        hero = Hero("KD", 121, 100, 20)
        enemy_hero = Hero("KD", 100, 100, 15)
        with self.assertRaises(Exception) as ex:
            hero.battle(enemy_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_error2(self):
        hero = Hero("KD", 121, 0, 20)
        enemy_hero = Hero("4ky", 100, 100, 15)
        with self.assertRaises(Exception) as ex:
            hero.battle(enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_error3(self):
        hero = Hero("KD", 121, 100, 20)
        enemy_hero = Hero("4ky", 100, 0, 15)

        with self.assertRaises(Exception) as ex:
            hero.battle(enemy_hero)
        self.assertEqual("You cannot fight 4ky. He needs to rest", str(ex.exception))

    def test_battle_if_draw(self):
        hero = Hero("KD", 1, 100, 200)
        enemy_hero = Hero("4ky", 1, 100, 200)

        self.assertEqual(hero.battle(enemy_hero), "Draw")

        self.assertEqual(hero.health, -100)
        self.assertEqual(enemy_hero.health, -100)

    def test_battle_if_I_win(self):
        hero = Hero("KD", 1, 100, 200)
        enemy_hero = Hero("4ky", 1, 100, 20)

        self.assertEqual(hero.battle(enemy_hero), "You win")

        self.assertEqual(hero.level, 2)
        self.assertEqual(hero.health, 85)
        self.assertEqual(hero.damage, 205)

    def test_battle_if_I_lose(self):
        hero = Hero("KD", 1, 100, 20)
        enemy_hero = Hero("4ky", 1, 100, 100)

        self.assertEqual(hero.battle(enemy_hero), "You lose")

        self.assertEqual(enemy_hero.level, 2)
        self.assertEqual(enemy_hero.health, 85)
        self.assertEqual(enemy_hero.damage, 105)

    def test_str(self):
        hero = Hero("KD", 1, 100, 20)
        self.assertEqual(f"Hero KD: 1 lvl\nHealth: 100\nDamage: 20\n", str(hero))


if __name__ == "__main__":
    main()
