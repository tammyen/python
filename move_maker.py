def move_maker(board, color):
    import copy
    list_of_boards = []
    if color == 1:
        index_row = 0
        for row in board:
            index_col = 0
            for i in row:
                if i == 1:
                    if board[index_row+1][index_col] == 0:
                        newboard = copy.deepcopy(board)
                        newboard[index_row+1][index_col] = newboard[index_row][index_col]
                        newboard[index_row][index_col] = 0
                        list_of_boards.append(newboard)
                    elif index_col == 0 or index_col < len(row) - 2:
                        if board[index_row+1][index_col+1] == 2:
                            newboard = copy.deepcopy(board)
                            newboard[index_row+1][index_col+1] = newboard[index_row][index_col]
                            newboard[index_row][index_col] = 0
                            list_of_boards.append(newboard)
                        else:
                            pass
                    elif index_col != 0 or index_col < len(row) - 1:
                        if board[index_row+1][index_col-1] == 2:
                            newboard = copy.deepcopy(board)
                            newboard[index_row+1][index_col-1] = newboard[index_row][index_col]
                            newboard[index_row][index_col] = 0
                            list_of_boards.append(newboard)
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
                index_col += 1
            index_row += 1
    elif color == 2:
        index_row = 0
        for row in board:
            index_col = 0
            for i in row:
                if i == 2:
                    if board[index_row-1][index_col] == 0:
                        newboard = copy.deepcopy(board)
                        newboard[index_row-1][index_col] = newboard[index_row][index_col]
                        newboard[index_row][index_col] = 0
                        list_of_boards.append(newboard)
                    if index_col == 0 or index_col < len(row) - 2:
                        if board[index_row-1][index_col+1] == 1:
                            newboard = copy.deepcopy(board)
                            newboard[index_row-1][index_col+1] = newboard[index_row][index_col]
                            newboard[index_row][index_col] = 0
                            list_of_boards.append(newboard)
                        else:
                            pass
                    if index_col != 0 or index_col < len(row) - 1:
                        if board[index_row-1][index_col-1] == 1:
                            newboard = copy.deepcopy(board)
                            newboard[index_row-1][index_col-1] = newboard[index_row][index_col]
                            newboard[index_row][index_col] = 0
                            list_of_boards.append(newboard)
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
                index_col += 1
            index_row += 1
    else:
        pass
    return(list_of_boards)

def move_chooser(list_of_boards, color):
    board_values = {}
    for board in list_of_boards:
        num_1 = 0
        num_2 = 0
        for row in board:
            for i in row:
                if i == 1:
                    num_1 += 1
                elif i == 2:
                    num_2 += 1
                else:
                    pass
        value = 0
        if color == 1:
            row_index = 0
            for row in board:
                col_index = 0
                for i in row:
                    if i == 1 and row_index == len(row)-1:
                        value += 10
                        break
                    elif i == 2 and row_index == 0:
                        value -= 10
                        break
                    elif num_2 == 0:
                        value += 10
                        break
                    elif i == 2:
                        no_moves = 0
                        if col_index == 0:
                            if board[row_index-1][col_index] != 0:
                                if board[row_index-1][col_index+1] != 1:
                                    no_moves += 1
                        elif col_index == len(row)-1:
                            if board[row_index-1][col_index] != 0:
                                if board[row_index-1][col_index-1] != 1:
                                    no_moves +=1
                        elif col_index != 0 and col_index != len(row) - 1:
                            if board[row_index-1][col_index] != 0:
                                if board[row_index-1][col_index+1] != 1:
                                    if board[row_index-1][col_index-1] != 1:
                                        no_moves += 1
                        else:
                            if no_moves == num_2:
                                value += 10
                    elif i == 1:
                        no_moves = 0
                        if col_index == 0:
                            if board[row_index + 1][col_index] != 0:
                                if board[row_index + 1][col_index + 1] != 2:
                                    no_moves += 1
                        elif col_index == len(row) - 1:
                            if board[row_index + 1][col_index] != 0:
                                if board[row_index + 1][col_index - 1] != 2:
                                    no_moves += 1
                        elif col_index != 0 and col_index != len(row) - 1:
                            if board[row_index + 1][col_index] != 0:
                                if board[row_index + 1][col_index + 1] != 2:
                                    if board[row_index + 1][col_index - 1] != 2:
                                        no_moves += 1
                        else:
                            if no_moves == num_1:
                                value -= 10
                    else:
                        value = num_1 - num_2
                col_index += 1
            row_index += 1
        board_values[str(board)] = value
        if color == 2:
            row_index = 0
            for row in board:
                col_index = 0
                for i in row:
                    if i == 2 and row_index == 0:
                        value += 10
                        break
                    elif i == 1 and row_index == len(row)-1:
                        value -= 10
                    elif num_1 == 0:
                        value += 10
                        break
                    elif i == 1:
                        no_moves = 0
                        if col_index == 0:
                            if board[row_index+1][col_index] != 0:
                                if board[row_index+1][col_index+1] != 2:
                                    no_moves += 1
                        elif col_index == len(row)-1:
                            if board[row_index+1][col_index] != 0:
                                if board[row_index+1][col_index-1] != 2:
                                    no_moves += 1
                        elif col_index != 0 and col_index != len(row) - 1:
                            if board[row_index+1][col_index] != 0:
                                if board[row_index+1][col_index+1] != 2:
                                    if board[row_index+1][col_index-1] != 2:
                                        no_moves += 1
                        else:
                            if no_moves == num_1:
                                value += 10
                    elif i == 2:
                        no_moves = 0
                        if col_index == 0:
                            if board[row_index - 1][col_index] != 0:
                                if board[row_index - 1][col_index + 1] != 1:
                                    no_moves += 1
                        elif col_index == len(row) - 1:
                            if board[row_index - 1][col_index] != 0:
                                if board[row_index - 1][col_index - 1] != 1:
                                    no_moves += 1
                        elif col_index != 0 and col_index != len(row) - 1:
                            if board[row_index - 1][col_index] != 0:
                                if board[row_index - 1][col_index + 1] != 1:
                                    if board[row_index - 1][col_index - 1] != 1:
                                        no_moves += 1
                        else:
                            if no_moves == num_2:
                                value -= 10
                    else:
                        value = num_2 - num_1
                col_index += 1
            row_index += 1
        board_values[str(board)] = value
    import operator
    best_board = max(board_values.items(), key=operator.itemgetter(1))[0]
    return best_board
board = [[0, 1, 1], [1, 0, 0], [2, 2, 2]]
mlist = move_maker(board, 2)
x = move_chooser(mlist,2)
print(x)