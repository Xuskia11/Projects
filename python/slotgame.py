import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}
symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winnings(columns, lines, bet, vaules):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbo_to_check = column[line]
            if symbol != symbo_to_check:
                break
        else:
            winnings += vaules[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines



def get_slot_machine_spin(rows, cols, symbols):
    all_symbold = []
    for i, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbold.append(i)
    

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbold[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row],end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("What would you like to deposit?: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please make a bid greater than 0. ")
        else:
            print("Enter a real type of money")
    return amount


def number_of_lines():
    while True:
        lines = input("Enter the number of lines between (1-"+ str(MAX_LINES) + ")?: ")
        if lines.isdigit():
            lines = int(lines)
            if lines >= 1 and lines <=3:
                break
            else:
                print("PLease enter a valid number. ")
        else:
            print("Must be a number. ")
    return lines


def get_bet():
    while True:
        bet = input("how much would you like to bet on each line?: $")
        if bet.isdigit():
            bet = int(bet)
            if bet >=1 and bet <=100:
                break
            else:
                print(f"Please enter valid bet between ${MIN_BET}-${MAX_BET}")
        else:
            print("Must be a number. ")
    return bet
def spin(balance):
    lines = number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Don't have enough money.Your currenty balance is ${balance}. ")
        else:
            break
    print(f"Your are betting ${bet} on {lines}. Total bet is ${total_bet}.")


    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet



def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin (q to quit). ")
        if answer == "q":
            break
        balance += spin(balance)
    
    print(f"You left with ${balance}")



main()
        



    

