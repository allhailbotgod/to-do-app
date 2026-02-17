#  CODE BY BOTGODJAY

print("=== TO-DO LIST APP ===")

# Implementing user input validation
try:
  user_choice = int(input('''
  1. Create Task
  2. View glob_task
  3. Update Task
  4. Delete Task
  5. End Program

  ==> '''))
except ValueError:
  print("Wrong input. Program ended.")

glob_task = []

# We define a function to easily loop through the 'glob_task' list and print out each items in it
def print_task():
    print("==== YOUR TASKS ====\n")

    for task in range(len(glob_task)):
      bullet = task + 1
      print(f"{bullet}.", glob_task[task].strip().title())

    print("\n====================\n")

# Iterating over all items in the list (express purpose of checking for empty input)
def null_checker():
  for task in range(len(glob_task)):
    return glob_task[task].strip()

# (Creating Task) Logic
if user_choice == 1:
  try:    
    user_input_task = str(input("\nWrite out your task. You can specify more than one task separated by a comma (,)\n==> "))

  except ValueError:
    print("Invalid input. Program ended.")
  
  glob_task = user_input_task.split(',')

  glob_task.extend(glob_task)

  # Handling empty input from the user
  if len(null_checker()) == 0:
    print("\nYou did not enter a value!\n")

  else:
    print_task()

# (Viewing Task) Logic
elif user_choice == 2:
  
  for task in range(len(glob_task)):
    glob_task = glob_task[task].strip()
  
  if len(glob_task) == 0:
    print("\nNo task created yet.\n")

  else:
    print_task()