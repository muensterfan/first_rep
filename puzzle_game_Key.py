from puzzle_functions_Key import puzzle_maker, puzzle_matcher
print("Welcome, Player 1")
puzzle_solution = input("Enter your puzzle solution. Use all lower-cased letters: ")
let_ind = True
for let in puzzle_solution:
    let_ind2 = let.isalpha() and let.islower()
    if not let_ind2 and let != " ":
        let_ind = False
while not let_ind:
    puzzle_solution = input("Please try again. Only lower case letters are allowed: ")
    let_ind = True
    for let in puzzle_solution:
        let_ind2 = let.isalpha() and let.islower()
        if not let_ind2 and let != " ":
            let_ind = False
puzzle_board = puzzle_maker(puzzle_solution)
print(puzzle_board)
for line in range(10):
    print("")
print("Welcome, Player 2")
print("Here is the puzzle board: " + puzzle_board)
tries_left = 6
letters_tried = ""
print("You have " + str(tries_left) + " incorrect guesses left.")
print("")
cur_guess = input("Guess a letter (lower case) or type 0 to give up!: ")
cur_guess_valid = len(cur_guess) == 1 and cur_guess.isalpha() and cur_guess.islower() and not cur_guess in letters_tried
while not cur_guess_valid and cur_guess != "0":
    cur_guess = input("Try a valid lower-cased letter that hasn't been picked or 0 to give up: ")
    cur_guess_valid = len(cur_guess) == 1 and cur_guess.isalpha() and cur_guess.islower() and not cur_guess in letters_tried
while cur_guess != "0" and tries_left > 0 and puzzle_board != puzzle_solution:
    letters_tried += cur_guess
    match_result = puzzle_matcher(puzzle_solution, puzzle_board, cur_guess)
    if match_result == "0":
        tries_left -= 1
        print("")
        print("Wrong!")
        print("You have " + str(tries_left) + " incorrect guess left.")
        print("")
    else:
        puzzle_board = match_result
        print("")
        print("Good guess!")
        print("")
    if tries_left > 0 and puzzle_board != puzzle_solution:
        print("Current puzzle board: " + str(puzzle_board))
        print("Letters tried: " + ''.join(sorted(str(letters_tried))))
        cur_guess = input("Enter your next letter or type 0 to give up: ")
        cur_guess_valid = len(cur_guess) == 1 and cur_guess.isalpha() and cur_guess.islower() and not cur_guess in letters_tried
        while not cur_guess_valid and cur_guess != "0":
            cur_guess = input("Try a valid lower-cased letter that hasn't been picked or 0 to give up: ")
            cur_guess_valid = len(cur_guess) == 1 and cur_guess.isalpha() and cur_guess.islower() and not cur_guess in letters_tried
if puzzle_board == puzzle_solution:
    print("Congratulations! You win!")
elif tries_left == 0:
    print("You lose! The solution was: " + puzzle_solution)
else:
    print("Have a good day.")

