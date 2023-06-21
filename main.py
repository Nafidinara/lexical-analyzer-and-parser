import re
import lib.Lexical_Analyzer as LA
import lib.parser as parser

def splitter(sentence):
    pattern = r'(\w+|[<>=+*/-]+|:)'

    result = re.findall(pattern, sentence)
    return result

def read_file(filename):
    with open(filename, 'r') as f:
        contents = f.read()
    return contents

if __name__ == '__main__':
    sentence = read_file(input("input nama file: "))
    
    # print(splitter(sentence))

    tokens = LA.do_la(splitter(sentence))
    print("array token:",tokens)
    
    print("=> Melakukan parsing:")
    result = parser.validator(tokens)
    print("")
    print("[+]",end=" ")
    print("Inputan bernilai VALID") if result == True else print("Inputan bernilai INVALID")