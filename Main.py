import argparse
import sys
from show import Display
from change import Changer

class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write(f'error: {message}\n')
        self.print_help()
        sys.exit(2)

my_parser = MyParser(prog='Contact Book App',
                     description='This app manages your contacts. '
                                 'Choose one relevant option to access '
                                 'the functionality.')
my_group = my_parser.add_mutually_exclusive_group(required=True)
my_group.add_argument('-list', action='store_true',
                      help="Use this option to display all contacts.")
my_group.add_argument('-group', action='store', nargs='+',
                       help="Use '-group name1 name2' to display contacts "
                            "from groups 'name1' and 'name2'")
my_group.add_argument('-contact', action='store', nargs='+',
                       help="Use '-contact surname1 surname2' to display "
                            "specific contacts with 'surname1' and 'surname2'")
my_group.add_argument('-add', action='store_true',
                       help='Use to add new contact')
my_group.add_argument('-edit', action='store_true',
                       help='Use to edit contact')
my_group.add_argument('-delete', action='store_true',
                       help='Use to delete contact')

args = my_parser.parse_args()

if args.list:
    app = Display('List')
if args.group:
    app = Display('Group', args.group)
if args.contact:
    app = Display('Contacts', args.contact)
if args.add:
    app = Changer('Add')
if args.edit:
    app = Changer('Edit')
if args.delete:
    app = Changer('Delete')