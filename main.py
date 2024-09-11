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

def bake_cookie(ingredients, tempature, instructions, tools):
    #print the list of ingredients 

    #print the oven temp 

    #print instructions
    print(instructions)
    


if __name__ == "__main__":
    main()
