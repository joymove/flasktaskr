import os


print __file__
a = os.path.abspath(__file__)
d = os.path.dirname(a)
print a
print d
print os.path.basename(__file__)
