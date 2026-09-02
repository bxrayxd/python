"""
The view module. It doesn't control how the data is processed
it only manage how it looks and the user interactions.

Author: Ziyad Alsaeed
Email: zalsaeed@qu.edu.sa
"""

from typing import Callable
import tkinter as tk

import logging


class GUI:
    def __init__(self, main_tk: tk.Tk):
        """
        The GUI initializer. We set up all the interface here.
        The interface is broken by columns and rows. Each element is
        placed in a specific cell.

        :param main_tk: The main tk element.
        """

        self.logger = logging.getLogger(__name__)
        self.callback = {}
        self.window = main_tk
        self.window.rowconfigure(14, minsize=50)
        self.window.columnconfigure(3, minsize=50)

        # ==================================
        # Student
        # ==================================
        self.group_label1 = tk.Label(text="Students", width=20, font=("Courier", 20))
        self.s_fn_label = tk.Label(
            text="First Name:",
            width=10,
        )
        self.s_ln_label = tk.Label(
            text="Last Name:",
            width=10,
        )
        self.s_dob_label = tk.Label(
            text="DOB:",
            width=10,
        )
        self.s_id_label = tk.Label(
            text="Student ID:",
            width=10,
        )

        self.group_label1.grid(row=0, column=0)
        self.s_fn_label.grid(row=1, column=0)
        self.s_ln_label.grid(row=2, column=0)
        self.s_dob_label.grid(row=3, column=0)
        self.s_id_label.grid(row=4, column=0)

        self.s_fn_entry = tk.Entry(width=10)
        self.s_ln_entry = tk.Entry(width=10)
        self.s_dob_entry = tk.Entry(width=10)
        self.s_id_entry = tk.Entry(width=10)

        self.s_fn_entry.grid(row=1, column=1)
        self.s_ln_entry.grid(row=2, column=1)
        self.s_dob_entry.grid(row=3, column=1)
        self.s_id_entry.grid(row=4, column=1)

        self.s_add_button = tk.Button(
            text="Add Student",
            width=10,
        )
        self.s_add_button.grid(row=5, column=0)

        # ==================================
        # Faculty
        # ==================================
        # TODO: This should be exactly as the the student setup, but for faculty.
        #  The names of the elements must be the same as in the unittests for the tests to pass.

        self.group_label2 = tk.Label(text="Faculty", width=20, font=("Courier", 20))
        self.f_fn_label = tk.Label(
            text="Fisrt name:",
            width=10,
        )
        self.f_ln_label = tk.Label(
            text="Last name:",
            width=10,
        )
        self.f_dob_label = tk.Label(
            text="DOB:",
            width=10,
        )
        self.f_office_label = tk.Label(
            text="Office:",
            width=10,
        )

        self.group_label2.grid(row=6, column=0)
        self.f_fn_label.grid(row=7, column=0)
        self.f_ln_label.grid(row=8, column=0)
        self.f_dob_label.grid(row=9, column=0)
        self.f_office_label.grid(row=10, column=0)

        self.f_fn_entry = tk.Entry(width=10)
        self.f_ln_entry = tk.Entry(width=10)
        self.f_dob_entry = tk.Entry(width=10)
        self.f_office_entry = tk.Entry(width=10)

        self.f_fn_entry.grid(row=7, column=1)
        self.f_ln_entry.grid(row=8, column=1)
        self.f_dob_entry.grid(row=9, column=1)
        self.f_office_entry.grid(row=10, column=1)

        self.f_add_button = tk.Button(
            text="Add Faculty",
            width=10,
        )
        self.f_add_button.grid(row=11, column=0)

        # ===========================
        # Remove a person
        # ===========================
        self.group_label3 = tk.Label(
            text="Remove Person", width=20, font=("Courier", 20)
        )
        self.remove_label = tk.Label(
            text="Person's Name:",
            width=10,
        )
        self.remove_entry = tk.Entry(width=10)
        self.remove_button = tk.Button(
            text="Remove Person",
            # command=self.click_remove_person,
            width=10,
        )

        self.group_label3.grid(row=12, column=0)
        self.remove_label.grid(row=13, column=0)
        self.remove_entry.grid(row=13, column=1)
        self.remove_button.grid(row=14, column=0)

        # ===========================
        # Person List
        # ===========================
        self.person_list = tk.Text()
        self.person_list.grid(row=0, column=2, rowspan=13)

        # ===========================
        # Error Label
        # ===========================
        self.error_label = tk.Label(text="", width=50, fg="red")
        self.error_label.grid(row=14, column=2)

    def add_callback(self, key: int, method: Callable):
        """
        We add a callback element. Each element is going to be linked
        to a specific button in the bind method.
        :param key: The key identifier (should be a digit)
        :param method: A method to call.
        """
        self.callback[key] = method

    def bind_command(self):
        """
        Bind each key to a specific button.
        """
        self.s_add_button.config(command=self.callback[1])
        self.f_add_button.config(command=self.callback[2])
        self.remove_button.config(command=self.callback[3])

    def add_student(self):
        """
        Get the student information from the GUI.
        :return: A student information as a string (e.g., "FirstName LastName 1999-10-10 999999999")
        """
        # TODO: implement this as we did for the faculty.
        fn = self.s_fn_entry.get()
        ls = self.s_ln_entry.get()
        dob = self.s_dob_entry.get()
        id = self.s_id_entry.get()
        inp = f"{fn} {ls} {dob} {id}"
        self.logger.debug(f"Adding Student: {inp}")
        return inp

    def add_faculty(self):
        """
        Get the faculty information from the GUI.
        :return: A faculty information as a string (e.g., "FirstName LastName 1999-10-10 20")
        """
        fn = self.f_fn_entry.get()
        ls = self.f_ln_entry.get()
        dob = self.f_dob_entry.get()
        office_no = self.f_office_entry.get()
        inp = f"{fn} {ls} {dob} {office_no}"
        self.logger.debug(f"Adding Faculty: {inp}")
        return inp

    def remove_person(self):
        """
        Get a person information to be deleted.
        :return: A person information as a string (e.g., "LastName")
        """
        # TODO: get the person information from the remove text box and pass it back.
        name = self.remove_entry.get()
        return name

    def list_people(self, persons: list):
        """
        Update the people's list based on the list passed.
        :param persons: A list of people's information.
        """
        info = ""
        for p in persons:
            info += f"{p}\n"

        self.person_list.delete("1.0", "end")
        self.person_list.insert("1.0", info)

        # TODO: Update the person_list element with the information in the passed list.
        #  Part of the code is given for you. You only need to update the element using the variable info.
        #  Hint, look into the test cases to see how the you can update the element

    def show_error(self, error: str):
        """
        Show the error passed in the gui. Please note how we update the label is different from the Text in the
        list_people above. Thus, you cannot use what you see here in the method above.
        :param error: Error message.
        """
        self.logger.error(error)
        self.error_label.config(text=error)
