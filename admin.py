import os

action = input("What do you want to do ?\n 0: Reset all process\n 1: Launch the subscribe phase\n 2: Run the generate algorithm, and open the decode phase\n-> ")

if action == "0":
    try:
        os.remove("result.txt")
    except:
        pass

    try:
        os.remove("public_keys.txt")
    except:
        pass

    f = open("phase", "w+")
    f.write("none")
    f.close()
elif action == "1":
    f = open("phase", "w+")
    f.write("subscribe")
    f.close()
    print("Subscribe phase successfully launched!")
elif action == "2":
    import generate
    f = open("phase", "w+")
    f.write("decode")
    f.close()
    print("Done!")
else:
    print("Please enter the right number")
