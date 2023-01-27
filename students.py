class Student:
    def __init__(self, name, grad_year):
        self.name = name
        self.graduation = grad_year

    def info(self):
        print(f"{self.name.capitalize()} graduates in {self.graduation}")


def main():
    print("hello world")
    first_year = Student("Bob", 2027)
    first_year.info()


if __name__ == "__main__":
    main()