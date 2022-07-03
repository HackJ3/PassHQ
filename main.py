from random import *

passwordmanlist = [""]


def welban():
    print(
        """
    Welcome To PassHQ
PassHQ Is Determined To Make
Managing Your Passwords Easier
By Creating State Of The Art
Software For Your Inner Lazy!
To Begin Follow The Prompts Below!
    """
    )

welban()    
    

def PassGen():
    global choice
    if choice == 1:
        import random

        print("PassGene")

        name = input("Hey, Let Me Have Your Name Real Quick")

        chars = "fefhesfheusuugg83435gn458b@*^&^6583489573()!#$^FEFE"

        number = input(
            f"Hey {name}, Whats The Amount Of Passwords To Generate : "
        )
        number = int(number)

        length = input(
            f"How Many Characters To Use For Your Password Length {name}?"
        )
        length = int(length)

        print("\nHere Are Your Password(s):")

        for pwd in range(number):
            passwords = ""
            for c in range(length):
                passwords += random.choice(chars)
            print(passwords)

        again = input(f"Do You Want To CONTINUE For More Passwords {name} ?")

        if again == "Yes":
            print("PassGene")

            chars = "fefhesfheusuugg83435gn458b@*^&^6583489573()!#$^FEFE"

            number = input(
                f"Hey {name}, Whats The Amount Of Passwords To Generate : "
            )
            number = int(number)

            length = input(
                f"How Many Characters To Use For Your Password Length {name}?"
            )
            length = int(length)

            print("\nHere Are Your Password(s):")

            for pwd in range(number):
                passwords = ""
                for c in range(length):
                    passwords += random.choice(chars)
                print(passwords)

            again = input(f"Do You Want To CONTINUE For More Passwords {name} ?")
        else:
            print("Goodbye!!!")


def PassMan():
    global choice
    if choice == 2:
        with open("pass0.txt", "r") as f:
            passwordmanlist = [line.strip() for line in f]
        print(passwordmanlist)
        choiceman = input("Do You Want To ADD Or DELETE(COMING SOON)?")
        if choiceman == "Add" or "add":
            passwordman = input("What Is The Password You Are Meaning To Manage?")
            passwordmanlist.append(passwordman)
            print(f"{passwordman} Was Added To Your List Of Passwords")
            print(passwordmanlist)
            with open(r"pass0.txt", "w") as fp:
                fp.write("\n".join(str(item) for item in passwordmanlist))



print("Choose The Following : (1)Password Generator (2)Password Manager")
choice = int(input(""))

PassGen()

PassMan()

while True:
    print("Choose The Following : (1)Password Generator (2)Password Manager")
    choice = int(input(""))
    PassGen()
    PassMan()
