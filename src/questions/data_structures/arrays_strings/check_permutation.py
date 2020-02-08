from src.helper.question import Question


class CheckPermutation(Question):

    def solve(self):
        """
        Given two strings, write a method to decide if one is a permutation of the other.
        :return: O[n*log(n)] * 2 = O[n*log(n)] - time | O[n] - space
        """
        string_1: str = 'ABCD'
        string_2: str = 'ACDB'
        if len(string_1) == len(string_2):
            string_1: str = ''.join(sorted(string_1))  # O[n*log(n)]
            string_2: str = ''.join(sorted(string_2))  # O[n*log(n)]
            self.result = bool(string_1 == string_2)
        else:
            self.result = False


if __name__ == '__main__':
    with CheckPermutation(CheckPermutation.__name__) as question_class:
        question_class.solve()
