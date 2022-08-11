from project.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):
    def test_name_error(self):
        with self.assertRaises(Exception) as ex:
            t = Team("LS League 1")
        self.assertEqual(str(ex.exception), "Team Name can contain only letters!")

    def test_add_member_method_case_one(self):
        t = Team("LSLeague")
        t.add_member(Slaven=10)
        self.assertEqual(t.add_member(Gosho=24, Petkan=0), "Successfully added: Gosho, Petkan")
        self.assertDictEqual(t.members, {"Slaven": 10, "Gosho": 24, "Petkan": 0})

    def test_add_member_method_case_two(self):
        t = Team("LSLeague")
        t.add_member(Slaven=10)
        self.assertEqual(t.add_member(Gosho=24, Slaven=0), "Successfully added: Gosho")
        self.assertDictEqual(t.members, {"Slaven": 10, "Gosho": 24})

    def test_remove_member_if_member_exists(self):
        t = Team("LSLeague")
        t.members = {"Gosho": 24, "Slaven": 10}
        self.assertEqual(t.remove_member("Gosho"), "Member Gosho removed")
        self.assertDictEqual(t.members, {"Slaven": 10})

    def test_remove_member_not_exist_message(self):
        t = Team("LSLeague")
        t.members = {"Gosho": 24, "Slaven": 10}
        self.assertEqual(t.remove_member("Petkan"), "Member with name Petkan does not exist")
        self.assertDictEqual(t.members, {"Gosho": 24, "Slaven": 10})

    def test_gt_magic_case_one(self):
        t1 = Team("LSLeague")
        t1.members = {"Petkan": 24, "Vladimir": 10, "Stoyan": 15}
        t2 = Team("MSLeague")
        t2.members = {"Gosho": 24, "Slaven": 10}

        self.assertTrue(t1 > t2)
        self.assertFalse(t2 > t1)

    def test_gt_magic_case_two(self):
        t1 = Team("LSLeague")
        t1.members = {"Gosho": 24, "Slaven": 10}
        t2 = Team("MSLeague")
        t2.members = {"Petkan": 24, "Vladimir": 10, "Stoyan": 15}

        self.assertTrue(t2 > t1)
        self.assertFalse(t1 > t2)

    def test_len_magic(self):
        t = Team("LSLeague")
        t.members = {"Gosho": 24, "Slaven": 10}

        self.assertEqual(len(t), 2)

    def test_magic_add(self):
        t1 = Team("LSLeague")
        t2 = Team("MSLeague")
        t1.add_member(Gosho=24, Petkan=0)
        t2.add_member(Slaven=45)

        new_team = t1 + t2

        self.assertEqual(new_team.name, "LSLeagueMSLeague")
        self.assertDictEqual(new_team.members, {"Gosho": 24, "Petkan": 0, "Slaven": 45})

    def test_magic_str(self):
        t = Team("LSLeague")
        t.add_member(Gosho=24, Slaven=10, Petkan=0, Mitko=0)

        expected = "Team name: LSLeague\nMember: Gosho - 24-years old\nMember: Slaven - 10-years old\nMember: Mitko - 0-years old\nMember: Petkan - 0-years old"
        self.assertEqual(str(t), expected)


if __name__ == "__main__":
    main()
