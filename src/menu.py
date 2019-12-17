import sys
from src.spreadsheet import SpreadSheet


class Menu:
    """
    Display a menu and respond to choices when run.
    """
    def __init__(self):
        # Options to be displayed in a .txt file
        file_text = open("resources/menu_options.txt", "r")
        self.text_menu = file_text.read()
        # Init spreadsheet by default size [20, 20]
        self.spreadsheet = None
        self.choices = {
                "1": self.new_spreadsheet,
                "2": self.save_spreadsheet,
                "3": self.load_spreadsheet,
                "4": self.set_cell_value,
                "5": self.get_cell_value,
                "6": self.quit
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

    def load_spreadsheet(self):
        print('Load Spreadsheet Selected')

    def set_cell_value(self):
        print('Set a cell value Selected')
        is_valid = False

        # is_valid condition to retry the input values
        while is_valid is not True:
            try:
                alias = input("Enter cell alias: ")
                value = input("Enter a value or expression: ")
                self.spreadsheet.set(alias=alias, value=value)
                is_valid = True
            except Exception as e:
                print(e)
                print('Set cell content again...')

    def get_cell_value(self):
        print('Get a cell value')
        alias = input("Enter cell alias: ")
        cell = self.spreadsheet.get_cell(alias=alias)
        print(cell.value)

    def quit(self):
        print("Bye Nerd!")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
