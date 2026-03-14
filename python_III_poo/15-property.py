class Person:
  def __init__(self, name, age):
    self._name = name
    self._age = age

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, value):
    if not isinstance(value, str):
      raise TypeError("Name must be a string")
    self._name = value

pessoa = Person("Alice", 30)
print(pessoa.name)  # Output: Alice
pessoa.name = "Bob"
print(pessoa.name)  # Output: Bob
