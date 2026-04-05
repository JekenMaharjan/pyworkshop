# ===============================================================
# To-Do List App
# ===============================================================

to_do_list = []

while True:
    
    to_do = input("Enter your To-Do (q to quit): ")
    
    if (to_do == 'q'):
        break

    to_do_list.append(to_do)
    
    # print(to_do_list)
    
    for i, task in enumerate(to_do_list, 1):
        print(f"{i}. {task}")