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