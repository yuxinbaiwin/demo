for i in range(1,10):
    for j in range(1, i):
        print(end='       ')
    for q in range(i,10):
        print("{}*{}={:2} ".format(i,q,i*q),end='')
    print()
