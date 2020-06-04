def move_maker(board, color):
    import copy
    list_of_boards = []
    if color == 1:
        for row in board:
            index = 0
            for i in row:
                if row[i] == 0:
                    pass
                elif row[i] == 2:
                    pass
                else:
                    if board[index+1][i] == 0:
                        newboard = copy.deepcopy(board)
                        newboard[index+1][i] = newboard[index][i]
                        newboard[index][i] = 0
                        list_of_boards.append(newboard)
                    elif board[index+1][i+1] == 2:
                        newboard = copy.deepcopy(board)
                        newboard[index+1][i+1] = newboard[index][i]
                        newboard[index][i] = 0
                        list_of_boards.append(newboard)
                    elif board[index+1][i-1] == 2:
                        newboard = copy.deepcopy(board)
                        newboard[index+1][i-1] = newboard[index][i]
                        newboard[index][i] = 0
                        list_of_boards.append(newboard)
                    else:
                        pass
            index += 1
    if color == 2:
        for row in board:
            index = 0
            for i in row:
                if row[i] == 0:
                    pass
                elif row[i] == 1:
                    pass
                else:
                    try:
                        board[index-1][i] == 0
                            newboard = copy.deepcopy(board)
                            newboard[index-1][i] = newboard[index][i]
                            newboard[index][i] = 0
                            list_of_boards.append(newboard)
                    except:
                        except Exception
                    try:
                        board[index-1][i+1] == 1:
                            newboard = copy.deepcopy(board)
                            newboard[index-1][i+1] = newboard[index][i]
                            newboard[index][i] = 0
                            list_of_boards.append(newboard)
                    except:
                        except Exception
                    try:
                        board[index-1][i-1] == 1:
                            newboard = copy.deepcopy(board)
                            newboard[index-1][i-1] = newboard[index][i]
                            newboard[index][i] = 0
                            list_of_boards.append(newboard)
                    except:
                        except Exception
                    else:
                        pass
            index += 1
    board = list_of_boards
    return [board]
