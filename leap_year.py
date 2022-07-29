def is_leap_year(a_year):
    #Is year divisible by 4, or is it divisible by 4 but, not 100
    if ((a_year % 400 == 0) or
       (a_year % 100 != 0) and (a_year % 4 == 0)):
       print("Yes, it is a leap year")
    else:
        print("No, it is not a leap year")
    

a_year = int(input("Which year would you like to check? "))

is_leap_year(a_year)
