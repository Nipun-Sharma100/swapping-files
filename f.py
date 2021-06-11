def swapfiles():
    filename1=input("Enter first file:  ")
    filename2=input("Enter second file:  ")

    f1=open(filename1, "r")
    data_a=f1.read()
    f2=open(filename2, "r")
    data_b=f2.read()

    with open(filename1, "w") as c:
        c.write(data_b)

    with open(filename2, "w") as d:
        d.write(data_a)

swapfiles()