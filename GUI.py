import tkinter as tk
from tkinter import ttk


class GUIFrame(tk.Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.items = dict()
        self.variables = dict()
        self.images = dict()
        self.grid()

    def add_label(self, name, **kwargs):
        """
        Create single label
        :param name: string, name of label
        :param kwargs: row, column, rowspan, columnspan, text, image, etc
        :return: created label
        """
        self.is_name_free(name)
        # self.images[name] = kwargs.get('image', None)  # only ImageTk.PhotoImage() → not implemented yet
        self.items[name] = tk.Label(self,
                                    **{k: v for k, v in kwargs.items() if k in {'text','bg','fg',
                                                                                'wraplength','compound',
                                                                                'justify', 'image'}},
                                    image=self.images['name']
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
        # self.images[name] = kwargs.get('image')  # only ImageTk.PhotoImage() → not implemented yet
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

    def add_radiobutton(self, name, val, **kwargs):
        """
        Create single radiobutton
        'name' is name of dictionary where similar radiobuttons are remembered,
        inside dictionary elements are numbered in orderd of creation.
        :param name: name of item
        :param val: value of radiobutton
        :param kwargs: row, column, rowspan, columnspan, text, image, etc
        :return: created radiobutton
        """
        # self.is_name_free(name)
        if name not in self.variables:
            self.variables[name] = tk.IntVar() if type(val) is int else tk.StringVar()
            self.variables[name].set(val)
            self.items[name] = dict()
        n_name = name+str(len(self.items[name]))
        self.items[name][n_name] = tk.Radiobutton(self,
                                                  **{k: v for k, v in kwargs.items() if k in {'bg', 'fg', 'text',
                                                                                              'compound', 'image',
                                                                                              'command'}},
                                                  variable=self.variables[name],
                                                  value=val
                                                  )
        self.items[name][n_name].grid(**{k: v for k, v in kwargs.items() if k in {'column', 'columnspan',
                                                                                  'row', 'rowspan',
                                                                                  'padx', 'pady', 'ipadx', 'ipady',
                                                                                  'sticky', 'in_'}})
        return self.items[name][n_name]

    def add_progressbar(self,name,**kwargs):
        """
        Create progressbar
        :param name: string, name of label
        :param kwargs: orient, row, column, rowspan, columnspan etc
        :return: created progressbar
        """
        self.is_name_free(name)
        self.variables[name] = tk.IntVar(value=kwargs.get('value',0))
        self.items[name] = ttk.Progressbar(self,
                                           **{k: v for k, v in kwargs.items() if k in {'orient', 'length',
                                                                                       'mode','maximum'}},
                                           variable=self.variables[name]
                                           )
        self.items[name].grid(**{k: v for k, v in kwargs.items() if k in {'column', 'columnspan',
                                                                          'row', 'rowspan',
                                                                          'padx', 'pady', 'ipadx', 'ipady',
                                                                          'sticky', 'in_'}})
        return self.items[name]

    def destroy_item(self, name):
        try:
            self.items[name].destroy()
            del self.items[name]
        except:
            print("Ups!")
            return False
        try:
            del self.variables[name]
        except:
            pass
        try:
            del self.images[name]
        except:
            pass
        return True

    def destroy_self(self):
        self.items.clear()
        self.variables.clear()
        self.images.clear()
        self.destroy()

    def configure_item(self, name, value=None, image=None, **kwargs):
        if value is not None:
            self.variables[name] = value
        if image is not None:
            self.images[name] = image
        if len(kwargs) > 0:
            self.items[name].configure(**kwargs)


    def mark_answers(self, answer, colour):
        pass

    def get_answers(self, dialog):
        pass

    def kill_selection_dialog(self, dialog):
        pass

    def rename_button(self, old_name, new_name):
        pass

    def get_var(self, name):
        return self.variables[name]

    def is_name_free(self, name):
        if name in self.items.keys():
            raise NameAlreadyUsedException(
                "This name is already used in this Frame, you need to use another one.")

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


class InvalidPositionException(Exception):
    pass


class NameAlreadyUsedException(Exception):
    pass
