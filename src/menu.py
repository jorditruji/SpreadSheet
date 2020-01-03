import sys
import os
sys.path.append(os.getcwd()[:os.getcwd().index('src')])

from src.spreadsheet import SpreadSheet

class Menu:
    """
    Display a menu and respond to choices when run.
    """
    def __init__(self):
        # Options to be displayed in a .txt file
        file_text = open("resources/menu_options.txt", "r")
        self.text_menu = file_text.read()

        self.spreadsheet = None
        self.choices = {
                "1": self.new_spreadsheet,
                "2": self.save_spreadsheet,
                "3": self.load_spreadsheet,
                "4": self.set_cell_value,
                "5": self.get_cell_value,
                "6": self.copy_cell,
                "7": self.quit
        }

    def display_menu(self):
        print(self.text_menu)

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def option_description(self):
        pass

    def new_spreadsheet(self):
        print('New Spreadsheet Selected')
        self.spreadsheet = SpreadSheet()
        print('Spreadsheet created !')

    def save_spreadsheet(self):
        print('Save Spreadsheet Selected')
        if self.spreadsheet is not None:
            try:
                name = input('Name of the file: ')
                self.spreadsheet.save(name=name)
            except Exception as e:
                print(e.custom_message)
        else:
            print('There is no initialized Spreadsheet Class.\n')

    def load_spreadsheet(self):
        print('Load Spreadsheet Selected')
        self.spreadsheet = SpreadSheet()
        try:
            name = input('Name of the file: ')
            self.spreadsheet = self.spreadsheet.load(name=name)
        except Exception as e:
            print(e.custom_message)

    def set_cell_value(self):
        print('Set a cell value Selected')
        #TODO: Considerar no ficar tantes compovacions aqui
        alias = input("Enter cell alias: ")
        try:
            # Check if cell exists
            cell, indx = self.spreadsheet.get_cell(alias=alias)
            print('Cell {} already exists'.format(alias))

            # Ask for replace
            replace = input('Do you want to replace it (y/n)? ')
            if replace == 'y':
                value = input("Enter a value or expression: ")

                self.spreadsheet.update_cell(alias=alias, value=value)
        except Exception as e:
            print(e.custom_message)
            # Cell don't exist, it can be created
            value = input("Enter a value or expression: ")
            self.spreadsheet.set(alias=alias, value=value)

    def get_cell_value(self):
        print('Get a cell value')
        alias = input("Enter cell alias: ")
        try:
            cell, _ = self.spreadsheet.get_cell(alias=alias)
            cell.printify()
        except Exception as e:
            print(e.custom_message)

    def copy_cell(self):
        print('Copy cell content')
        alias_origin = input('Enter cell to be coppied: ')
        range = input("Enter cell or range of cells: ")
        self.spreadsheet.copy_cell(alias_origin=alias_origin, range=range)

    def quit(self):
        print("Bye!")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
