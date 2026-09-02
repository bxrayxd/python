"""
A test module to validate the Controller class functionalities.

Author: Ziyad Alsaeed
Email: zalsaeed@qu.edu.sa
"""


import unittest

import tkinter as tk

from controller import Controller
from gui import GUI
from persons import PersonList


class TestController(unittest.TestCase):

    def setUp(self):
        self.c = Controller()

    def test_initialization(self):
        """Validating the initialization
        """
        self.assertIsInstance(self.c._persons, PersonList)
        self.assertIsInstance(self.c._view, GUI)
        self.c.main_tk.quit()
        self.c.main_tk.destroy()

    def test_add_student(self):
        """Validate we can add a student.
        """
        self.assertEqual(0, len(self.c._persons.people))
        self.c._view.s_fn_entry.delete(0, tk.END)
        self.c._view.s_fn_entry.insert(0, "Ahmad")

        self.c._view.s_ln_entry.delete(0, tk.END)
        self.c._view.s_ln_entry.insert(0, "Adam")

        self.c._view.s_dob_entry.delete(0, tk.END)
        self.c._view.s_dob_entry.insert(0, "1999-1-10")

        self.c._view.s_id_entry.delete(0, tk.END)
        self.c._view.s_id_entry.insert(0, "999999999")

        self.c.add_student()
        self.assertEqual(1, len(self.c._persons.people))

    def test_add_student_go_wrong(self):
        """Validate wrongly added information.
        """
        self.assertEqual(0, len(self.c._persons.people))

        self.c._view.s_fn_entry.delete(0, tk.END)
        self.c._view.s_fn_entry.insert(0, "Ahmad")

        self.c._view.s_ln_entry.delete(0, tk.END)
        self.c._view.s_ln_entry.insert(0, "Adam")

        self.c._view.s_dob_entry.delete(0, tk.END)
        self.c._view.s_dob_entry.insert(0, "1999-1-10")
        self.c.add_student()

        self.assertEqual(0, len(self.c._persons.people))

    def test_add_student_clear_error_message(self):
        """Validate the error message clearance
        """
        self.c._view.s_fn_entry.delete(0, tk.END)
        self.c._view.s_fn_entry.insert(0, "Ahmad")

        self.c._view.s_ln_entry.delete(0, tk.END)
        self.c._view.s_ln_entry.insert(0, "Adam")

        self.c._view.s_dob_entry.delete(0, tk.END)
        self.c._view.s_dob_entry.insert(0, "1999-1-10")

        self.c._view.s_id_entry.delete(0, tk.END)
        self.c._view.s_id_entry.insert(0, "999999999")
        self.c.add_student()

        self.assertEqual("", self.c._view.error_label.cget("text"))

    def test_add_student_return_error_message(self):
        """Validate showing the error message.
        """
        self.c._view.s_fn_entry.delete(0, tk.END)
        self.c._view.s_fn_entry.insert(0, "Ahmad")

        self.c._view.s_ln_entry.delete(0, tk.END)
        self.c._view.s_ln_entry.insert(0, "Adam")

        self.c._view.s_dob_entry.delete(0, tk.END)
        self.c._view.s_dob_entry.insert(0, "1999-1-10")
        self.c.add_student()

        self.assertNotEqual("", self.c._view.error_label.cget("text"))

    def test_add_student_people_list_update(self):
        """Validate the list of people in the view
        is updated after adding a student.
        """
        current_info = self.c._view.person_list.get("1.0", tk.END)

        self.c._view.s_fn_entry.delete(0, tk.END)
        self.c._view.s_fn_entry.insert(0, "Ahmad")

        self.c._view.s_ln_entry.delete(0, tk.END)
        self.c._view.s_ln_entry.insert(0, "Adam")

        self.c._view.s_dob_entry.delete(0, tk.END)
        self.c._view.s_dob_entry.insert(0, "1999-1-10")

        self.c._view.s_id_entry.delete(0, tk.END)
        self.c._view.s_id_entry.insert(0, "999999999")

        self.c.add_student()
        self.assertNotEqual(current_info, self.c._view.person_list.get("1.0", tk.END))

    def test_add_faculty(self):
        """Validate we can add a faculty.
        """
        self.assertEqual(0, len(self.c._persons.people))

        self.c._view.f_fn_entry.delete(0, tk.END)
        self.c._view.f_fn_entry.insert(0, "Ahmad")

        self.c._view.f_ln_entry.delete(0, tk.END)
        self.c._view.f_ln_entry.insert(0, "Adam")

        self.c._view.f_dob_entry.delete(0, tk.END)
        self.c._view.f_dob_entry.insert(0, "1999-1-10")

        self.c._view.f_office_entry.delete(0, tk.END)
        self.c._view.f_office_entry.insert(0, "999999999")

        self.c.add_faculty()
        self.assertEqual(1, len(self.c._persons.people))

    def test_add_faculty_go_wrong(self):
        """Validate wrongly added information.
        """
        self.assertEqual(0, len(self.c._persons.people))

        self.c._view.f_fn_entry.delete(0, tk.END)
        self.c._view.f_fn_entry.insert(0, "Ahmad")

        self.c._view.f_ln_entry.delete(0, tk.END)
        self.c._view.f_ln_entry.insert(0, "Adam")

        self.c._view.f_dob_entry.delete(0, tk.END)
        self.c._view.f_dob_entry.insert(0, "1999-1-10")

        self.c.add_faculty()

        self.assertEqual(0, len(self.c._persons.people))

    def test_add_faculty_clear_error_message(self):
        """Validate the error message clearance
        """
        self.c._view.f_fn_entry.delete(0, tk.END)
        self.c._view.f_fn_entry.insert(0, "Ahmad")

        self.c._view.f_ln_entry.delete(0, tk.END)
        self.c._view.f_ln_entry.insert(0, "Adam")

        self.c._view.f_dob_entry.delete(0, tk.END)
        self.c._view.f_dob_entry.insert(0, "1999-1-10")

        self.c._view.f_office_entry.delete(0, tk.END)
        self.c._view.f_office_entry.insert(0, "999999999")

        self.c.add_faculty()

        self.assertEqual("", self.c._view.error_label.cget("text"))

    def test_add_faculty_return_error_message(self):
        """Validate showing the error message.
        """
        self.c._view.f_fn_entry.delete(0, tk.END)
        self.c._view.f_fn_entry.insert(0, "Ahmad")

        self.c._view.f_ln_entry.delete(0, tk.END)
        self.c._view.f_ln_entry.insert(0, "Adam")

        self.c._view.f_dob_entry.delete(0, tk.END)
        self.c._view.f_dob_entry.insert(0, "1999-1-10")

        self.c.add_faculty()

        self.assertNotEqual("", self.c._view.error_label.cget("text"))

    def test_add_faculty_people_list_update(self):
        """Validate the list of people in the view is updated
        after adding a faculty.
        """
        current_info = self.c._view.person_list.get("1.0", tk.END)

        self.c._view.f_fn_entry.delete(0, tk.END)
        self.c._view.f_fn_entry.insert(0, "Ahmad")

        self.c._view.f_ln_entry.delete(0, tk.END)
        self.c._view.f_ln_entry.insert(0, "Adam")

        self.c._view.f_dob_entry.delete(0, tk.END)
        self.c._view.f_dob_entry.insert(0, "1999-1-10")

        self.c._view.f_office_entry.delete(0, tk.END)
        self.c._view.f_office_entry.insert(0, "999999999")

        self.c.add_faculty()
        self.assertNotEqual(current_info, self.c._view.person_list.get("1.0", tk.END))

    def test_remove_existing_person(self):
        """Validate removing existing person
        """
        self.assertEqual(0, len(self.c._persons.people))

        # first person
        self.c._view.f_fn_entry.delete(0, tk.END)
        self.c._view.f_fn_entry.insert(0, "Ahmad")

        self.c._view.f_ln_entry.delete(0, tk.END)
        self.c._view.f_ln_entry.insert(0, "LastName")

        self.c._view.f_dob_entry.delete(0, tk.END)
        self.c._view.f_dob_entry.insert(0, "1999-1-10")

        self.c._view.f_office_entry.delete(0, tk.END)
        self.c._view.f_office_entry.insert(0, "999999999")
        self.c.add_faculty()

        # another person
        self.c._view.f_fn_entry.delete(0, tk.END)
        self.c._view.f_fn_entry.insert(0, "Ahmad")

        self.c._view.f_ln_entry.delete(0, tk.END)
        self.c._view.f_ln_entry.insert(0, "OtherLastName")

        self.c._view.f_dob_entry.delete(0, tk.END)
        self.c._view.f_dob_entry.insert(0, "1999-1-10")

        self.c._view.f_office_entry.delete(0, tk.END)
        self.c._view.f_office_entry.insert(0, "999999999")
        self.c.add_faculty()

        self.assertEqual(2, len(self.c._persons.people))

        self.c._view.remove_entry.delete(0, tk.END)
        self.c._view.remove_entry.insert(0, "LastName")
        self.c.remove_person()

        self.assertEqual(1, len(self.c._persons.people))

    def test_remove_non_existing_person(self):
        """Validate removing non-existing person.
        Nothing should be removed.
        """
        self.assertEqual(0, len(self.c._persons.people))

        # first person
        self.c._view.f_fn_entry.delete(0, tk.END)
        self.c._view.f_fn_entry.insert(0, "Ahmad")

        self.c._view.f_ln_entry.delete(0, tk.END)
        self.c._view.f_ln_entry.insert(0, "LastName")

        self.c._view.f_dob_entry.delete(0, tk.END)
        self.c._view.f_dob_entry.insert(0, "1999-1-10")

        self.c._view.f_office_entry.delete(0, tk.END)
        self.c._view.f_office_entry.insert(0, "999999999")
        self.c.add_faculty()

        # another person
        self.c._view.f_fn_entry.delete(0, tk.END)
        self.c._view.f_fn_entry.insert(0, "Ahmad")

        self.c._view.f_ln_entry.delete(0, tk.END)
        self.c._view.f_ln_entry.insert(0, "OtherLastName")

        self.c._view.f_dob_entry.delete(0, tk.END)
        self.c._view.f_dob_entry.insert(0, "1999-1-10")

        self.c._view.f_office_entry.delete(0, tk.END)
        self.c._view.f_office_entry.insert(0, "999999999")
        self.c.add_faculty()

        self.assertEqual(2, len(self.c._persons.people))

        self.c._view.remove_entry.delete(0, tk.END)
        self.c._view.remove_entry.insert(0, "NotThere")
        self.c.remove_person()

        self.assertEqual(2, len(self.c._persons.people))

        self.c._view.remove_entry.delete(0, tk.END)
        self.c._view.remove_entry.insert(0, "")
        self.c.remove_person()

        self.assertEqual(2, len(self.c._persons.people))

    def test_remove_existing_person_update_people_list(self):
        """Validate updating the people list in the view
        after removing an existing person.
        """
        current_info = self.c._view.person_list.get("1.0", tk.END)

        # first person
        self.c._view.f_fn_entry.delete(0, tk.END)
        self.c._view.f_fn_entry.insert(0, "Ahmad")

        self.c._view.f_ln_entry.delete(0, tk.END)
        self.c._view.f_ln_entry.insert(0, "LastName")

        self.c._view.f_dob_entry.delete(0, tk.END)
        self.c._view.f_dob_entry.insert(0, "1999-1-10")

        self.c._view.f_office_entry.delete(0, tk.END)
        self.c._view.f_office_entry.insert(0, "999999999")
        self.c.add_faculty()

        # another person
        self.c._view.f_fn_entry.delete(0, tk.END)
        self.c._view.f_fn_entry.insert(0, "Ahmad")

        self.c._view.f_ln_entry.delete(0, tk.END)
        self.c._view.f_ln_entry.insert(0, "OtherLastName")

        self.c._view.f_dob_entry.delete(0, tk.END)
        self.c._view.f_dob_entry.insert(0, "1999-1-10")

        self.c._view.f_office_entry.delete(0, tk.END)
        self.c._view.f_office_entry.insert(0, "999999999")
        self.c.add_faculty()

        self.c._view.remove_entry.delete(0, tk.END)
        self.c._view.remove_entry.insert(0, "LastName")
        self.c.remove_person()

        self.assertNotEqual(current_info, self.c._view.person_list.get("1.0", tk.END))
