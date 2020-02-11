from src.helper.question import Question


class TripleStep(Question):

    def solve(self):
        """
        A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
        Implement a method to count how many possible ways the child can run up the stairs.
        :return: O[n] - time | O[n] - space
        """
        def recursion(n: int, memory: list):
            if n < 0:
                return 0
            elif n == 0:
                return 1
            elif memory[n] > -1:
                return memory[n]
            else:
                memory[n] = recursion(n - 1, memory) + recursion(n - 2, memory) + recursion(n - 3, memory)
                return memory[n]

        number: int = 4
        memo: list = [-1] * (number + 1)
        self.result = recursion(number, memo)


if __name__ == '__main__':
    with TripleStep(TripleStep.__name__) as question_class:
        question_class.solve()
