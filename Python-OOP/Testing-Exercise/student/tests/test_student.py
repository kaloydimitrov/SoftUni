from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):
    def test_init1(self):
        s = Student("Stoyan")

        self.assertEqual(s.name, "Stoyan")
        self.assertEqual(s.courses, {})

    def test_init2(self):
        s = Student("Stoyan", {"course1": ["note1", "note2"]})

        self.assertEqual(s.name, "Stoyan")
        self.assertDictEqual(s.courses, {"course1": ["note1", "note2"]})

    def test_enroll_message1(self):
        s = Student("Stoyan", {"course1": ["note1", "note2", "note3"]})

        self.assertEqual(s.enroll("course1", ["note4", "note5"], "Z"), "Course already added. Notes have been updated.")
        self.assertDictEqual(s.courses, {"course1": ["note1", "note2", "note3", "note4", "note5"]})

    def test_enroll_message2(self):
        s = Student("Stoyan", {"course1": ["note1", "note2"]})

        self.assertEqual(s.enroll("course2", ["note1", "note2"], "Y"), "Course and course notes have been added.")
        self.assertDictEqual(s.courses, {"course1": ["note1", "note2"], "course2": ["note1", "note2"]})

    def test_enroll_message3(self):
        s = Student("Stoyan", {})

        self.assertEqual(s.enroll("course1", ["note1", "note2"], "Z"), "Course has been added.")
        self.assertDictEqual(s.courses, {"course1": []})

    def test_add_notes(self):
        s = Student("Stoyan", {"course1": ["note1", "note2", "note3"], "course2": ["note1"]})
        self.assertEqual(s.add_notes("course2", "note2"), "Notes have been updated")
        self.assertDictEqual(s.courses, {"course1": ["note1", "note2", "note3"], "course2": ["note1", "note2"]})

    def test_add_notes_error(self):
        s = Student("Stoyan", {"course1": ["note1", "note2", "note3"]})
        with self.assertRaises(Exception) as ex:
            s.add_notes("course3", "note1")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course(self):
        s = Student("Stoyan", {"course1": ["note1", "note2", "note3"], "course2": ["note1"]})
        self.assertEqual(s.leave_course("course1"), "Course has been removed")
        self.assertDictEqual(s.courses, {"course2": ["note1"]})

    def test_leave_course_error(self):
        s = Student("Stoyan", {"course1": ["note1", "note2", "note3"]})
        with self.assertRaises(Exception) as ex:
            s.leave_course("course3")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
