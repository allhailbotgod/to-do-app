#  CODE BY BOTGODJAY

import os

print("=== TO-DO LIST APP ===")

# Implementing user input validation
try:
  user_choice = int(input('''
  1. Create Task
  2. View Task
  3. Add Task
  4. Delete Task

======================

==> '''))
except ValueError:
  print("Invalid input. Program end.")

# (Create Task)

if user_choice == 1:
  try:
    print("\nWARNING!: Creating new task will overwrite previous ones if it already exits. Use 'Add Task' instead.\nThis operation cannot be reversed!")
    intent_create = str(input("Do you want to continue?\n\nYES (y) or NO (n)\n\n==> ")).lower()

    if intent_create == "yes" or intent_create == "y":
      task_intake = str(input("\nWrite out your task. You can specify more than one task separated by a comma (,)\n==> ")).strip()

      if task_intake == "":
        print("Your input is EMPTY!")
      
      else:
        with open("file.txt", "w") as file:
          file.write(task_intake)
        
        with open("file.txt", "r") as file:
          data = file.read()
        saved_data = data.split(",")

        print("\nTasks created successfully!\n\n===== YOUR TASKS =====\n")
        for task in range(len(saved_data)):
          bullet = task + 1
          print(f"{bullet}.", saved_data[task].strip().capitalize())
        print("\n======================\n")

    elif intent_create == "no" or intent_create == "n":
      print("\nOperation cancelled!")
    
    else:
      print("\nInvalid input. Program end")
    
  except ValueError:
    print("Invalid input!\nProgram end")

# (View Tasks)

elif user_choice == 2:
  if not os.path.exists("file.txt"):
    print("\nFile does not exist...\n\nNo Tasks to view...\nCreate a New Tasks first...\n\nProgram end\n")
  
  else:
    with open("file.txt", "r") as file:
      data = file.read()
    
    if data.strip() == "":
      print("\nTasks opened successfully!\n\n===== YOUR TASKS =====\n")
      print("No task have been created yet!\n\n======================\n")

    else:
      with open("file.txt", "r") as file:
        data = file.read()
      saved_data = data.split(",")

      print("\nTasks opened successfully!\n\n===== YOUR TASKS =====\n")
      for task in range(len(saved_data)):
        bullet = task + 1
        print(f"{bullet}.", saved_data[task].strip().capitalize())
      print("\n======================\n")

# (Add Task)

elif user_choice == 3:
  if not os.path.exists("file.txt"):
    print("\nFile does not exist...\n\nCreate a new Task first...\n\nProgram end\n")

  else:
    with open("file.txt", "r") as file:
      data = file.read()
    saved_data = data.split(",")

    try:
      new_intake = str(input("\nWrite out your task. You can specify more than one task separated by a comma (,)\n==> ")).strip()

      if new_intake == "":
          print("Your input is EMPTY!")
        
      else:
        with open("file.txt", "a") as file:
          file.write(f"{new_intake},".strip(","))
        
        with open("file.txt", "r") as file:
          data = file.read()
        saved_data = data.split(",")

        print("\nTasks added successfully!\n\n===== YOUR TASKS =====\n")
        for task in range(len(saved_data)):
          bullet = task + 1
          print(f"{bullet}.", saved_data[task].strip().capitalize())
        print("\n======================\n")
    
    except ValueError:
      print("Invalid input!\nProgram end")

# (Delete Task)

elif user_choice == 4:
  if not os.path.exists("file.txt"):
    print("\nFile does not exist!\nProgram end\n")

  else:
    print('''
\n===== PICK AN OPTION =====

1. Delete All Tasks
2. Delete Task by Index
          
==========================
  ''')

    delete_option = int(input("==> "))

    if delete_option == 1:
      validate_option = str(input("\nWARNING!: This operation cannot be reversed!\nDo you want to continue?\nYES (y) or NO (n)\n\n==> ")).lower()

      if validate_option == "yes" or validate_option == "y":
        print("\nDeleting 'file.txt'...")
        os.remove("file.txt")
        print("Operation completed successfully!\n")

      elif validate_option == "no" or validate_option == "n":
        print("Operation cancelled!\n")

      else:
        print("Invalid input\nTasks not deleted!\n\nProgram end\n")

    elif delete_option == 2:
      with open("file.txt", "r") as file:
        data = file.read()
      saved_data = data.split(",")

      print("\n=| ID | == | TASK |=======\n")
     
      for task in range(len(saved_data)):
        bullet = task + 1
        print(f"{bullet}.", saved_data[task].strip().capitalize())
      print("\n===========================\n")
      
      get_index = int(input("Enter the #id of the task you wish to delete\n\n==> "))

      validate_option = str(input("\nWARNING!: This operation cannot be reversed!\nDo you want to continue?\nYES (y) or NO (n)\n\n==> ")).lower()

      if validate_option == "yes" or validate_option == "y":
        print("\nLocating task...\nTask located...\nDeleting...")
        with open("file.txt", "r+") as file:
          data = file.read()
        saved_data = data.split(",")

        index = get_index - 1
        saved_data.pop(index).strip()

        stringify_saved_data = ",".join(saved_data)

        with open("file.txt", "w") as file:
          file.write(stringify_saved_data)
        print(f"\nTASK:'{saved_data.pop(index).strip().capitalize()}' has been deleted successfully\nUpdating tasks...")

        with open("file.txt", "r") as file:
          data = file.read()
        saved_data = data.split(",")

        print("\n===== YOUR TASKS =====\n")
        for task in range(len(saved_data)):
          bullet = task + 1
          print(f"{bullet}.", saved_data[task].strip().capitalize())
        print("\n======================\n")

      elif validate_option == "no" or validate_option == "n":
        print("Operation cancelled!")

      else:
        print("Invalid input\nTask not deleted!\n\nProgram end")
    
    else:
      print("Invalid input!\nProgram end")
      