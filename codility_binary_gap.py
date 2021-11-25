while True:
    max_gap = 0
    counter = 0
    N = int(input('Input number:'))
    n = str(bin(N))[2:]
    print(n)
    for i in n:
        if i == '0':
            counter = counter + 1
        #print(counter)
        elif i == '1':
            if counter > max_gap:
                max_gap = counter
                counter = 0
    print(max_gap)
