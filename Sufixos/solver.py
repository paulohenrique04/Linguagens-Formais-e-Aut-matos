def sufixos(x):
    if x == "":
        return [""]
    
    sufix = sufixos(x[1:]) 
    sufix.insert(0, x)
    
    return sufix
        
        
def main():
    x = input()
    
    print( sufixos(x) )


if __name__ == "__main__":
    main()
    