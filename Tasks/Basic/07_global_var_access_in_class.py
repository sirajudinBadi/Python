x = 154
class A:
    def increment_x(self):
        global x
        x += 1
        return x

    def get_x(self):
        return x

a = A()
print(a.get_x())
print(a.increment_x())
print(a.increment_x())