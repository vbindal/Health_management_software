
#exercise 5:

# Health management system


def getdate():
    import datetime
    return datetime.datetime.now()
def log(k):
    if k==1:
        c= int(input("Enter 1 for exercise and 2 for food:"))
        if c==1:
            value= input("Type here:")
            with open("harry-ex.txt","a") as txt:
                txt.write(str([getdate()])+":"+value+"\n")
                print("Successfully written")
        if c==2:
            value= (input("Type here:"))
            with open("harry-fd.txt","a") as txt:
                txt.write(str([getdate()])+":"+value+"\n")
                print("Successfully written")
    elif k==2:
        l = int(input("Enter 1 for exercise and 2 for food:"))
        if l == 1:
            value = input("Type here:")
            with open("hammad-ex.txt", "a") as txt:
                txt.write(str([getdate()])+":"+value+"\n")
                print("Successfully written")
        if l == 2:
            value = input("Type here:")
            with open("hammad-fd.txt", "a") as txt:
                txt.write(str([getdate()])+":"+value+"\n")
                print("Successfully written")
    elif k==3:
        m = int(input("Enter 1 for exercise and 2 for food:"))
        if m == 1:
            value = input("Type here:")
            with open("Rohan-ex.txt", "a") as txt:
                txt.write(str([getdate()])+":"+value+"\n")
                print("Successfully written")
        if m == 2:
            value = input("Type here:")
            with open("Rohan-fd.txt", "a") as txt:
                txt.write(str([getdate()])+":"+value+"\n")
                print("Successfully written")
    else:
        print("please enter a valid input for harry,hammad and rohan")
def retrieve(k):
    if k==1:
        c= int(input("Enter 1 for exercise and 2 for food:"))
        if c==1:
            with open("harry-ex.txt") as txt:
                for i in op:
                    print(i,end="")
        if c==2:
            with open("harry-fd.txt") as txt:
                for i in op:
                    print(i,end="")

    if k==2:
        l= int(input("Enter 1 for exercise and 2 for food:"))
        if l==1:
            with open("hammad-ex.txt") as txt:
                for i in op:
                    print(i,end="")
        if l==2:
            with open("hammad-fd.txt") as txt:
                for i in op:
                    print(i,end="")
    if k==3:
        m= int(input("Enter 1 for exercise and 2 for food:"))
        if m==1:
            with open("Rohan-ex.txt") as txt:
                for i in op:
                    print(i,end="")
        if m==2:
            with open("Rohan-fd.txt") as txt:
                for i in op:
                    print(i,end="")
ab= print("[HEALTH MANAGEMENT SYSTEM]")
a= int(input("Enter 1,2,3 for harry , hammad and rohan:"))
b= int(input("Press 1 to log the data and 2 for retrieve data:"))
if b==1:
    log(a)
else:
    retrieve(a)

