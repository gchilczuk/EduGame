import tkinter as tk
from tkinter import ttk

class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.names = {}
        self.textvariables = dict()
        self.variables = dict()
        self.images = dict()
        self.labels = dict()
        self.checkboxes = dict()
        self.radiobuttons = dict()
        self.last_used_row = 0
        self.last_used_column = 0
        self.max_column = 0
        self.max_row = 0

    def add_label(self, name, **kwargs):
        """
        Create single label
        :param name: string, name of item
        :param kwargs: row, column, rowspan, columnspan, text, image, etc
        :return: created label
        """
        self.images[name] = kwargs.get('image')  # only ImageTk.PhotoImage() → not implemented yet
        self.textvariables[name] = tk.StringVar(value=kwargs.get('text', ''))
        self.labels[name] = tk.Label(self,
                                     textvariable=self.textvariables[name],
                                     **{k : v for k, v in kwargs.items() if k in {'bg', 'fg', 'wraplength',
                                                                                   'compound', 'justify'}},
                                     # image=self.images['name']
                                     )
        self.labels[name].grid(**{k : v for k, v in kwargs.items() if k in {'column', 'columnspan',
                                                                           'row', 'rowspan',
                                                                           'padx', 'pady', 'ipadx', 'ipady',
                                                                           'sticky', 'in_'}})
        return self.labels[name]


    def add_checkbox(self, name, **kwargs):
        """
        Create single checkbox
        :param name: name of item
        :param kwargs: row, column, rowspan, columnspan, text etc
        :return: created checkbox
        """
        self.checkboxes[name] = tk.Checkbutton(self, **kwargs)
        return self.checkboxes[name]

    def add_radiobutton(self, name,  **kwargs):
        """
        Create single radiobutton
        :param name: name of item
        :param var: string name of varieble
        :return:
        """
        if name not in self.variables: self.variables[name] = tk.IntVar()
        self.radiobuttons[name] = tk.Radiobutton(self, variable=self.variables[name], **kwargs)
        return self.radiobuttons[name]

    def add_single_selection_dialog(self, name, question, answers, left_up, right_down, orientation='h'):
        """
        Create Label with question and radiobuttons with answers
        :param name: string, name of dialog
        :param question: string, question itself
        :param answers: list of strings, variety of answers
        :param left_up:
        :param right_down:
        :param orientation: v for verticle, h for horizontal
        :return:
        """

        # ?
        a = len(answers) + 1
        h = right_down[1] - left_up[1]
        l = right_down[0] - left_up[0]
        rety = []
        if orientation == 'h':
            if a > h or l < 2:
                raise InvalidPositionException("More objects than reserved space")

            rety.append(self.add_radiobutton(name, text=question, row=left_up[0], column=0))

        elif orientation == 'v':
            if a > l or h < 1:
                raise InvalidPositionException("More objects than reserved space")



    def add_multiple_selection_dialog(self, name, question, answers, position=None, orientation='v'):
        pass

    def mark_answers(self, answer, colour):
        pass

    def get_answers(self, dialog):
        pass

    def kill_selection_dialog(self, dialog):
        pass

    def add_button(self, name, function, position=None):
        pass

    def rename_button(self, old_name, new_name):
        pass

    def kill_button(self, name):
        pass

    def is_name_free(self, name):
        if name in self.names: raise NameAlreadUsedException("This name is already used in this Frame, you need to use another one.")

class InvalidPositionException(Exception):
    pass

class NameAlreadUsedException(Exception):
    pass
