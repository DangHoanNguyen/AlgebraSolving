import arrange

def Gauss(array):
    c_array = array
    res_arr = []
    j=0

    while len(res_arr) <= len(array) and j < len(array[0]):
        temp_arr = []
        for line in c_array:
            if line[j] == 0:
                break
            else:
                temp_arr.append(line)
        if len(temp_arr) <= 1:
            if len(temp_arr) == 1:
                res_arr.append(temp_arr[0])
                c_array.remove(temp_arr[0])
            j=j+1
            continue
        for line in temp_arr:
            c_array.remove(line)
        
        res_arr.append(temp_arr[0])
        
        for i in range(1,len(temp_arr)):
            
            n = temp_arr[0][j]/(temp_arr[i][j])
            array_to_append = []
            for index in range(j):
                array_to_append.append(0)
            for m in range(j, len(temp_arr[i])):
                x = temp_arr[0][m] - temp_arr[i][m]*n
                array_to_append.append(x)
            res_arr.append(array_to_append)
        if len(c_array) > 1:
            arrange.arange(c_array)

        j = j+1
    res_arr += c_array
    
    return res_arr

