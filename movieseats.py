num_rows = int(input("The number of rows?"))
num_cols = int(input("The number of columns?"))



row_num = 1
for i in range(num_rows):
    col_letter = "A"
    for j in range(num_cols):
        print(row_num, end='')
        print(col_letter,'',end='' )
        col_letter = chr(ord(col_letter) + 1)
    row_num = row_num + 1
print()