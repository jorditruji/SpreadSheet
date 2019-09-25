import sys
from spreadsheet import SpreadSheet


class Menu:
    """
    Display a menu and respond to choices when run.
    """
    def __init__(self):
        # Options to be displayed in a .txt file
        file_text = open("menu_options.txt", "r")
        self.text_menu = file_text.read()
        # Init spreadsheet by default size [20, 20]
        self.spreadsheet = SpreadSheet([20, 20])
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

    def new_spreadsheet(self):
        print('New Spreadsheet Selected')
        n_rows = input("Number of rows for spreadsheet: ")
        n_cols = input("Number of columns for spreadsheet: ")
        self.spreadsheet = SpreadSheet([int(n_rows), int(n_cols)])

    def save_spreadsheet(self):
        print('Save Spreadsheet Selected')

    def load_spreadsheet(self):
        print('Load Spreadsheet Selected')

    def set_cell_value(self):
        print('Set a cell value')
        posx = input("Index of column: ")
        posy = input("Index of row: ")
        value = input("Enter a value or expression: ")
        # TODO: Com diferenciem el tipus de valor entre string i numeric? -> En un input el valor sempre es string
        # Mirar si es numero??
        self.spreadsheet.set(posx=int(posx), posy=int(posy), value=value)

    def get_cell_value(self):
        print('Get a cell value')
        posx = input("Index of column: ")
        posy = input("Index of row: ")
        cell = self.spreadsheet.get_value_by_pos(posx=int(posx), posy=int(posy))
        print(cell.value)

    def quit(self):
        print("Bye Nerd!")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
