"""
A test module to validate the GUI class functionalities.

Author: Ziyad Alsaeed
Email: zalsaeed@qu.edu.sa
"""


import unittest

import tkinter as tk

from gui import GUI


class TestController(unittest.TestCase):

    def setUp(self) -> None:
        main_tk = tk.Tk()
        self.view = GUI(main_tk)

    def test_add_student(self):
        """Validate adding a student.
        """
        self.view.s_fn_entry.delete(0, tk.END)
        self.view.s_fn_entry.insert(0, "Ahmad")

        self.view.s_ln_entry.delete(0, tk.END)
        self.view.s_ln_entry.insert(0, "Adam")

        self.view.s_dob_entry.delete(0, tk.END)
        self.view.s_dob_entry.insert(0, "1999-1-10")

        self.view.s_id_entry.delete(0, tk.END)
        self.view.s_id_entry.insert(0, "999999999")
        self.assertEqual(f"Ahmad Adam 1999-1-10 999999999", self.view.add_student())

    def test_add_faculty(self):
        """Validate adding a faculty.
        """
        self.view.f_fn_entry.delete(0, tk.END)
        self.view.f_fn_entry.insert(0, "Ahmad")

        self.view.f_ln_entry.delete(0, tk.END)
        self.view.f_ln_entry.insert(0, "Adam")

        self.view.f_dob_entry.delete(0, tk.END)
        self.view.f_dob_entry.insert(0, "1999-1-10")

        self.view.f_office_entry.delete(0, tk.END)
        self.view.f_office_entry.insert(0, "999999999")
        self.assertEqual(f"Ahmad Adam 1999-1-10 999999999", self.view.add_faculty())

    def test_remove_person(self):
        """Validate removing a person.
        """
        self.view.remove_entry.delete(0, tk.END)
        self.view.remove_entry.insert(0, "SomeOne")
        self.assertEqual(f"SomeOne", self.view.remove_person())

    def test_list_people(self):
        """Validate updating the list of people.
        """
        people = []
        for i in range(3):
            people.append("FistName LastName 44 | Office 12")
        self.view.list_people(people)

        info = ""
        for p in people:
            info += f"{p}\n"

        self.assertEqual(info, self.view.person_list.get("1.0", tk.END)[0: -1])

    def test_show_error(self):
        """Validate the showing an error message.
        """
        self.view.show_error("Some error!")
        self.assertEqual("Some error!", self.view.error_label.cget("text"))
