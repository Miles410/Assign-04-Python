#!/usr/bin/env python3
# Created By: Boluwatife Dada
# created on April 25
# This program creates a multiplication times table from 1-9


def multiplication_table():
    """
    Prints the 0-9 multiplication table.
    """
    for i in range(10):
        for j in range(10):
            product = i * j
            print(f"{i} X {j} = {product}")


if __name__ == "__main__":
    multiplication_table()
