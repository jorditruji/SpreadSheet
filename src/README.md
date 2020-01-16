#Spreadsheet

##Introduction
Spreadsheet with some core components implemented, which can be used
through a textual menu interface.

###Project Requirements:
Spreadsheet should support textual, numeric and expression cells. The types of values are defined as:
1. `ExpressionCell`: `float`
2. `NumericCell`: `float`
3. `TextCell`: `string`

The cells are identified by an alias which contains the column label `(A-ZZ)` and the 
row number `(1-...)` in `string` format.

####Expressions:
Expression cells value always start with `=`,supports all kind of basic operands and also this functions:
1. `MIN()/min()`
2. `MAX()/max()`
3. `SUM()/sum()`
4. `MEAN()/mean()`

A function can be called inside another function.

#####Parser and evaluator:
To handle the cells involved in the operation, ranges defined by `first_alias:last_alias` and single alias 
separed by `,` can be used.

#####Copy cell content:
Aliases column and row can be fixed using `$` before column label and/or row number to avoid the changing of
the cells involved in a expression when copying a cell to other cell or cells.
#####Observer:

Referenced cells in expression are handled by subscribing observers inside the cells. So when a value is updated,
the cells that have this cell inside an expression is notified to be evaluated again.

Following this [reference](https://refactoring.guru/design-patterns/observer).

##Usage
Execute `python menu.py`

##Tests
Execute `python tests.py` 