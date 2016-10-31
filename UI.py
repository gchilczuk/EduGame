from stage_creator import GUIFrame
class Menu:
    def __init__(self, root, start_command):
        self.frame = GUIFrame(root)
        self.hello()
        self.ask1()
        self.ask2()
        self.start_but(start_command)

    def hello(self):
        hello = """Witaj w programie EduGra.
Wybierz liczbę powtórzeń pytania, oraz karę za błędną odpowiedź i kliknij przycisk "START". """
        self.frame.add_label('hello',text=hello,column=0, columnspan=12, row=0, sticky="W")
        self.frame.add_label('blank', text="  ", column=0, columnspan=4, row=2, sticky="W")

    def ask1(self):
        self.frame.add_label('ask1', text="Ile powtórzeń każdego pytania?", column=0, columnspan=4, row=3, sticky='W')
        self.frame.add_radiobutton('ask1_rb',1, column=0, row=4, text='1')
        self.frame.add_radiobutton('ask1_rb',2, column=1, row=4, text='2')
        self.frame.add_radiobutton('ask1_rb',3, column=2, row=4, text='3')
        self.frame.add_radiobutton('ask1_rb',4, column=3, row=4, text='4')

    def ask2(self):
        self.frame.add_label('ask2', text="Ile karnych powtórzeń za błędną odpowiedź?", column=0, columnspan=4, row=5, sticky='W')
        self.frame.add_radiobutton('ask2_rb', 0, column=0, row=6, text='0')
        self.frame.add_radiobutton('ask2_rb', 1, column=1, row=6, text='1')
        self.frame.add_radiobutton('ask2_rb', 2, column=2, row=6, text='2')
        self.frame.add_radiobutton('ask2_rb', 3, column=3, row=6, text='3')

    def start_but(self, start_command):
        self.frame.add_button('start', command=start_command, column=1, columnspan=2, row=7, text="START", pady=10)


class Level:

    def __init__(self):
        pass

    def get_answers(self, dialog):
        pass

    def mark_answers(self, answer, colour):
        pass
