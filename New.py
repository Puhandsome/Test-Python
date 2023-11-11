import random

MAX_LINES = 3 #Upper case to make the value cannot change
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3
#Oods for symbols in a slot machine
symbol_count = {
    "A" : 4,
    "B" : 6,
    "C" : 8,
    "D" : 10
}
#If this symbol occurs, multiply by this number
symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}
   

#User's deposit
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

#How many lines do the user want to bet on?
def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number.")
    return lines

#Get the amount of money that user want to bet on
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.") #f is to call function in a string
        else:
            print("Please enter a number.")
    return amount

#To generate a random slot machine
def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items(): # A,2 in keys and items
        for _ in range(symbol_count): #in range 2
            all_symbols.append(symbol) # A,A

    columns = []
    for _ in range(cols): #if cols = 3, do this loop 3 times
        column = []
        current_symbols = all_symbols[:] #Create a copy of the list
        for _ in range(rows):
            value = random.choice(current_symbols) #Randomly pick a symbol from the copied list
            current_symbols.remove(value) #To remove the characters that have been used
            column.append(value) #To add a value to the column
        
        columns.append(column) #Add the column to the columns list
    return columns #return all values in the loop to the columns

#To print out the slot machine
def print_slot_machine(columns):
    for row in range(len(columns[0])): #loops through each rows in the first column(length of rows)
        for i,column in enumerate(columns): #enumerate is used to get both index(i) and the content(column)
            if i != len(columns) - 1: #print the pipe operator when the index is not 2
                print(column[row],end = " | ")
            else:
                print(column[row],end = " ") #Don't print the pipe operator at the end
        print() #move to the next line and start a new row

#To check how much the user's have won the bet
def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines): #Check the symbol in a line
        symbol = columns[0][line] #Check the first column and check lines
        for column in columns: #loop to check all symbols by columns
            symbol_to_check = column[line] #check the column at whatever rows you are looking at
            if symbol != symbol_to_check:
                break
        else: # if the for loop doesn't break out then come to else(if they win)
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

#Main running functions
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count) 
    print_slot_machine(slots) 
    winnings,winning_line = check_winnings(slots,lines,bet,symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_line) #print with space if don't win then it will print out nothing
    return winnings - total_bet 

#Looping the program
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == 'q':
            break
        balance += spin(balance)
    
    print(f"You left with ${balance}.")


main()