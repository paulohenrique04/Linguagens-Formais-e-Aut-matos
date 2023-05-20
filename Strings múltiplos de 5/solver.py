#Projete um autômato finito determinístico que aceita a linguagem L das strings binárias que começam com 1 e que, quando interpretadas como números são múltiplos de 5. 
#Por exemplo, 101, 1010, 1111 estão na linguagem; 100 e 111 não estão em L.

edges = { # função de transição
(1, '0') : 'dead',
(1, '1') : 2,
(2, '0') : 3,
(2, '1') : 4,
(3, '0') : 3,
(3, '1') : 6,
(4, '0') : 4,
(4, '1') : 5,
(5, '1') : 4,
(5, '0') : 5,
(6, '0') : 6,
(6, '1') : 2,
('dead', '0') : 'dead',
('dead', '1') : 'dead'
}

current = 1 # estado inicial
accepting = [5, 6] # estados finais

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