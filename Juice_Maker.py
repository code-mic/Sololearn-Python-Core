class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return (self.name + ' ('+str(self.capacity)+'L)')

    def __add__(self, A):
        t_name = self.name + '&' + A.name
        t_capacity = self.capacity + A.capacity
        return '{0} ({1}L)'.format(t_name, t_capacity)

a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

result = a + b
print(result)
