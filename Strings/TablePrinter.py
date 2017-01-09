def print_table(table_data):
    col_widths = [0] * len(table_data)
    for row in range(len(table_data)):
        for colStr in table_data[row]:
            if len(colStr) > col_widths[row]:
                col_widths[row] = len(colStr)

    row = len(table_data)
    for col in range(len(table_data[0])):
        rowStr = ''
        for i in range(row):
            rowStr += table_data[i][col] + ' '
        print(rowStr.rjust(sum(col_widths)))


tableData = [['apples', 'oranges', 'cherries', 'bananas'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

print_table(tableData)