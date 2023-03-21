def user_input():
    print ("enter what you would like to calculate.")
    userinput = input("function: ")
    return userinput

def isNumber(Number:str):
    if(Number >= "0" and Number <= "9"):
        return True
    return False

def isOperator(Operator:str):
    if(Operator == "("):
        return True
    if(Operator == ")"):
        return True
    if(Operator == "^"):
        return True
    if(Operator == "+"):
        return True
    if(Operator == "-"):
        return True
    if(Operator == "*"):
        return True
    if(Operator == "/"):
        return True
    
def Calc(Operator_number:int,Math_input:list):
    print(Math_input)
    if (len(Math_input) == 2):
        print("got here =",sum(Math_input))
        return sum(Math_input)
    else:
        Operator = Math_input[Operator_number]
        First_num = float(Math_input[Operator_number-1])
        Second_num = float(Math_input[Operator_number+1])
    #print(First_num,":",Operator,":",Second_num)
    if(Operator == "^"):
        return pow(First_num,Second_num)
    if(Operator == "*" or Operator == "/"):
        if (Operator == "*"):
            return First_num * Second_num
        if (Operator == "/"):
            return First_num / Second_num
    if(Operator == "+" or Operator == "-"):
        if (Operator == "+"):
            return First_num + Second_num
        if (Operator == "-"):
            return First_num - Second_num

def Operator_Priority_Check(New_Operator:str,Old_Operator:str):
    if (Old_Operator == "^"):
        return False
    if (New_Operator == "^"):
        return True
    if (Old_Operator == "*" or Old_Operator == "/"):
        return False
    if (New_Operator == "*" or New_Operator == "/"):
        return True
    if (Old_Operator == "+" or Old_Operator == "-"):
        return False
    if (New_Operator == "+" or New_Operator == "-"):
        return True
    return 

def parenthsis_handler(input_list:list):
    parenthsis_start = 0
    parenthsis_end = 0
    index = 0
    for item in input_list:
        if(item == "(" and parenthsis_end == 0):
            parenthsis_start = index
        if(item == ")" and parenthsis_end == 0):
            parenthsis_end = index
        index = index + 1
    if (parenthsis_start == parenthsis_end):
        return False
    new_list = []
    new_list.append(parenthsis_start)
    new_list.append(parenthsis_end)
    for item in range(parenthsis_start,parenthsis_end):
        if (item == parenthsis_start):
            input_list.pop(parenthsis_start)
        if (item == parenthsis_end-1):
            input_list.pop(parenthsis_start)
        else:
            new_list.append(input_list[item])
    print(new_list)
    return new_list

def number_and_operator_splitter(string:str):
    Math_function = []
    Number = ""
    string = string + "?"
    previous_char = ""
    for char in string:
        if(char == "?"):
            if (Number != ""):
                Math_function.append(Number)
        if(isNumber(char)):
            Number = Number + char
        if(isOperator(char)):
            if (Number == "" and char != ")" and char != "(" and previous_char != ")"):
                Math_function.append(0)
            else:
                if (Number != ""):
                    Math_function.append(Number)
            if (isNumber(previous_char) and char == "("):
                Math_function.append("*")
            Math_function.append(char)
            Number = ""
        previous_char = char
    print("Current Math_function:",Math_function)
    return Math_function

def func_parser(math_function:list):
    if (len(math_function) == 1):
        return math_function[0]
    Current_index = 0
    Highest_priority_operator_index = 0
    Symbol = ""
    for math_symbol in math_function:
        if(isOperator(math_symbol)):
            if (Operator_Priority_Check(math_symbol,Symbol)):
                Highest_priority_operator_index = Current_index
                print("current highest index: ",Highest_priority_operator_index)
                Symbol = math_symbol
        Current_index = Current_index + 1
    Answer = Calc(Highest_priority_operator_index,math_function)
    if (len(math_function) == 2):
        for item in range(0,2):
            math_function.pop(0)
        math_function.insert(0,Answer)
    else:
        for item in range(0,3):
            math_function.pop(Highest_priority_operator_index-1)
        math_function.insert(Highest_priority_operator_index-1,Answer)
    print(math_function)
    return func_parser(math_function)

def basic_logic(Inital_list):
    parenthsis_copy = []
    for item in Inital_list:
        parenthsis_copy.append(item)
    any_parenthsis = parenthsis_handler(parenthsis_copy)
    if (any_parenthsis == False):
        Answer = func_parser(Inital_list)
        return Answer
    else:
        index_start = any_parenthsis.pop(0)
        index_end = any_parenthsis.pop(0)
        Answer = func_parser(any_parenthsis)
        for item in range(index_start,index_end+1):
            Inital_list.pop(index_start)
        Inital_list.insert(index_start,Answer)
        print("Inital_List: ",Inital_list)
        return basic_logic(Inital_list)
    
def add_answer(answer):
    Raw_string = user_input()
    Raw_string = Raw_string.replace("ans",str(answer))
    Raw_string = Raw_string.replace(" ","")
    print("current ans:", answer, "current_string",Raw_string)
    Inital_list = number_and_operator_splitter(Raw_string)
    answer = basic_logic(Inital_list)
    print("Answer: ",answer)
    add_answer(int(answer))

add_answer(0)