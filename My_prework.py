#Question 1: Write a function to print "hello_USERNAME!" USERNAME is the input of the function

def hello_name(user_name):
    print("\nHello " + user_name + " welcome back!")

hello_name("Dylan")

#Question 2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds(number):

    number = []
    
    for num in range(100):
            #if number isn't divisible by 2 then add that number to the list
            #then add 2, and continue
        if num % 2 !=0:
            number.append(num)
            
            num = num + 2
            continue
            #If the number IS divisible by 2, continue with list without adding
            #to the list then continue
        elif num % 2 == 0:
            continue
            #if the number is greater than or equal to 100 then stop the loop
        elif num in number >= 100:
            break
        else:
            print("invalid")
    print(number)
        
    
    
first_odds(str(1))


#Question 3: Please write a Python function, max_num_in_list to return the max number
#of a given list
def max_num_in_list(a_list):
    #a_list will equal maximum (max) value of input list
    a_list = max(a_list)
    print(a_list)
    return a_list

max_num_in_list([503, 22, 13, 56])


#Question 4: Write a function to return if the given year is a leap year
def is_leap_year(a_year):
    #Is year divisible by 4, or is it divisible by 4 but, not 100
    if ((a_year % 400 == 0) or
       (a_year % 100 != 0) and (a_year % 4 == 0)):
       print("Yes, it is a leap year")
    else:
        print("No, it is not a leap year")
    

a_year = int(input("Which year would you like to check? "))

is_leap_year(a_year)


#Question 5: Write a function to check to see if all the numbers in the liast are consecutive numbers.
def is_consecutive(a_list):
    
    min_val = min(a_list)
    max_val = max(a_list)
    #Is max value of list - minimum value of list +1 = to length? if no
    #return false
    if max_val - min_val + 1 == len(a_list):
        for n in range(len(a_list)):        
            if a_list[n]< 0:
                #If number is greater than 0 then subtract [n]-minimum value in list
                #then assign that value to v
                v = -a_list[n] - min_val
            else:
                v = a_list[n] - min_val
                #is [v] greater than 0? if yes, return true
            if a_list[v] > 0:
                #use this to take care of duplicate number being seen 
                #as consecutive, ex.[1,3,3,7]
                a_list[v] = -a_list[v]
            else:
                return False
        return True
    return False
a_list = [1,2,3,4]
print(is_consecutive(a_list))