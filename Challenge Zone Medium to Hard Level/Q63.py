"""
Write a Python program which adds up columns and rows of given table as shown in the specified figure.

25 69 51 26
68 35 29 54
54 57 45 63
61 68 47 59
"""


def add_table_rows_and_columns(table):
    # Calculate the sum of each row
    row_sums = [sum(row) for row in table]

    # Calculate the sum of each column
    col_sums = [sum(col) for col in zip(*table)]

    return row_sums, col_sums


# Given table
table = [
    [25, 69, 51, 26],
    [68, 35, 29, 54],
    [54, 57, 45, 63],
    [61, 68, 47, 59]
]

# Add rows and columns
row_sums, col_sums = add_table_rows_and_columns(table)

# Print the table
for row in table:
    print(*row)

# Print the sums of rows
print("Row sums:", row_sums)

# Print the sums of columns
print("Column sums:", col_sums)
