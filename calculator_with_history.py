HISTORY_FILE = "history.text"

def show_history():
    #mode r pass read- file handling
    file = open(HISTORY_FILE, 'r')
    lines = file.readlines()
    if len(lines) == 0:
        print("No history found!")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()
    
def clear_history():
    #file overwrite & mode w for write
    file = open(HISTORY_FILE, 'w')
    file.close()
    print('History cleared.')
    
def save_to_history(equation,result):
    file = open(HISTORY_FILE, 'a')
    #a for append
    file.write(equation + "=" + str(result) + "\n")
    file.close()
    
def calculate(user_input): 
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input. Use format:number operator number (e.g 8 + 8)")
        return
    
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])
    
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 + num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print('Cannot Divide by zero!')
        return
        result = num1 / num2
    else:
        print("Invalid operator. USE ONLY + - * /")
        return

#to remove 2.0, 0 when changing to float
    if int(result) == result:
        # change 4.0 to 4 to show clearly
        result = int(result)
    print("Result:", result)
    save_to_history(user_input, result)
    
def main():
    print('---SIMPLE CALCULATOR (type history, clear or exit)')
    
    #while loop
    while True:
        user_input = input("Enter calculation (+ - * /) or command (history, clear, exit)")
        if user_input == "exit":
            print("Goodbye!")
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
        else:
            calculate(user_input)
            
main()