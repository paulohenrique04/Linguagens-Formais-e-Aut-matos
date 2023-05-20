# Strings binárias que começam ou terminam com 01
edges = { (0, '') :  [1,5],
          (1, '1') : [2],
          (2, '0') : [2,13],
          (2, '1') : [3],
          (3, '0') : [4],
          (3, '1') : [4],
          (4, '0') : [4],
          (4, '1') : [4],      
          (5, '0') : [6],
          (6, '0') : [12],
          (6, '1') : [7],
          (7, '0') : [9],
          (7, '1') : [8],
          (8, '0') : [8],
          (8, '1') : [8],
          (9, '0') : [10],
          (9, '1') : [9],
          (10, '0'): [11],
          (10, '1'): [11],
          (11, '0'): [11],
          (11, '1'): [11],
          (13, '0'): [13,14],
          (14, '1'): [4]

 }
initial   = 0
accepting = [2,4,9,11,12] 

def epsilon_nfa(string, current, edges, accepting): 
    #print ("current: " + str(current) + "string: " + string )    
    if string == "":
        return  current in accepting       
    else:
        if (current, '') in edges:
          for next in edges[(current,'')]:
            if epsilon_nfa(string, next, edges, accepting):
                    return True
        c = string[0]
        if (current,c) in edges:
            for next in edges[(current,c)]:
                if epsilon_nfa(string[1:], next, edges, accepting):
                    return True
        
        return False
        

string = input()
print (epsilon_nfa( string , initial, edges, accepting) )  