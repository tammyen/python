##Lesley Tam Uyen Tran
##September 7, 2018
##ECS 10 Eiselt
##
##prog5.py

#Problem 1
def addTables(table1, table2):
    """function will ask for two arguments, both being a 2 dimmen-
    sional tables. each value in the first table will be added with
    a value in the second table with the same index and then
    will be added into a third table. the third table will be
    returned."""
    table3 = []
    index1 = 0 #this is the row
    for row1 in table1:
        index2 = 0 #this is the column
        add_table = [] #makes separate lists like in the input
        for num1 in row1:
            num_add = num1 + table2[index1][index2]
            #the two indexes will be used to find the value in
            #table 2
            index2 += 1
            add_table = add_table + [num_add]
            #value found will be added to a preliminary table
        table3 = table3 + [add_table]
        #preliminary table will be added to the final table
        #to account for rows
        index1 += 1
    return(table3)
