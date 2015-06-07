# Implement a iterator that iterates a list fromn the reverse direction
class reverse_iter(object):
    def __init__(self, l):
        self.l = l
        self.m = 0
        self.n = -len(l)
    
    def __iter__(self):
        return self

    def next(self):
        if self.m > self.n:
            self.m = self.m-1
            return self.l[self.m]
        else:
            raise StopIteration() 


l = [1, 2, 3, 'hello']
r = reverse_iter(l)
for i in r:
    print i
