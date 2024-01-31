import random

# Maximum number of lines that can be played
MAX_LINES = 3

# Maximum bet per line
MAX_BET = 100
MIN_BET = 1

# Number of rows and columns in the slot machine

ROWS = 3
COLS = 3

# Dictionary representing the count of each symbol
symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}
# Dictionary representing the value of each symbol
symbol_value = {"A": 6, "B": 5, "C": 4, "D": 3}


# Function to check for winning combinations in the slot machine
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []

    # Iterate over each line
    for line in range(lines):
        # Get the symbol from the first column in the current line
        symbol = columns[0][line]

        # Check if all symbols in the line are the same
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            # If all symbols in the line are the same, calculate winnings
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


# Function to generate a random spin of the slot machine
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            # Randomly select a symbol for each position in the column
            value = random.choice(all_symbols)

            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    print(columns)
    return columns


# Function to print the slot machine output
def print_splot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


# Function to prompt the player to deposit money
def deposite():
    while True:
        amount = input("Enter amount you would like to deposite? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount


# Function to prompt the player to choose the number of lines to bet on
def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a  valid number.")
        else:
            print("Please enter a number.")
    return lines


# Function to prompt the player to choose the bet amount
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount


# Function to perform a spin of the slot machine
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > balance:
            print(
                f"You do not have enough amount to bet. Your current balance is ${balance}"
            )
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. The total bet amount is ${total_bet}"
    )

    # Generate a spin of the slot machine
    slot = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_splot_machine(slot)

    # Check for winning combinations and calculate winnings
    winnings, winnings_lines = check_winnings(slot, lines, bet, symbol_value)
    print(f"You have won {winnings}")
    print(f"you won on lines:", *winnings_lines)

    # Calculate net winnings (winnings - total bet) and return
    return winnings - total_bet


# Main function to start the game
def main():
    # Prompt the player to deposit money
    balance = deposite()

    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        # Perform a spin and update the balance
        balance += spin(balance)

    print(f"You left with ${balance}")


# main function
main()
