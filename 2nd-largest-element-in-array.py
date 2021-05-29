def second_max(arr):
    #if length is 1
    if(len(arr)==1):
        return "No 2nd maximum"
        
    max1=arr[0] #maximum in array
    max2=arr[1] #2nd maximun in array
    if(max2>max1):
        max1,max2=max2,max1
        
    if(len(arr)==2 and max1==max2):
        return "No 2nd maximum"
    
    for i in range(2,len(arr)):
        if(arr[i]>max1):
            max2=max1
            max1=arr[i]
        elif(arr[i]>max2 and arr[i]!=max1):
            max2=arr[i]
            
    if(max1!=max2):
        return max2
    else:
        return "No 2nd maximum"
            
        
#space separated integers as input
arr=list(map(int,input().split(" ")))
print(second_max(arr))

