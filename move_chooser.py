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
                        if col_index = 0:
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
                            if no_moves = num_2:
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
        board_values[board] = value
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
        board_values[board] = value