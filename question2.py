class Sazal:
    def __init__(self):
        self.b=1
try:
    object=Sazal()
    print(object.c)
except:
    print("Attribute Error raised")


try:
    x= float(input())
    a=input('Enter the value')
    z=x+a

except TypeError as e:
            print("yo add float with int",e)
except ValueError as e:
            print("You have given a value int")

