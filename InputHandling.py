import DataBaseMethods

def input_handler():
    input_handling_active = True
    while input_handling_active:

        print_menu()

        menu_option = input()

        if menu_option == 5:  # exit condition

            input_handling_active = False
            f'option 5 selected'

def print_menu():
    print("Please select an option from the menu:\n"
          "1 - Create Contact\n"
          "2 - Edit Contact\n"
          "3 - Search Contact\n"
          "4 - Delete Contact\n"
          "5 - Exit\n")
