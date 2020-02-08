from src.helper.question import Question


class IsUnique(Question):

    def solve(self):
        """
        Implement an algorithm to determine if a string has all unique characters.
        What if you cannot user additional data structures?
        :return: O[n*log(n)] + O[n] = O[n] - time | O[n] - space
        """
        string_input: str = 'language'
        string_input: str = ''.join(sorted(string_input))  # O[n*log(n)]
        for idx in range(len(string_input)):  # O[n]
            if idx != len(string_input) - 1:
                if string_input[idx] == string_input[idx + 1]:
                    self.result = False
                    return
        self.result = True


if __name__ == '__main__':
    with IsUnique(IsUnique.__name__) as question_class:
        question_class.solve()
