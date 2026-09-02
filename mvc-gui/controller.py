"""
The controller module. It connects the view with the model.

Author: Ziyad Alsaeed
Email: zalsaeed@qu.edu.sa
"""

import logging

import tkinter as tk

from gui import GUI
from persons import PersonList
from person import Student, Faculty

# set up logger
for handler in logging.root.handlers[:]:  # make sure all handlers are removed
    logging.root.removeHandler(handler)

logging_level = logging.DEBUG
logging_format = logging.Formatter(
    "%(asctime)s: %(levelname)s [%(name)s:%(funcName)s:%(lineno)d] - %(message)s"
)
logging.root.setLevel(logging_level)
h = logging.StreamHandler()
h.setFormatter(logging_format)
logging.root.addHandler(h)


class Controller:
    def __init__(self):
        """
        Initialize the controller and bind all the button from the view.
        """
        self._persons = PersonList()
        self.main_tk = tk.Tk()
        self._view = GUI(self.main_tk)

        # add the commands to the view callback dict
        self._view.add_callback(1, self.add_student)
        self._view.add_callback(2, self.add_faculty)
        self._view.add_callback(3, self.remove_person)
        self._view.bind_command()

        self.logger = logging.getLogger(__name__)

    def run(self):
        """
        Run the GUI interface.
        """
        self.main_tk.mainloop()

    def add_student(self):
        """
        Add a student to the persons list based on info from the view.
        """

        # TODO: Clear the error message in the view.
        self._view.error_label.config(text="")
        inp = self._view.add_student()
        data = inp.split(" ")
        p = Student(data[0], data[1], data[2], int(data[3]))
        try:
            self._persons.append(p)
        except Exception as e:
            # TODO: notify the view of the error if any error happens!
            self._view.error_label.config(text=f"Unable to parse input! {e}")

        self._view.list_people(self._persons.get_people())

    def add_faculty(self):
        self._view.error_label.config(text="")
        inp = self._view.add_faculty()
        data = inp.split(" ")
        p = Faculty(data[0], data[1], data[2], int(data[3]))
        try:
            self._persons.append(p)
        except Exception as e:
            self._view.error_label.config(text=f"Unable to parse input! {e}")

    def remove_person(self):
        pass
