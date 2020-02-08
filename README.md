# Cracking the Coding Interview

[![HitCount](http://hits.dwyl.io/AlbertSuarez/cracking-the-coding-interview.svg)](http://hits.dwyl.io/AlbertSuarez/cracking-the-coding-interview)
![Python application](https://github.com/AlbertSuarez/cracking-the-coding-interview/workflows/Python%20application/badge.svg)
[![GitHub stars](https://img.shields.io/github/stars/AlbertSuarez/cracking-the-coding-interview.svg)](https://GitHub.com/AlbertSuarez/cracking-the-coding-interview/stargazers/)
[![GitHub forks](https://img.shields.io/github/forks/AlbertSuarez/cracking-the-coding-interview.svg)](https://GitHub.com/AlbertSuarez/cracking-the-coding-interview/network/)
[![GitHub contributors](https://img.shields.io/github/contributors/AlbertSuarez/cracking-the-coding-interview.svg)](https://GitHub.com/AlbertSuarez/cracking-the-coding-interview/graphs/contributors/)
[![GitHub license](https://img.shields.io/github/license/AlbertSuarez/cracking-the-coding-interview.svg)](https://github.com/AlbertSuarez/cracking-the-coding-interview/blob/master/LICENSE)

📗 Code answers of the 6th edition of [Cracking the Coding Interview](http://www.crackingthecodinginterview.com/): 189 Programming Questions &amp; Solutions.

[Repository hosted through GitHub pages](https://asuarez.dev/cracking-the-coding-interview)

## Requirements

1. Python 3.7+

## Recommendations

Usage of [virtualenv](https://realpython.com/blog/python/python-virtual-environments-a-primer/) is recommended for package library / runtime isolation.

## Usage

Run the code for any of the questions under the `src.questions` Python module from the root directory.

```bash
python3 -m src.questions.X.Y.Z
```

being:
- `X`: Interview question category.
- `Y`: Chapter name.
- `Z`: Question name.

Or run all the available questions all together.

```bash
python3 -m src
```

## Implement new questions

Every question has to be a class based on the abstract class called `Question` (found at `src.helper.question`).

The code for every question has to start like this:

```python
from src.helper.question import Question


class QuestionClass(Question):

    def solve(self):
        # To implement
        pass


if __name__ == '__main__':
    with QuestionClass(QuestionClass.__name__) as question_class:
        question_class.solve()

```

## Authors

- [Albert Suàrez](https://github.com/AlbertSuarez)

## License

MIT © Cracking the Coding Interview
