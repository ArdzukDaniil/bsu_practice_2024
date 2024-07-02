while (n := input()):
    if not n.endswith('@@@'):
        if n.startswith('##'):
            print(n[2:])
        else:
            print(n)