# Car class
# Noah Lindon
# CSCI 290
# 1/30/20
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year
 

def main():
    #where you input the cars info
    make = input("Enter the make of your vehicle: ")
    model = input("Enter the model of your vehicle: ")
    year = input("Enter the year of your vehicle: ")
    myCar=Car(make,model,year)
    #displays car info
    print("The make of your car is ", myCar.get_make())
    print("The model of your car is ", myCar.get_model())
    print("The year of your car is ", myCar.get_year())

    #where you input the cars info
    make = input("Enter the make of your second vehicle: ")
    myCar.set_make(make)
    print("The make of your car is ", myCar.get_make())
    model = input("Enter the model of your second vehicle: ")
    myCar.set_model(model)
    #displays car info
    print("The model of your car is ", myCar.get_model())
    year = input("Enter the year of your second vehicle: ")
    myCar.set_year(year)
    print("The year of your car is ", myCar.get_year())
   
    


# Call the main function.
main()
