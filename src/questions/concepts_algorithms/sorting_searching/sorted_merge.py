from src.helper.question import Question


class SortedMerge(Question):

    def solve(self):
        """
        You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B.
        Write a method to merge B into a in sorted order.
        :return: O[n*log(m)] - time | O[n + m] - space
        """
        def binary_search(array: list, left: int, right: int, value: int):
            if left == right:
                return left
            m: int = int((left + right) / 2)
            if array[m] > value:
                return binary_search(array, left, m, value)
            else:
                return binary_search(array, m + 1, right, value)

        array_a: list = [1, 2, 4, 9, 10, 15, 23, 90]
        array_b: list = [2, 8, 22, 45, 48]
        for element_b in array_b:
            idx = binary_search(array_a, 0, len(array_a), element_b)
            array_a = array_a[:idx] + [element_b] + array_a[idx:]
        self.result = array_a


if __name__ == '__main__':
    with SortedMerge(SortedMerge.__name__) as question_class:
        question_class.solve()
