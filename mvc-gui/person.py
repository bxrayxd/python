"""
A Person Class and all its descendents.

In the case of MVC, this is our MVC. In real projects.
It is much more complicated than this. However, we only
want to demonstrate that it manages the data.

Author: Ziyad Alsaeed
Email: zalsaeed@qu.edu.sa
"""

from datetime import datetime
import utility


class Person:
    def __init__(self, firstname: str, lastname: str, date_of_birth: str):
        """
        Initialize a persons object. Although the date_of_birth is of type str,
        the initializer here should take care of converting it to datetime object.

        Hint: Fix what is in the util file!

        :param firstname: The person's first name.
        :param lastname: The person's last name.
        :param date_of_birth: The person's date of birth as a string.
        """
        self._first_name = firstname
        self._last_name = lastname
        # TODO: Fix Me! The _dob should take a datetime object based on the passed string.
        self._dob = utility.convert_string_to_datetime(date_of_birth)

    def get_name(self) -> str:
        """
        Format the name such that the last name appears before the first name.
        Example, my name should be written as 'Alsaeed, Ziyad'.
        :return: A string of the full name where the last name appears first, and they are seperated by a comma.
        """
        # TODO: Fix Me!
        full_name = f"{self._last_name}, {self._first_name}"
        return full_name

    def get_age(self) -> int:
        """
        Calculate the age of the person given today's date and their date of birth.
        Hint: there are 365.2425 days in a year!
        :return: The age of the person in years as an integer.
        """
        # TODO: Fix Me!
        today = datetime.now()
        age = (
            today.year
            - self._dob.year
            - ((today.month, today.day) < (self._dob.month, self._dob.day))
        )
        return age

    def __str__(self):
        """
        Format the object to print the full name with the age all together.
        :return:
        """
        return f"{self.get_name()}: {self.get_age()}"


class Faculty(Person):
    def __init__(self, firstname: str, lastname: str, date_of_birth: str, office: int):
        super().__init__(
            firstname=firstname, lastname=lastname, date_of_birth=date_of_birth
        )
        self._office = office

    def get_office_number(self) -> int:
        """
        Get the faculty office number!
        """
        # TODO: Fix Me!
        return self._office

    def __str__(self):
        return f"Faculty: {super().__str__()} | Office: {self.get_office_number()}"


class Student(Person):
    def __init__(self, firstname: str, lastname: str, date_of_birth: str, sid: int):
        super().__init__(
            firstname=firstname, lastname=lastname, date_of_birth=date_of_birth
        )
        self._sid = sid

    def get_student_id(self) -> int:
        """
        Get the student's id number!
        """
        # TODO: Fix Me!
        return self._sid

    def __str__(self):
        return f"Student: {super().__str__()} | SID: {self.get_student_id()}"
