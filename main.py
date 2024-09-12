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
    bake_cookie(ingredients_list, snickerdoodle, tempature)
    bake_cookie(ingredients_list, snickerdoodle, tempature, cutter = "star")
    

def bake_cookie(ingredients, tempature, instructions, cutter="circle"):
    #print the list of ingredients 
    for item in ingredients:
        print(item)
    #print the oven temp 
    print(f"set oven temp to {tempature}")
    print(f"shape is a {cutter}")
    #print instructions
    print(instructions, end="\n")


    
    


if __name__ == "__main__":
    main()
