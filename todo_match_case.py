todos = []

while True:
    user_action = input("Type 'add', 'show', 'edit', or 'exit': ")
    user_action = user_action.strip()
    user_action = user_action.lower()
    
    if user_action == 'add':
        todo = input("Enter a todo: ")
        todos.append(todo)
    
    elif user_action == 'show':
        for index, item in enumerate(todos):
            row = f"{index + 1}: {item}"
            print(row)
    
    elif user_action == 'edit':
        try:
            number = int(input("Number of the todo to edit: "))
            if number < 1 or number > len(todos):
                print("Invalid todo number. Please enter a valid number.")
                continue
            new_todo = input("Enter new todo: ")
            todos[number - 1] = new_todo
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    elif user_action == 'exit':
        break
    
    else:
        print("Invalid action. Please choose from 'add', 'show', 'edit', or 'exit'.")
