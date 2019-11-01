import database_handler as db

class Changer:
    def __init__(self, caller):
        self.n_padding = 12
        self.s_padding = 12
        self.ph_padding = 15
        self.em_padding = 20
        self.bi_padding = 15
        self.gr_padding = 15
        self.padding = 35
        if caller == 'Add':
            self.add_new()
        if caller == 'Edit':
            self.edit_record()
        if caller == 'Delete':
            self.del_old()

    def add_new(self):
        print('To add a new contact, please fill below information')
        name = input('Name: ')
        surname = input('Surname: ')
        phone = input('Phone number: ')
        email = input('Email number: ')
        birthday = input('Birthday date (yyyy/mm/dd): ')
        group = input('Contact Group: ')
        data_list = [name, surname, phone, email, birthday, group]
        self.pretty_print(data_list)
        confirm = input('Add to contact list(Y/N)? ')
        if confirm == 'Y':
            connector = db.DataAccess()
            connector.connect()
            connector.add_data(data_list)
        else:
            exit()

    def edit_record(self):
        print('Choose a contact that you want to edit.')
        old_surname = input('Surname: ')
        data_list = [old_surname]
        connector = db.DataAccess()
        connector.connect()
        result = connector.fetch_filtered_data('contacts', data_list)
        self.pretty_contact(result)
        print('Please provide updated information:')
        name = input('Name: ')
        surname = input('Surname: ')
        phone = input('Phone number: ')
        email = input('Email number: ')
        birthday = input('Birthday date (yyyy/mm/dd): ')
        group = input('Contact Group: ')
        data_list = [name, surname, phone, email, birthday, group]
        connector.edit_data(old_surname, data_list)
        new_data_list = [surname]
        new_result = connector.fetch_filtered_data('contacts', new_data_list)
        self.pretty_contact(new_result)

    def del_old(self):
        print('To delete an old contact, please fill below information.')
        name = input('Name: ')
        surname = input('Surname: ')
        data_list = [name, surname]
        self.pretty_print(data_list)
        confirm = input('Delete to contact list(Y/N)? ')
        if confirm == 'Y':
            connector = db.DataAccess()
            connector.connect()
            connector.del_data(data_list)
        else:
            exit()

    def pretty_print(self, data_list):
        if len(data_list) == 6:
            sep_line = '+' + '-'*self.n_padding + '+' + '-'*self.s_padding + \
                       '+' + '-'*self.ph_padding + '+' + \
                       '-'*self.em_padding + '+' + '-'*self.bi_padding + \
                       '+' + '-'*self.gr_padding + '+'
            print(sep_line)
            print(f'{"| name":<{self.n_padding}}',
                  f'{"| surname":<{self.s_padding}}',
                  f'{"| phone":<{self.ph_padding}}',
                  f'{"| email":<{self.em_padding}}',
                  f'{"| birthday":<{self.bi_padding}}',
                  f'{"| group":<{self.gr_padding}}', '|')
            print(sep_line)
            print('|', f'{data_list[0]:<{self.n_padding}}', '|',
                  f'{data_list[1]:<{self.s_padding}}', '|',
                  f'{data_list[2]:<{self.ph_padding}}', '|',
                  f'{data_list[3]:<{self.em_padding}}', '|',
                  f'{data_list[4]:<{self.bi_padding}}', '|',
                  f'{data_list[5]:<{self.gr_padding}}', '|', sep='')
            print(sep_line)
        else:
            sep_line = '+' + '-'*self.n_padding + '+' + '-'*self.s_padding + '+'
            print(sep_line)
            print(f'{"| name":<{self.n_padding}}',
                  f'{"| surname":<{self.s_padding}}',
                  '|')
            print(sep_line)
            print('|', f'{data_list[0]:<{self.n_padding}}', '|',
                  f'{data_list[1]:<{self.s_padding}}', '|', sep='')
            print(sep_line)

    def pretty_contact(self, data):
        if len(data) == 1:
            label = 'Contact'
        else:
            label = 'Contacts'
        print(f'+', '-'*self.padding, '+', sep='')
        print(f'{f"| {label}":<{self.padding}} |')
        print(f'+', '-'*self.padding, '+', sep='')
        for contact in data:
            for record in contact:
                print(f'{f"| Name {record.name}":<{self.padding}} |')
                print(f'{f"| Surname {record.surname}":<{self.padding}} |')
                print(f'{f"| Phone number {record.phone}":<{self.padding}} |')
                print(f'{f"| Email {record.email}":<{self.padding}} |')
                print(f'{f"| Birthday {record.birthday}":<{self.padding}} |')
                print(f'{f"| Contact Group {record.group}":<{self.padding}} |')
                print(f'+', '-'*self.padding, '+', sep='')

if __name__ == '__main__':
    print('This is change module.')