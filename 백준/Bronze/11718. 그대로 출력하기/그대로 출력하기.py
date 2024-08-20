while True:
    try:
        S = input()
        if S:
            print(S)
    except EOFError:
        break