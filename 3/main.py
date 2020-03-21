class foo:
    def __init__(self, n):
        self.n = n

    def __call__(self, i):
        self.n += i
        return self.n


x = foo(1)
x(5)
foo(3)
print(x(2.3))
