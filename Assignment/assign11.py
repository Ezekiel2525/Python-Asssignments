import time
phone = input("Enter *312# to access options: ").strip()
if phone == "*312#":
    time.sleep(1)
    print("""To Perform\n
             1. Buy Data Plan\n
             2. Match Day Special Offer\n
             3. Gift Data Plan\n
             4. Share Data Plan\n
             5. Check Data Balance\n
             6. Manage Data Plan""")
    choice = (input("Enter your choice: ")).strip()
    if choice == "1":
        time.sleep(1)
        print("""
                1. Buy Daily Data Plan\n
                2. Buy Weekly Data Plan\n
                3. Buy Monthly Data Plan""")
        options = (input("Enter your data plan: ")).strip()
        if options == "1":
            time.sleep(1)
            print(""" 
                      1. #50 for 40MB
                      2. #100 for 100MB 
                      3. #500 for 2GB""")
            opt_1 = input("Enter your option: ").strip()
            if opt_1 == "1":
                time.sleep(2)
                print("You have successfully bought a Daily Data-Plan of 40MB  for #50 😁")
            elif opt_1 == "2":
                time.sleep(2)
                print("You have successfully bought a Daily Data-Plan of 100MB for #100 😁")
            elif opt_1 == "3":
                time.sleep(2)
                print("You have successfully bought a Daily Data-Plan of 2GB for #500 😁")
            else:
                print("Invalid Code😡!!!")
        elif options == "2":
            time.sleep(2)
            print("""
                    1. #500 for 750MB (14 days)
                    2. #1000 for 2GB  
                    3. #2000 for 10GB""")
            opt_2 = input("Enter your option: ")
            if opt_2 == "1":
                time.sleep(2)
                print("You have successfully bought a Weekly Data-Plan of 750MB (14 days) for #500 😁")
            elif opt_2 == "2":
                time.sleep(2)
                print("You have successfully bought a Weekly Data-Plan of 2GB for #1000 😁")
            elif opt_2 == "3":
                time.sleep(2)
                print("You have successfully bought a Weekly Data-Plan of 2GB for #1000 😁")
            else:
                print("Invalid Code😡!!!")
        elif options == "3":
            time.sleep(2)
            print("""
                     1. #1000 for 1GB
                     2. #2000 for 2.5GB
                     3. #5000 for 10GB """)
            opt_3 = input("Enter your option: ")
            if opt_3 == "1":
                time.sleep(2)
                print("You have successfully bought a Monthly Data-Plan of #1000 for 1GB😁")
            elif opt_3 == "2":
                time.sleep(2)
                print("You have successfully bought a Monthly Data-Plan of #2000 for 2.5GB😁")
            elif opt_3 == "3":
                time.sleep(2)
                print("You have successfully bought a Monthly Data-Plan of #5000 for 10GB 😁")
            else:
                print("Invalid Code😡!!!")
        else:
            print("Unable to perform operation😣!!!")
    else:
        print("Unable to Connect😣!!!")

else:
    print("Connection for MMMI code failed😥!!!")