def congratulations(manager, tester, *developers):
    print("Happy New Year! Take care of yourself and your loved ones!\nFor:")
    print(manager + "\n" + tester)
    for x in tuple(developers):
        print(x)