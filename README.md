# Console Pyramid Maker

A simple Python console program that generates different types of pyramids using loops.

## Features

The program supports:

* Right pyramid
* Isosceles pyramid

## How It Works

The user chooses the pyramid type and enters the number of layers.

The program then uses nested `for` loops to print the selected pyramid.

## Example

```text
Enter the pyramid type: right
Enter the number of layers: 4

*
* *
* * *
* * * *
```

For an isosceles pyramid:

```text
Enter the pyramid type: isosceles
Enter the number of layers: 4

   *
  ***
 *****
*******
```

## Concepts Used

* Python
* `input()`
* `if / elif / else`
* `for` loops
* Nested loops
* `range()`
* String formatting with `end`

## How to Run

```bash
python pyramid_maker.py
```
