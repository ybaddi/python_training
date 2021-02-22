# file app_new.py 

import app

print(app.a)
app.hello()

print(app.__name__)
print(__name__)


# lambda function

def multiple(x,y): return x*y

r = lambda x,y: x*y

print(r(12,3))

print( (lambda x,y: x*y) (12,3) )
