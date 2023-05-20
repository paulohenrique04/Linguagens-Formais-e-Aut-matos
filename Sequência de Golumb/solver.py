def golumb():

    yield 1
    yield 2
    yield 2
    #use o gerador para descobrir quantas vezes o número n deve ser repetido
    gerador = golumb()
    
    next(gerador)
    next(gerador)
    
    n = 3
    a = 3
    
    for repeat in gerador:
        for i in range(repeat):
            yield a
            n += 1
            
        a += 1
        
def main():
    
    n = int(input())
    gerador = golumb()
    l = [ next(gerador) for i in range(n)]
    print(l)


if __name__ == "__main__":
    main()