
"""
A test module to validate the PersonList class functionalities.

Author: Ziyad Alsaeed
Email: zalsaeed@qu.edu.sa
"""


import unittest

from person import Faculty, Student
from persons import PersonList


class TestPersonList(unittest.TestCase):

    def setUp(self):
        self.faculty1 = Faculty("Osama", "Ibrahim", "1998-11-1", 350)

        self.student1 = Student("Ali", "Nader", "2002-04-10", 931991919)

    def test_append(self):
        """Validate that we can add to the people list
        """
        people = PersonList()
        people.append(self.faculty1)
        self.assertEqual(1, len(people.people))
        people.append(self.student1)
        self.assertEqual(2, len(people.people))

    def test_getting_people(self):
        """Validate that we can retrieve the people we added,
        and they are ordered
        """
        people = PersonList()
        people.append(self.student1)
        people.append(self.faculty1)
        self.assertEqual([self.faculty1, self.student1], people.get_people())

    def test_removing_someone_by_last_name(self):
        """Validate that we can remove someone by their
        last name or even the first part of it!
        """
        people = PersonList()
        people.append(self.faculty1)
        self.assertEqual(1, len(people.people))
        people.append(self.student1)
        self.assertEqual(2, len(people.people))

        people.remove("Nad")
        self.assertEqual(1, len(people.people))


if __name__ == '__main__':
    unittest.main()
