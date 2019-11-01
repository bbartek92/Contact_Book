import database_handler as db

class Display:
    def __init__(self, caller, values=()):
        self.padding = 35
        print('In Show via', caller, values)
        if caller == 'List':
            self.select_all()
        if caller == 'Group':
            print('group')
            self.select_group(values)
        if caller == 'Contacts':
            print('contacts')
            self.select_contacts(values)

    def select_all(self):
        connector = db.DataAccess()
        connector.connect()
        result = connector.fetch_data_all()
        self.pretty_list(result)

    def select_group(self, values):
        print('select group', 'with values', values)
        connector = db.DataAccess()
        connector.connect()
        result = connector.fetch_filtered_data('group', values)
        self.pretty_group(result)

    def select_contacts(self, values):
        print('select contacts', 'with values', values)
        connector = db.DataAccess()
        connector.connect()
        result = connector.fetch_filtered_data('contacts', values)
        self.pretty_contact(result)

    def pretty_list(self, data):
        print(f'+', '-'*self.padding, '+', sep='')
        print(f'{"| Contacts":<{self.padding}} |')
        print(f'+', '-'*self.padding, '+', sep='')
        for record in data:
            print(f'{F"| {record.name} {record.surname}":<{self.padding}} |')
        print(f'+', '-'*self.padding, '+', sep='')

    def pretty_group(self, data):
        print(f'+', '-'*self.padding, '+', sep='')
        print(f'{"| Contacts":<{self.padding}} |')
        print(f'+', '-'*self.padding, '+', sep='')
        for contact in data:
            for record in contact:
                print(f'{F"| {record.name} {record.surname}":<{self.padding}} |')
        print(f'+', '-'*self.padding, '+', sep='')

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

if __name__=="__main__":
    print("This is show module.")
