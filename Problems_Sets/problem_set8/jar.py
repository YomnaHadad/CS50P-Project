class Jar:
            
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self.n_cookie = 0

    def __str__(self):
        return "🍪" * self.n_cookie

    def deposit(self, n):
        if self.n_cookie + n > self.capacity:
            raise ValueError
        self.n_cookie += n

    def withdraw(self, n):
        if n <= 0 or n > self.n_cookie:
            raise ValueError
        self.n_cookie -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.n_cookie
