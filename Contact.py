import csv

class Contact:
    """class to represent Contact table in simulated database"""
    def __init__(self):
        self.current_index = 0
        self.size_of_table = 0
        self.contacts_list = []  # list of dictionaries -- to delete, set given index to nullish values
        # self.holes_in_table_counter = 0  # for counting num of times rows/indexes removed
        # self.hole_in_indexes_list = []
        self.field_names = ['first_name', 'last_name', 'gender']


    def create_contact_dict(self, contact_tuple):
        # if len(contact_tuple) != 3:  # catching incorrect number args passed in tuple
        #     raise ValueError("The wrong number of arguments were passed to create_contact_dict\n"
        #                      + str(len(contact_tuple)) + " arguments were passed instead of 3")
        return ({"first_name": contact_tuple[0],
                 "last_name": contact_tuple[1],
                 "gender": contact_tuple[2]})

    # if str(contact_tuple[0]).isalpha():  # type checking ID type, changing to int
    #     int(contact_tuple[0])

    def handle_input_contact_row_to_list(self):
        # first_name, last_name, gender = input(
        #     'Please enter the first name, last name, and gender, separated by a space\n').split()
        # return (first_name,
        #         last_name,
        #         gender)
        # TODO: implement try catch block
        correct_input = False
        while not correct_input:  # input loop to ensure correct number arguments passed
            try:
                first_name, last_name, gender = input(
                    'Please enter the first name, last name, and gender, separated by a space\n').split()
            # if error, handle it here
            except Exception as e:
                print(e)  # prints error message
                print('An example of acceptable input is: Jesus Christ female')
            # else if no error, exit loop and return input contact tuple
            else:
                correct_input = True
        return (first_name,
                last_name,
                gender)


    # def create_contact_dict(m_first_name: str, m_last_name: str, m_gender: str):
    #     return ({"first_name": m_first_name,
    #              "last_name": m_last_name,
    #              "gender": m_gender})
    #
    # # catching case of int vs string as ID
    # def create_contact_dict(m_first_name: str, m_last_name: str, m_gender: str):
    #     return ({"first_name": m_first_name,
    #              "last_name": m_last_name,
    #              "gender": m_gender})
    #
    # #  just string arguments
    # def create_contact_dict(m_first_name, m_last_name, m_gender):
    #     return ({"first_name": m_first_name,
    #              "last_name": m_last_name,
    #              "gender": m_gender})


    def store_contact_in_table(self, contact_dict):
        self.contacts_list.append(contact_dict)
        self.current_index += 1

    # TODO: still need to save it to .txt via csv
    def add_contact(self):                          # calls corresponding methods to create and store contact into contacts_list
        self.store_contact_in_table(                # inserts a dictionary into the contact table (list of dicts)
            self.create_contact_dict(               # returns a list as a dictionary labelled for contact table
                self.handle_input_contact_row_to_list()    # handles input and returns list tuple of contact entry (f_name, l_name, gender)
            )
        )

        # ct.store_contact_in_table(  # inserts a dictionary into the contact table (list of dicts)
        #     ct.create_contact_dict(  # returns a list as a dictionary labelled for contact table
        #         ct.handle_input_contact_row_to_list()
        #         # handles input and returns list tuple of contact entry (f_name, l_name, gender)
        #     )

    def print_contacts(self):
        if not self.contacts_list:
            f'The table of contacts is empty'
        else:
            f'Contacts table size: {len(self.contacts_list)}  '
            print(self.contacts_list)

            # f'{self.contacts_list[0]}'
            # for header, rows in zip(headers, columns):
            #     print("{}: {}".format(header, ", ".join(rows)))
            #
            # for index in range(len(self.contacts_list) -1, -1, -1)

    def write_new_contact_to_csv_file(self):
        f''

    # def edit_contact(self):

