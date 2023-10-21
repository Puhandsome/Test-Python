import random

MAX_LINES = 3 #Upper case to make the value cannot change
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3
#Oods for symbols in a slot machine
symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}
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
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ") #Added 2 strings together
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

#Main running functions
def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True: #To check if the total bet is greater than the balance or not
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}") #if the balnce is greater than the bet then print this line
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count) #Generate a slot machine
    print_slot_machine(slots)

main()