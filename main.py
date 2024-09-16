def main():
    print("hello world")

    #declare vaiables
    age = 17
    teacher = "navab"
    is_teacher = True
    my_grade = 99.99
    
    print("age is: ", type(age), "teacher is a ", type(teacher), "is_teacher ", type(is_teacher), "my grade is a ", type(my_grade))

    #string formating with f-string
    print(f"The type of the variable is: {type(age)}")

    x = 42
    y = 3/4
    z = int('7')
    a = float(5)
    name = "Nina"
    print(type(x), type(y), type(z), type(a), type(name))
    print("my age in 10 years: ", (age + 10))
    
    #initialize args for function 
    ingredients_list = ["chocolate chips", "Uranium 231", "arsonic", "asbesdos"]
    snickerdoodle = "idk"
    tempature = 300
    
    #call a function
    #bake_cookie(ingredients_list, snickerdoodle, tempature)
    #bake_cookie(ingredients_list, snickerdoodle, tempature, cutter = "star")

    print("we doing math now")
    print(calculate_numbers(2, 3))
    print(calculate_numbers(2, 3, "multiply"))
    print(calculate_numbers(2, 3, operation="subtract"))

    #demonstate modifying values while iterating 
    #note that you can mix data types in the same list
    numbers = [5, 6, 929, 85, 99, 2, "hi"]
    list_iteration(numbers)

    #test different container types 
    listDemo()
    tupleDemo()
    setDemo()
    dictDemo()

def listDemo():
    print("List demo***")
    myList = ["f","u","c","k","","y","o","u","","a","b","b","y"]
    myList.append("!")
    print(myList)
    print("this is how many items are in the list", len(myList))

    #using index to access specfic item 
    print(myList[0])
    print(myList[12:14]) #item at index 12 is inclusive, 14 is exlcusive
    print(myList[4:])
    print(myList[-2:]) #negative index is the same as len(list) minus whatever is inside of the []

    #remove the f 
    myList.remove("f") #removes the first of this char
    myList.append(1, "ph")
    print(myList)

def tupleDemo():
    print("Tuple Demo***")

def setDemo():
    print("demo of set ***")

def dictDemo():
    print("this is a dictionary demo***")
    

def bake_cookie(ingredients, tempature, instructions, cutter="circle"):
    #print the list of ingredients 
    for item in ingredients:
        print(item)
    #print the oven temp 
    print(f"set oven temp to {tempature}")
    print(f"shape is a {cutter}")
    #print instructions
    print(instructions, end="\n")

def calculate_numbers(x, y, operation="add"):
    if operation == "add":
        return x + y
    elif operation == "subtract":
        return x - y 
    elif operation == "multiply":
        return x * y
    elif operation == "divide": 
        return x / y
    
def list_iteration(inputList):
    #dif ways to modify values while idderating 
    #1. create a new list as you loope 
    print("this is the first method")
    new_List = []
    for item in inputList: 
            new_List.append(item*2)
    print(new_List)

    #2. list comprehension
    print("this is the second method")

    inputList = [item * 2 for item in inputList]
    print(inputList) 


if __name__ == "__main__":
    main()
