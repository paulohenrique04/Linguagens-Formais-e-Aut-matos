#Código Python 
#Projete um autômato finito determinístico que aceita a linguagem L de strings formada por 0’s e 1’s definida como:
#L = {w|w tem 011 como substring}
#Por exemplo, 0111 está em L e 0010 não está em L.
edges = { # função de transição
(1, '1') : 1,
(1, '0') : 2,
(2, '0') : 3,
(2, '1') : 2,
(3, '0') : 4,
(3, '1') : 4,
(4, '0') : 2,
(4, '1') : 2
}

current = 1 # estado inicial
accepting = [2] # estados finais

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