#by Mersad Akabri 2020.3.10
import sys
import colored
if sys.argv[1] == "--help":
        print("\033[1;32mWelcome to change time program , enjot it :) \n \t\033[1;39m1 - first you have to enter your time that you want to change , example : 2\n\t2 - next you have to enter type of your first time, example : d (day)\n\t3 - and finally you have to enter the type of time that you want to change your first time to it, example:h\n\t4 - you have to give args in terminal like :\n\t\t\033[1;35m python3 app1.py 2 d h\033[1;39m\n\tthis give you 2 day to hours, so the answer is 48 hours\n\n\033[1;30mYear => Y \tDay => D \tMouth => MO\nHour => H \tMinute => M \tSecond => S")
        help = 1
if help != 1:
    try:
        first = int(sys.argv[1])
        try:
            first_type = str(sys.argv[2])
            second_type = str(sys.argv[3])
        except:
            pass
        if first_type == "Y" or first_type == "y":
                #if result time was mounth :
            if second_type == 'Mo' or second_type == 'mo' or second_type == 'MO' or second_type == 'mO':
                print(f"{first} year ==> {first*12} Mounth")
            #if result time was day :
            if second_type == 'D' or second_type == 'd':
                print(f"{first} year ==> {first*360} days")
            #if result time was hour :
            if second_type == 'H' or second_type == 'h':
                print(f"{first} year ==> {first*8640} hour")
            #if result time was minute :
            if second_type == 'M' or second_type == 'm':
                print(f"{first} year ==> {first*518400} minute")
            #if result time was second :
            if second_type == 'S' or second_type == 's':
                print(f"{first} year ==> {first*311040000} second")
        #if first time was Mounth :
        elif first_type == 'm' or first_type == 'M':
            #if result time was day :
            if second_type == 'D' or second_type == 'd':
                print(f"{first} Mounth ==> {first*30} days")
            #if result time was Hour :
            if second_type == 'H' or second_type == 'h':
                print(f"{first} mounth ==> {first*720} hour")
            #if result time was minute :
            if second_type == 'M' or second_type == 'm':
                print(f"{first} mounth ==> {first*43200} minute")
            #if result time was day :
            if second_type == 'S' or second_type == 's':
                print(f"{first} mounth ==> {first*2592000} seconds")


        #if first time was Day :
        elif first_type == 'd' or first_type == 'D':
            #if result was hour :
            if second_type == 'H' or second_type == 'h':
                print(f"{first} day ==> {first*24} hour")
            #if result time was minute :
            if second_type == 'M' or second_type == 'm':
                print(f"{first} day ==> {first*1440} minute")
            #if result time was day :
            if second_type == 'S' or second_type == 's':
                print(f"{first} day ==> {first*86400} seconds")


        #if first time was Hour :
        elif first_type == 'h' or first_type == 'H':
            #if result time was minute :
            if second_type == 'M' or second_type == 'm':
                print(f"{first} hour ==> {first*60} minute")
            if second_type == 'S' or second_type == 's':
                print(f"{first} hour ==> {first*3600} seconds")

        #if first time was Minute :
        elif first_type == 'm' or first_type == 'M':
            print(f"{first} minute ==> {first*60} seconds")
        else:
            print(f"{sys.argv[1]} is not defined \ntry --help")
    except:
        print("command not found, use --help to get help")
