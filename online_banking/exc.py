class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B → " + super().method()

class C(A):
    def method(self):
        return "C → " + super().method()

class D(C,B):
    pass

print(D().method())