__author__ = "William Goble"
__email__ = "will.goble@gmail.com"
__version__ = "0.1.0"


class Student:
    def __init__(self, name, grad_year):
        self.name = name
        self.graduation = grad_year
        self.classes = list()

    def info(self):
        print(f"{self.name.capitalize()} graduates in {self.graduation}")

    def addClass(self, course):
        self.classes.append(course)


def main():
    print("hello world")
    first_year = Student("Bob", 2027)
    first_year.info()


if __name__ == "__main__":
    main()
