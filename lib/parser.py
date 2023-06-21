import time

def create_stack():
    return []

def push(stack, item):
    stack.append(item)

def pop(stack):
    if not is_empty(stack):
        stack.pop()
    else:
        print("Stack is empty")

def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    else:
        print("Stack is empty")

def is_empty(stack):
    return len(stack) == 0


def validator(arr_token):
    stack = create_stack()
    i = 0
    state = ""
    
    if "error" in arr_token:
        return False
    
    state = "i"
    push(stack,'#')
    state = "S"
    push(stack,'S')
    
    symbol = arr_token[i]
    top = peek(stack)
    
    # <statement> ::= if <condition> : <action> else : <action> | if <condition> <logical_operator> <condition> : <action> else : <action>
    # <condition> ::= true | false | <variable> <comparison_operator> <variable>
    # <action> ::= <variable> = <variable> <arithmetic_operator> <variable>
    # <variable> ::= a | b | c
    # <comparison_operator> ::= == | != | <= | >= | < | > 
    # <arithmetic_operator> :== + | - | * | /
    # <logical_operator> :== and | or
    
    # <statement> A
    # <condition> B
    # <action> C
    # <variable> D
    # <comparison_operator> E
    # <arithmetic_operator> F
    # <logical_operator> G
    
    # Simbol non-terminal : <statement> , <condition> , <action>, <variable>, <comparison_operator>, <arithmetic_operator>, <logical_operator>
    # Simbol terminal : if, :, else, true, false, =, a, b, c, ==, !=, <=, >=, <, >, +, -, *, /, and, or 
            
    while top != "#":
        time.sleep(0.3)
        print("stack:",stack,"top:",top,"symbol:",symbol,"index:",i)
        if top == 'S':
            if symbol == "9" and ("11" not in arr_token and "12" not in arr_token):
                pop(stack)
                push(stack,"C")
                push(stack,"15")
                push(stack,"10")
                push(stack,"C")
                push(stack,"15")
                push(stack,"B")
                push(stack,"9")
            elif symbol == "9" and ("11" in arr_token or "12" in arr_token):
                pop(stack)
                push(stack,"C")
                push(stack,"15")
                push(stack,"10")
                push(stack,"C")
                push(stack,"15")
                push(stack,"B")
                push(stack,"G")
                push(stack,"B")
                push(stack,"9")
            else:
                return False
            
        elif top == "B":
            if symbol == "13":
                pop(stack)
                push(stack,"13")
            elif symbol == "14":
                pop(stack)
                push(stack,"14")
            elif symbol == "1":
                pop(stack)
                push(stack,"D")
                push(stack,"E")
                push(stack,"D")
            else:
                return False
            
        elif top == "C":
            if symbol == "1": #D = D f D
                pop(stack)
                push(stack,"D")
                push(stack,"F")
                push(stack,"D")
                push(stack,"8")
                push(stack,"D")
            else:
                return False
        
        elif top == "D":
            if symbol == "1":
                pop(stack)
                push(stack,"1")
            else:
                return False
        
        elif top == "E": # comparison
            if symbol == "2":
                pop(stack)
                push(stack,"2")
            elif symbol == "3":
                pop(stack)
                push(stack,"3")
            elif symbol == "4":
                pop(stack)
                push(stack,"4")
            elif symbol == "5":
                pop(stack)
                push(stack,"5")
            elif symbol == "6":
                pop(stack)
                push(stack,"6")
            elif symbol == "7":
                pop(stack)
                push(stack,"7")
            else:
                return False
        
        elif top == "F": 
            if symbol == "16":
                pop(stack)
                push(stack,"16")
            elif symbol == "17":
                pop(stack)
                push(stack,"17")
            elif symbol == "18":
                pop(stack)
                push(stack,"18")
            elif symbol == "19":
                pop(stack)
                push(stack,"19")
            else:
                return False
            
        elif top == "G":
            if symbol == "11":
                pop(stack)
                push(stack,"11")
            elif symbol == "12":
                pop(stack)
                push(stack,"12")
        
        elif top == "1":
            if symbol != "1":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]
                
        elif top == "2":
            if symbol != "2":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]
                
        elif top == "3":
            if symbol != "3":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]
                
        elif top == "4":
            if symbol != "4":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]
                
        elif top == "5":
            if symbol != "5":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]
                
        elif top == "6":
            if symbol != "6":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]
                
        elif top == "7":
            if symbol != "7":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]
                
        elif top == "8":
            if symbol != "8":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]
                
        elif top == "9":
            if symbol != "9":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]
                
        elif top == "10":
            if symbol != "10":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]

        elif top == "11":
            if symbol != "11":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]

        elif top == "12":
            if symbol != "12":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]

        elif top == "13":
            if symbol != "13":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]

        elif top == "14":
            if symbol != "14":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]

        elif top == "15":
            if symbol != "15":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]

        elif top == "16":
            if symbol != "16":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]

        elif top == "17":
            if symbol != "17":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]

        elif top == "18":
            if symbol != "18":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]

        elif top == "19":
            if symbol != "19":
                return False
            else:
                pop(stack)
                i += 1
                symbol = arr_token[i]
        
        else:
            return False
        
        top = peek(stack)
    
    top = peek(stack)
    
    if top == "#":
        if symbol != "#":
            return False
            
        else:
            return True
    else:
        return False

# def test():
#     tokens1 = ['9', '1', '4', '1', '15', '1', '8',
#               '1', '16', '1', '10', '15', '1',
#               '8', '1', '19', '1', '#']
    
#     tokens2 = ['9', '1', '4', '1', '11', '1', '7', 
#                '1', '15', '1', '8', '1', '16', '1', 
#                '10', '15', '1', '8', '1', '19', '1', '#']
    
#     validator(tokens2)