def SpecCheck(str):
    specstr = "~!@#$%^&*()_+-*/<>.[]\/"
    for n in specstr:
        if n in str:
            print("Invalid input!Contain special characters!")
        else:
            list = str.split(',')
    print(list)
    return(list)