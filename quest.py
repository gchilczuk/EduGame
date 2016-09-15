

class Question:

    def __init__(self, question, variants, answers, repeat=1, penalty=1):
        """
        :param question: string, question
        :param variants: list of strings, all variants of answers
        :param answers: list of strings, correct answers in full length
        :param repeat: integer, how much times question must be repeated
        :param penalty: integer, how much times more question have to be repeated after incorrect answer
        """
        for an in answers:
            if an not in variants:
                raise InputDataConflictException("Answers are unavailable")

        self.question = question
        self.variants = variants
        self.answers = answers
        self.repeats_left = repeat
        self.penalty = penalty

    def check_answer(self, user_answers):
        """
        Checks if answers are correct
        :param user_answers: list of strings, answers given by user
        :return: dict, answer-:-is_it_correct_bool
        """
        for an in user_answers:
            if an not in self.variants:
                raise InputDataConflictException("Answers are invalid and can't be checked")

        ret = {}
        for an in user_answers:
            ret[an] = an in self.answers

        self._count_down_repeats_left(ret)

        return ret

    def is_passed(self):
        """
        Checks if question is passed
        :return: True if question is passed; else: False
        """
        return self.repeats_left == 0

    def set_repeats(self, repeat, penalty):
        self.repeats_left = repeat
        self.penalty = penalty

    def _count_down_repeats_left(self, ret_of_check_dict):
        is_good = True
        for an in self.answers:
            if an not in ret_of_check_dict:
                is_good = False

        if False in ret_of_check_dict.values():
            is_good = False

        self.repeats_left -= 1
        if not is_good:
            self.repeats_left += self.penalty

class InputDataConflictException(Exception):
    pass
