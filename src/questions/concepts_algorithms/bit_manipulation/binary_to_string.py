from src.helper.question import Question


class BinaryToString(Question):

    def solve(self):
        """
        Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double, print the binary representation.
        If the number cannot be represented accurately in binary with at most 32 characters, print "ERROR".
        :return: O[n] - time | O[n] - space
        """
        number: float = 0.72

        if number <= 0 or number >= 1:
            self.result = 'ERROR'
            return
        array_representation: list = ['.']
        while number > 0:
            number *= 2
            if number >= 1:
                array_representation.append('1')
                number -= 1
            else:
                array_representation.append('0')
        self.result = ''.join(array_representation)


if __name__ == '__main__':
    with BinaryToString(BinaryToString.__name__) as question_class:
        question_class.solve()
