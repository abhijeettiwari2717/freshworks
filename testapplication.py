import task_freshworks as task


def operation():
    print("Select any one of the operation to perfom:  ")
    print("1. CREATE KEY")
    print("2. UPDATE VALUE")
    print("3. READ THE KEY")
    print("4. DELETE THE KEY")
    print(" ")
    d = int(input("Enter your Choice--->   "))
    if d==1:
        print(" ")
        a = input("Enter the key Name:  ")
        b = int(input("Enter the value of the above given Key:  "))
        c = int(input("Enter the time to live for the above given key:  "))
        task.create(a,b,c)

    elif d==2:
        print(" ")
        e = (input("Enter the key to update:  "))
        h =  int(input("Enter the new value for above key:  "))
        task.update(e,h)

    elif d==3:
        print(" ")
        f = input("Enter the key you want to read:  ")
        task.read(f)

    elif d==4:
        print(" ")
        g = input("Enter the key you want to delete:  ")
        task.delete(g)

    operation()



operation()