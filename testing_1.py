class Person:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age


if __name__ == "__main__":
    p = Person("Kaysan", 3)
    print(p.name)
    print(p.age)
