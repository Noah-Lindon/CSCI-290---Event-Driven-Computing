# Noah Lindon
# CSCI 290
# 2/4/20
# Employee class
class Employee:
    def __init__(self):
        self.__name = " "
        self.__idNum = " "
        self.__title = " "
        self.__salary = 0
        self.__department = " "
#sets information for employeee
    def set_name(self, name):
        self.__name = name

    def set_idNum(self, idNum):
        self.__idNum = idNum

    def set_title(self, title):
        self.__title = title

    def set_salary(self, salary):
        self.__salary = salary
        
    def set_department(self, department):
        self.__department = department

#gets information for employee
    def get_name(self):
        return self.__name
    def get_idNum(self):
        return self.__idNum
    def get_title(self):
        return self.__title
    def get_salary(self):
        return self.__salary
    def get_department(self):
        return self.__department
#main function
def main():
    
    # Create a Employee object.
    myEmployee = Employee()
#calls the myEmployee and their sets and adds information
    myEmployee.set_name("Noah Lindon")
    myEmployee.set_idNum("12345")
    myEmployee.set_title("humble beggar")
    myEmployee.set_salary("poor")
    myEmployee.set_department("computer science")
    
    
    
    # Display the name.
    print('Your name is:', myEmployee.get_name())
    
    # Display the idNum.
    print('Your idNum is:', myEmployee.get_idNum())
    
    # Display the title.
    print('Your title is:', myEmployee.get_title())
    
    # Display the salary.
    print('Your salary is:', myEmployee.get_salary())
    
    # Display the department.
    print('Your department is:', myEmployee.get_department())
    

# Call the main function.
main()
