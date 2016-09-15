# v2
from quest import Question
from random import choice
from copy import deepcopy

class Game:

    def __init__(self, UI):
        """
        :param UI: User Interface from GUI module
        """
        self.curent_question = None
        self.base = None    # questions database
        self.to_ask = None  # questions to ask (deepcopy of 'base')
        self.passed = None  # used questions
        self.user_answers = []
        self.start = False
        self.UI = UI

    def boot(self, repeat=1, penalty=1, base=None):
        """
        Boot the game
        :param repeat: integer, how much times question must be repeated
        :param penalty: integer, how much repeat have to be incremented after incorrect answer
        :param base: database of questions
        :return: None
        """
        if self.base is None or len(self.base) == 0:
            if base is None or len(base) == 0:
                raise DatabaseNotFoundException("Database is unavailable")
            else:
                self.base = base

        self.to_ask = deepcopy(self.base)
        self.passed = []

        for quest in self.to_ask:
            quest.set_repeats(repeat, penalty)

        self.UI.boot()

        self.next_question()
        self.start = True

    def next_question(self):
        """
        Switch to next question
        :return:
        """
        self.user_answers = []
        self.curent_question = choice(self.to_ask)

    def set_base(self, base):
        """
        Set base of questions
        :param base: database of questions
        :return: None
        """
        self.base = base

    def set_user_answers(self, *args):
        for a in args:
            self.user_answers.append(a)

    def check_answer(self):
        pass



class DatabaseNotFoundException(Exception):
    pass

class InvalidStepException(Exception):
    pass