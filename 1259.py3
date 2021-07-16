while True :
    n = list(input())
    
    if n == ['0'] : break

    n_reverse = list(reversed(n))
    if n == n_reverse : print("yes")
    else : print("no")