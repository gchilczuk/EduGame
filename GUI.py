import tkinter as tk
from tkinter import ttk


class GUI(tk.Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.items = dict()
        self.variables = dict()
        self.images = dict()
        self.last_used_row = 0
        self.last_used_column = 0
        self.max_column = 0
        self.max_row = 0

    def add_label(self, name, **kwargs):
        """
        Create single label
        :param name: string, name of label
        :param kwargs: row, column, rowspan, columnspan, text, image, etc
        :return: created label
        """
        self.is_name_free(name)
        self.images[name] = kwargs.get('image')  # only ImageTk.PhotoImage() → not implemented yet
        self.items[name] = tk.Label(self,
                                    **{k: v for k, v in kwargs.items() if k in {'text','bg','fg',
                                                                                 'wraplength','compound',
                                                                                 'justify'}},
                                    # image=self.images['name']
                                    )
        self.items[name].grid(**{k: v for k, v in kwargs.items() if k in {'column', 'columnspan',
                                                                           'row', 'rowspan',
                                                                           'padx', 'pady', 'ipadx', 'ipady',
                                                                           'sticky', 'in_'}})
        return self.items[name]

    def add_button(self, name, **kwargs):
        """
        :param name: string, name of button
        :param kwargs: row, column, rowspan, columnspan, text, image, etc
        :return: created button
        """
        self.is_name_free(name)
        self.images[name] = kwargs.get('image')  # only ImageTk.PhotoImage() → not implemented yet
        self.items[name] = tk.Button(self,
                                     **{k: v for k, v in kwargs.items() if k in {'bg', 'fg', 'text',
                                                                                 'compound', 'image',
                                                                                 'command'}}
                                     )
        self.items[name].grid(**{k: v for k, v in kwargs.items() if k in {'column', 'columnspan',
                                                                          'row', 'rowspan',
                                                                          'padx', 'pady', 'ipadx', 'ipady',
                                                                          'sticky', 'in_'}})
        return self.items[name]

    def add_checkbox(self, name, start_value=0, **kwargs):
        """
        Create single checkbox
        :param name: name of checkbox
        :param start_value: initial value of checkbox (0 or 1)
        :param kwargs: row, column, rowspan, columnspan, text etc
        :return: created checkbox
        """
        self.is_name_free(name)
        self.variables[name] = tk.IntVar(value=start_value)
        self.items[name] = tk.Checkbutton(self,
                                          **{k: v for k, v in kwargs.items() if k in {'bg', 'fg', 'text',
                                                                                      'compound', 'image',
                                                                                      'command'}},
                                          variable=self.variables[name]
                                          )
        self.items[name].grid(**{k: v for k, v in kwargs.items() if k in {'column', 'columnspan',
                                                                          'row', 'rowspan',
                                                                          'padx', 'pady', 'ipadx', 'ipady',
                                                                          'sticky', 'in_'}})
        return self.items[name]

    def add_radiobutton(self, name, **kwargs):
        """
        Create single radiobutton
        :param name: name of item
        :param kwargs: row, column, rowspan, columnspan, text, image, etc
        :return:
        """
        # self.is_name_free(name)
        if name not in self.variables:
            self.variables[name] = tk.IntVar()
        self.items[name] = tk.Radiobutton(self,
                                          **{k: v for k, v in kwargs.items() if k in {'bg', 'fg', 'text',
                                                                                      'compound', 'image',
                                                                                      'command'}},
                                          variable=self.variables[name]
                                          )
        self.items[name].grid(**{k: v for k, v in kwargs.items() if k in {'column', 'columnspan',
                                                                          'row', 'rowspan',
                                                                          'padx', 'pady', 'ipadx', 'ipady',
                                                                          'sticky', 'in_'}})
        return self.items[name]

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

    def rename_button(self, old_name, new_name):
        pass

    def kill_button(self, name):
        pass

    def is_name_free(self, name):
        if name in self.items.keys():
            raise NameAlreadyUsedException(
                "This name is already used in this Frame, you need to use another one.")


class InvalidPositionException(Exception):
    pass


class NameAlreadyUsedException(Exception):
    pass
