"""
A test module to validate the Person class functionalities.

Author: Ziyad Alsaeed
Email: zalsaeed@qu.edu.sa
"""

import unittest
from datetime import datetime

from person import Faculty, Student


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.faculty1 = Faculty("Osama", "Ibrahim", "1998-11-1", 350)

        self.student1 = Student("Ali", "Nader", "2002-04-10", 931991919)

    def test_initialization(self):
        """Validate that all objects initialize as expected."""

        # test a faculty
        self.assertEqual("Osama", self.faculty1._first_name)
        self.assertEqual("Ibrahim", self.faculty1._last_name)
        self.assertEqual(datetime(1998, 11, 1), self.faculty1._dob)
        self.assertEqual(350, self.faculty1._office)

        # test a student
        self.assertEqual("Ali", self.student1._first_name)
        self.assertEqual("Nader", self.student1._last_name)
        self.assertEqual(datetime(2002, 4, 10), self.student1._dob)
        self.assertEqual(931991919, self.student1._sid)

    def test_get_full_name(self):
        """Validate the full name is printed as expected."""
        self.assertEqual("Ibrahim, Osama", self.faculty1.get_name())
        self.assertEqual("Nader, Ali", self.student1.get_name())

    def test_get_age(self):
        """Validate the age calculations."""
        self.assertEqual(26, self.faculty1.get_age())
        self.assertEqual(23, self.student1.get_age())

    def test_str(self):
        """Validate the prints of the objects"""
        self.assertEqual(
            "Faculty: Ibrahim, Osama: 26 | Office: 350", str(self.faculty1)
        )
        self.assertEqual(
            "Student: Nader, Ali: 23 | SID: 931991919", str(self.student1))

    def test_get_office_number(self):
        """Validate the return of the office number"""
        self.assertEqual(350, self.faculty1.get_office_number())

    def test_get_sid_number(self):
        """Validate the return of the student id"""
        self.assertEqual(931991919, self.student1.get_student_id())


if __name__ == "__main__":
    unittest.main()
