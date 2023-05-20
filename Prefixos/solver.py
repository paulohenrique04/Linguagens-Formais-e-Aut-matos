def prefixo(x, y):
    ## Coloque seu código aqui
    if x == "":
        return True
        
    if x != "" and y == "":
        return False
        
    if x[0] == y[0]:
        return prefixo(x[1:], y[1:])
        
    else:
        return False

def main():
    x = input()
    y = input()
    print( prefixo(x,y) )


if __name__ == "__main__":
    main()