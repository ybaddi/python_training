# file app.y 

a = 1970
def hello():
    print("Iam from app.y")

print(__name__)
if __name__ == "__main__":
    print("excuting as a main program")
    print("Value of __name__ is ", __name__)
    hello()