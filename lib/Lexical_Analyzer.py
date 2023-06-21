import lib.FA as FA

def get_token(word):
    if FA.valid(word,'a') :
        return "1"
    elif FA.valid(word,'b'):
        return "1"
    elif FA.valid(word,'c'):
        return "1"
    elif FA.valid(word,'=='):
        return "2"
    elif FA.valid(word,'!='):
        return "3"
    elif FA.valid(word,'<='):
        return "4"
    elif FA.valid(word,'>='):
        return "5"
    elif FA.valid(word,'<'):
        return "6"
    elif FA.valid(word,'>'):
        return "7"
    elif FA.valid(word,'='):
        return "8"
    elif FA.valid(word,'if'):
        return "9"
    elif FA.valid(word,'else'):
        return "10"
    elif FA.valid(word,'and'):
        return "11"
    elif FA.valid(word,'or'):
        return "12"
    elif FA.valid(word,'true'):
        return "13"
    elif FA.valid(word,'false'):
        return "14"
    elif FA.valid(word,':'):
        return "15"
    elif FA.valid(word,'+'):
        return "16"
    elif FA.valid(word,'-'):
        return "17"
    elif FA.valid(word,'/'):
        return "18"
    elif FA.valid(word,'*'):
        return "19"
    else:
        return "error"

def do_la(arr_string):
    print("array str:",arr_string)
    result = []
    for word in arr_string:
        result.append(get_token(word))
        
    result.append("#")
    
    return result