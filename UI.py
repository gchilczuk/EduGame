from tkinter import Tk
from stage_creator import GUIFrame
from game import Game


class EduGame:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("600x200+100+100")
        self.frame = None
        self.game = Game()

    def loop(self):
        self.root.mainloop()

    def destroy_frame(self):
        self.frame.destroy_self()
        self.frame = None

    def create_menu(self):
        """
        Creates first stage - menu
        :return: None
        """
        self.frame = GUIFrame(self.root)
        self.create_hello_menu()
        self.create_param1_menu()
        self.create_param2_menu()
        self.create_start_but_menu()

    def creat_level(self):
        self.frame = GUIFrame(self.root)
        lr = self.create_question(self.game.get_question_text(),
                             self.game.get_qestion_variants(),
                             self.game.get_question_image())
        self.create_check_but_level(lr+1)
        self.create_save_but_level(lr+1)


    def _start(self):
        pass

    def create_save_but_level(self, row):
        # self.frame.add_button()
        pass

    def create_check_but_level(self, row):
        # self.frame.add_button()
        pass

    def create_question(self, question, answers, img):
        """
        col: 0-3(4)
        row: 0~
        :param question: string of question
        :param answers: list of answers
        :param img: image optionally enclosed to question
        :return: row of last element
        """
        self.frame.add_label('question', text=question,
                             column=0, columnspan=4, row=0, sticky='W')
        if img is not None:
            self.frame.add_label(image=img, column=4, row=0, rowspan=6)

        last_row = 0
        for i in range(len(answers)):
            self.frame.add_checkbox(text=answers[i], column=1, columnspan=3, row=(1+i))
            last_row += 1

        return last_row



    def create_hello_menu(self):
        """
        col:0-11
        row:0
        Adds "Hello label" at the top of menu
        :return: None
        """
        hello = """Witaj w programie EduGra.
Wybierz liczbę powtórzeń pytania, oraz karę za błędną odpowiedź, 
a następnie kliknij przycisk "START". """
        self.frame.add_label('hello', text=hello, column=0, columnspan=12, 
                             row=0, sticky="W")
        self.frame.add_label('blank', text="  ", column=0, columnspan=4, 
                             row=2, sticky="W")

    def create_param1_menu(self):
        """
        col:[0,3]
        row:[3,4]
        Create dialog (using radiobuttons) with user
        Ask about first game parameter
        :return: None
        """
        self.frame.add_label('param1', text="Ile powtórzeń każdego pytania?", 
                             column=0, columnspan=4, row=3, sticky='W')
        self.frame.add_radiobutton('param1_rb', 1, column=0, row=4, text='1')
        self.frame.add_radiobutton('param1_rb', 2, column=1, row=4, text='2')
        self.frame.add_radiobutton('param1_rb', 3, column=2, row=4, text='3')
        self.frame.add_radiobutton('param1_rb', 4, column=3, row=4, text='4')

    def create_param2_menu(self):
        """
        col:[0,3]
        row:[5,6]
        Create dialog (using radiobuttons) with user
        Ask about second game parameter
        :return: None
        """
        self.frame.add_label('param2', 
                             text="Ile karnych powtórzeń za błędną odpowiedź?",
                             column=0, columnspan=4, row=5, sticky='W')
        self.frame.add_radiobutton('param2_rb', 0, column=0, row=6, text='0')
        self.frame.add_radiobutton('param2_rb', 1, column=1, row=6, text='1')
        self.frame.add_radiobutton('param2_rb', 2, column=2, row=6, text='2')
        self.frame.add_radiobutton('param2_rb', 3, column=3, row=6, text='3')

    def create_start_but_menu(self):
        """
        col:[1,2]
        row:[7,7]
        Create START button
        :return: None
        """
        self.frame.add_button('start', text="START", column=1, columnspan=2,
                              row=7, command=self._start, pady=10)

    # def get_answers(self, dialog):
    #     pass
    #
    # def mark_answers(self, answer, colour):
    #     pass
