def puzzle_maker(solution):
    puzzle_blank = ""
    puzzle_pos = 0
    all_lets = True
    while all_lets == True and puzzle_pos < len(solution):
#        if solution[puzzle_pos].isalpha() == False and solution[puzzle_pos] != " ":
#            all_lets = False
#        else:
        if solution[puzzle_pos] == " ":
            puzzle_blank += " "
        else:
            puzzle_blank += "_"
        puzzle_pos += 1
    if all_lets == True:
        return puzzle_blank
#    else:
#        return 1

def puzzle_matcher(puzzle_solution, puzzle_board, let_guess):
    if not let_guess in puzzle_solution:
        return "0"
    else:
        curpos = 0
        new_puzzle_board = ""
        while curpos < len(puzzle_solution):
            if puzzle_solution[curpos] == let_guess:
                new_puzzle_board += let_guess
            else:
                new_puzzle_board += puzzle_board[curpos]
            curpos += 1
        return new_puzzle_board