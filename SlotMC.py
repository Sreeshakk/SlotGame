import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            if column[line] != symbol:
                break
            else:
                winnings += values[symbol] * bet
            winning_lines.append(line + 1)
        return winnings, winning_lines

def machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end="|")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("How much do you want to deposit?: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a number greater than 0.")
        else:
            print("Please enter a positive number.")
    return amount

def number_of_lines():
    while True:
        lines = input("How many lines to bet on(1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a VALID NUMBER.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        bet = input("How much do you want to bet on each line?: $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Please enter a VALID NUMBER. {MIN_BET} - {MAX_BET}.")
        else:
            print("Please enter a VALID NUMBER.")
    return bet

def game(balance):
    lines = number_of_lines()
    while True:
        bet = get_bet()
        total_amount = bet * lines
        if total_amount > balance:
            print(f"You don't have enough money. Your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. The total bet amount is ${total_amount}")

    slots = machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check(slots, lines, bet, symbol_value)
    print(f"You won ${winnings} on", *winning_lines)
    return balance - total_amount + winnings

def main():
    balance = deposit()
    while True:
        print (f"Current balance: ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += game(balance)
    print(f"You left with ${balance}")

main()
