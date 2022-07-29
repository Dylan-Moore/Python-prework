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
        