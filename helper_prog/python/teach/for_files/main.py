def create_py_file(index , context):
    with open(f"task_{index}.py" , "w") as file:
        file.write(context)

for i in range(25):
    create_py_file(i+1 , f"print(hello world {i})")