import InputHandling
import Contact

# TODO: how to implement primary keys
# TODO: how to implement foreign keys


def main():
    #  initalizing vars
    example_entry_1 = ('Makoto', 'Ward', 'male')
    example_entry_2 = ('John', 'Doe', 'other')
    # InputHandling.input_handler()
    ct = contact_table = Contact.Contact()
    # address_table = Address.Address()
    # phone_table = Phone.Phone()

    # ct.store_contact_in_table(ct.create_contact_dict(example_entry_1))
    # ct.store_contact_in_table(ct.create_contact_dict(example_entry_2))

    # input loop
    input_handling_active = True
    while input_handling_active:

        print_menu()
        menu_option = int(input())

        if menu_option == 1:
            ct.add_contact()
        if menu_option == 2:
            f'd'
            # TODO: do i fully understand the keys aspect?



        if menu_option == 5:  # exit condition

            input_handling_active = False
            f'option 5 selected'

        ct.print_contacts()  # prints for debugging purposes


def print_menu():
    print("Please select an option from the menu:\n"
          "1 - Create Contact\n"
          "2 - Edit Contact\n"
          "3 - Search Contact\n"
          "4 - Delete Contact\n"
          "5 - Exit\n")

def createPrimaryKey():
    '''Returns primary key and checks for duplicates'''
    #  might not need, can probably use len(ct.contacts_list) - 1

if __name__ == "__main__":
    main()


# for key, pair in {'one':1, 'two':2}:
#     print(key)
