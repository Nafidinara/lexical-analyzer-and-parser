def valid(input_string,string_rules):
    current_state = "q0"

    transition = {}

    # buat state diagram
    for x in range(0,len(string_rules)):
        transition[f"q{x}"] = {
                string_rules[x]: f"q{x+1}",
                "eos": "error"
            }
        
    # tambah accept state
    transition[f"q{len(string_rules)}"] = {
            f"q{len(string_rules)}": f"q{len(string_rules)}",
            "eos": "accept"
        }
    
    # tambah error exception state 
    transition["qerror"] = {
            "qerror": "qerror",
            "eos": "error"
        }
    
    # print(transition,"\n")
    for char in input_string:
        if char in transition[current_state]:
            # print(current_state,end=" => ")
            current_state = transition[current_state][char]
        else:
            current_state = transition["qerror"]["qerror"]

    # print(current_state)
    return transition[current_state]["eos"] == "accept"
