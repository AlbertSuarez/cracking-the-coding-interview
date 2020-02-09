from src.helper.question import Question


class Insertion(Question):

    def solve(self):
        """
        You are given two 32-bit number, N and M, and two bit positions, i and j.
        Write a method to insert M into N that M starts at bit j and ends at bit i.
        You can assume that the bits j through i have enough space to fit all M.
        :return: O[n] - time | O[n] - space
        """
        m = 0b10011
        n = 0b10000000000
        i = 2
        j = 6

        if i > j or i < 0 or j >= 32:  # Checking input.
            self.result = 0
            return
        all_ones = ~0  # All ones.
        left_part = all_ones << (j + 1) if j < 31 else 0  # Adding as much zeros as j.
        right_part = ((1 << i) - 1)  # Adding as much ones as i.
        masquerade_number = left_part | right_part  # Merging both parts leaving zeros between j and i.
        n_cleared = n & masquerade_number  # Clearing N.
        m_shifted = m << i  # Shifting M for adapting it to N.
        self.result = bin(n_cleared | m_shifted)  # Adding M into N.


if __name__ == '__main__':
    with Insertion(Insertion.__name__) as question_class:
        question_class.solve()
