def l657(moves):
    return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")
    # a = [0,0]
    # moves_list = list(moves)
    # for i in range(len(moves_list)):
    #     if moves_list[i] == 'U':
    #         a[1] = a[1]+1
    #     elif moves_list[i] == 'D':
    #         a[1] = a[1]-1
    #     elif moves_list[i] == 'L':
    #         a[0] = a[0]-1
    #     elif moves_list[i] == 'R':
    #         a[0] = a[0]+1
    #
    # if a == [0,0]:
    #     return True
    # return False


print(l657("UD"))
