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

Referenced cells in expression are handled by subscribing observers inside the cells. So when a value is updated,
the cells that have this cell inside an expression is notified to be evaluated again.

Following this [reference](https://refactoring.guru/design-patterns/observer).

## Usage
Execute `python menu.py`

8 options are available: 
1) Create new Spreadsheet: We will need to select this option if we want to start working with an empty new spreadsheet.
2) Save Spreadsheet: We can save the current Spreadsheet with its content into a S2V text file, which can be opened later with any .csv reader (i.e. Excel)
3) Load Spreadsheet: We can also start working with an already created spreadsheet. This option will load its content and we will be able to modify it afterwards.
4) Set Value: When an spreadsheet is created (it can be a new one or a loaded one), we are able to set values to its cells. The "name" of the cell will be asked (i.e. A1, B3, C5...) and then the content we want to add. It can be a number, a string or an expression. If the expression involves other cells, those need to have already some value.
5) Get Value: We can see the value of a chosen cell. If this cell contains an expression, we will get the expression plus de evaluated result.
6) Copy cell: The content of one cell can be copied to another cell or rang of cells. It also takes into account absolute references.
7) Print current Spreadsheet: A tool to visualize in terminal the current spreadsheet, so we can keep track of the cells that already have a content and which one is it.
8) Quit: Finishes the execution of the program.

## Tests
Execute `python tests.py` 
