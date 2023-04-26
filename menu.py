import os

ans = True
while ans:
    print ("""
    ZarGate switch config tool!

    1. Config QUANTA edge switch
    2. Config QUANTA core switch
    3. Config DELL subcore switch
    4. Config HP common switch
    9. Exit/Quit
    """)
    ans = raw_input("What would you like to do? ")
    if ans == "1":
        os.system('edgeconfig.py')
    elif ans == "2":
        os.system('coreconfig.py')
    elif ans == "3":
        os.system('dellconfig.py')
    elif ans == "4":
        os.system('hpcommonconfig.py')
    elif ans == "9":
        print("\n Goodbye")
        exit()
    elif ans != "":
        print("\n Invalid choice. Try again.")
