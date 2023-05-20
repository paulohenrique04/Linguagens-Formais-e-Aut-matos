#Código Python 
#Projete um autômato finito determinístico que aceita a linguagem L de strings formada por 0’s e 1’s definida como:
#L = {w|w termina em 011}
#Por exemplo, 1011 está em L e 0110 não está em L.
# 
#   
edges = { # função de transição
(1, '0') : 1,
(1, '1') : 2,
(2, '1') : 3,
(2, '0') : 1,
(3, '0') : 1      
}

current = 1 # estado inicial
accepting = [3] # estados finais

# Função que roda o autômato
def dfa(string, current, edges, accepting):
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        remainder = string[1:]
        if (current, letter) in edges:
            newstate = edges[(current, letter)]
            return dfa(remainder, newstate, edges, accepting)
        return False


string = input()
print (dfa(string, current, edges, accepting))