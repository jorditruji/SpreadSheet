# Spreadsheet

## Introduction
Spreadsheet with some core components implemented, which can be used
through a textual menu interface.

### Project Requirements:
Spreadsheet should support textual, numeric and expression cells. The types of values are defined as:
1. `ExpressionCell`: `float`
2. `NumericCell`: `float`
3. `TextCell`: `string`

The cells are identified by an alias which contains the column label `(A-ZZ)` and the 
row number `(1-...)` in `string` format.

#### Expressions:
Expression cells value always start with `=`,supports all kind of basic operands and also this functions:
1. `MIN()/min()`
2. `MAX()/max()`
3. `SUM()/sum()`
4. `MEAN()/mean()`

A function can be called inside another function.

#### Parser and evaluator:
To handle the cells involved in the operation, ranges defined by `first_alias:last_alias` and single alias 
separed by `,` can be used.

Parser and evaluator used is taken from a Python code made by Vera Mazhuga based on [js-expression-eval](https://github.com/silentmatt/js-expression-eval), by Matthew Crumley 


#### Copy cell content:
Any cell can be coppied to a cell or ranges of cells.

Expression cells should change the expression involved cells if these are not fixed with `$`.

Aliases column and row can be fixed using `$` before column label and/or row number to avoid the changing of
the cells involved in a expression when copying a cell to other cell or cells.
#### Observer:

Every type of cell can be subject including expression cells. Only expression cells are the observers
Every cell (subject) have a list of observers. If a cell is involved to an expression, the expression cell will be attached
as an observer of the involved cell. Every time an involved value is changed, the expression cell value will be updated accordingly.

Following this [reference](https://refactoring.guru/design-patterns/observer).

## Design
#### UML Diagram:

![Alt text](resources/img/uml.jpg?raw=true "UML Diagram")

### Design choices and other comments
On the first design cells was stored in a matricial manner, after seeing how the abstract factory pattern worked we thought it would be useful to just create the cells on demand using this factory. However, the container used for storing created cells would be a dictionary having as key alias as keys instead of a plain list if we did the project again.


Managing the dependencies between cells in expressions is not a trivial thing. One single update on a numeric cell can trigger multiple chained updates on other cells. The observer pattern make this problem much easier to solve with few lines of code.

One other comment is the code styliling of the classes used to parse and evaluate expressions is clearly different from the rest of the project and should be adaptated to follow both commenting and coding styles.






## Installation

```
virtualenv --python=python3.6 python_36
source python3.6/bin/activate
git clone https://github.com/jorditruji/SpreadSheet.git
cd SpreadSheet
pip3 install -r requirements.txt
```


## Usage
Execute `python menu.py`
```
SpreadSheet Menu:

1. Create new Spreadsheet
2. Save Spreadsheet
3. Load Spreadsheet
4. Set Value
5. Get Value
6. Copy cell
7. Print current Spreadsheet
8. Quit
Enter an option: 
```
8 options are available: 
1) Create new Spreadsheet: We will need to select this option if we want to start working with an empty new spreadsheet.

2) Save Spreadsheet: We can save the current Spreadsheet with its content into a S2V text file, which can be opened later with any .csv reader (i.e. Excel)

3) Load Spreadsheet: We can also start working with an already created spreadsheet. This option will load its content and we will be able to modify it afterwards.

4) Set Value: When an spreadsheet is created (it can be a new one or a loaded one), we are able to set values to its cells. The "name" of the cell will be asked 
(i.e. A1, B3, C5...) and then the content we want to add. It can be a number, a string or an expression. If the expression involves other cells, those need to have already some value.

5) Get Value: We can see the value of a chosen cell. If this cell contains an expression, we will get the expression plus de evaluated result.

6) Copy cell: The content of one cell can be copied to another cell or range of cells. It also takes into account absolute references.

7) Print current Spreadsheet: A tool to visualize in terminal the current spreadsheet, so we can keep track of the cells that already have a content and which one is it.

8) Quit: Finishes the execution of the program.

## Tests
Execute `python tests.py` 
