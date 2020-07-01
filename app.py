#by Mersad Akbari at 2020.3.10

#Variables
first = int(input("What Time You Want To Change => "))
first_type = str(input("\nYear => Y \tDay => D \tMouth => MO\nHour => H \tMinute => M \tSecond => S\n\nWhat Is Type Of Your Time? Y/MO/D/H/M/S => "))
#if first time was year :
if first_type == 'y' or first_type == 'Y':
    second_type = str(input("\nDay => D \tMouth => MO\nHour => H \tMinute => M \tSecond => S\n\nWhat Is Type Of Your Time? MO/D/H/M/S => "))
    #if result time was mounth :
    if second_type == 'Mo' or second_type == 'mo' or second_type == 'MO' or second_type == 'mO':
        print(f"\n{first} year ==> {first*12} Mounth")
    #if result time was day :
    if second_type == 'D' or second_type == 'd':
        print(f"\n{first} year ==> {first*360} days")
    #if result time was hour :
    if second_type == 'H' or second_type == 'h':
        print(f"\n{first} year ==> {first*8640} hour")
    #if result time was minute :
    if second_type == 'M' or second_type == 'm':
        print(f"\n{first} year ==> {first*518400} minute")
    #if result time was second :
    if second_type == 'S' or second_type == 's':
        print(f"\n{first} year ==> {first*311040000} second")

#if first time was Mounth :
if first_type == 'm' or first_type == 'M':
    second_type = str(input("\nDay => \tD Hour => H\nMinute => M\t Second => S\n\nWhatType You Want To Your Time Be? D/H/M/S => "))
    #if result time was day :
    if second_type == 'D' or second_type == 'd':
        print(f"\n{first} Mounth ==> {first*30} days")
    #if result time was Hour :
    if second_type == 'H' or second_type == 'h':
        print(f"\n{first} mounth ==> {first*720} hour")
    #if result time was minute :
    if second_type == 'M' or second_type == 'm':
        print(f"\n{first} mounth ==> {first*43200} minute")
    #if result time was day :
    if second_type == 'S' or second_type == 's':
        print(f"\n{first} mounth ==> {first*2592000} seconds")


#if first time was Day :
if first_type == 'd' or first_type == 'D':
    second_type = str(input("\nHour => H \nMinute => M\t Second => S\n\nWhatType You Want To Your Time Be? H/M/S => "))
    #if result was hour :
    if second_type == 'H' or second_type == 'h':
        print(f"\n{first} day ==> {first*24} hour")
    #if result time was minute :
    if second_type == 'M' or second_type == 'm':
        print(f"\n{first} day ==> {first*1440} minute")
    #if result time was day :
    if second_type == 'S' or second_type == 's':
        print(f"\n{first} day ==> {first*86400} seconds")


#if first time was Hour :
if first_type == 'h' or first_type == 'H':
    second_type = str(input("\nMinute => M\t Second => S\n\nWhatType You Want To Your Time Be? M/S => "))
    #if result time was minute :
    if second_type == 'M' or second_type == 'm':
        print(f"\n{first} hour ==> {first*60} minute")
    if second_type == 'S' or second_type == 's':
        print(f"\n{first} hour ==> {first*3600} seconds")

#if first time was Minute :
if first_type == 'm' or first_type == 'M':
    print(f"\n{first} minute ==> {first*60} seconds")
