def policz_slowa(a):
    dict = {}
    a = a.lower().split()
    for i in a:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    print(dict)


policz_slowa("Python jest super, bo Python jest prosty")

