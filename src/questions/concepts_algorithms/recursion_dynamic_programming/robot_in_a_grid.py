from src.helper.question import Question


class RobotInAGrid(Question):

    def solve(self):
        """
        Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
        The robot can only move in two directions, right and down, but certain cells are "off limits" such
        that the robot cannot step on them. Design an algorithm to find a path for the robot from
        the top left to the bottom right.
        :return: O[i + j] - time | O[i * j] - space
        """
        def recursion(m: list, p: list, fp: list, i: int, j: int):
            if i < 0 or j < 0 or not m[i][j]:
                return False
            cell: tuple = (i, j)
            if cell in fp:
                return False
            if (i == 0 and j == 0) or recursion(m, p, fp, i - 1, j) or recursion(m, p, fp, i, j - 1):
                p.append(cell)
                return True
            fp.append(cell)
            return False

        matrix: list = [
            [True, True, False],
            [False, True, False],
            [True, True, True]
        ]
        path: list = []
        failed_points: list = []
        found = recursion(matrix, path, failed_points, len(matrix) - 1, len(matrix[0]) - 1)
        self.result = path if found else None


if __name__ == '__main__':
    with RobotInAGrid(RobotInAGrid.__name__) as question_class:
        question_class.solve()
