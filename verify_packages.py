import example_pkg
from example_pkg import a
from example_pkg import b

print(example_pkg.__path__)
print(a.name)
print(a.__path__)
print(b.name)
print(b.__path__)
