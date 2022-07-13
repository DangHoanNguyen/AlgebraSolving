import math

# Matrix chuyen vao la matrix bo xung - bao gom he so tu do 
def arange(array): 
    clone_array = array
    res_arr = []
    
    j = 0

    while len(res_arr) <= len(array) and j < len(array[0]):
        # List cac phuong trinh co cung so he so
        temp_array = []
        for line in clone_array:
            
            if line[j] == 0:
                break
            else:
                temp_array.append(line)
           
        for line in temp_array:
            clone_array.remove(line)
        
        while len(temp_array) != 0:  
            array_to_append = []  
            max = -math.inf
            for line in temp_array:
                if line[j] >= max:
                    max = line[j]
                    array_to_append = line
            res_arr.append(array_to_append)
            temp_array.remove(array_to_append)
        
        j = j + 1

    res_arr += clone_array

    return res_arr
        
            