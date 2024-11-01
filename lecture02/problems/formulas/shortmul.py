class MyClass:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def short_mul(self) -> float:
        _result = self._a ** 2 + 2 * self._a * self._b + self._b ** 2
        return _result

