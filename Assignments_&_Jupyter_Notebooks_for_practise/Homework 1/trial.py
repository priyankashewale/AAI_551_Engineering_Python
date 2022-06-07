def samesign(a,b):
    if a/abs(a) == b/abs(b):
        return True
    else:
        return False
def countSeq(arr):
    l= len(arr);
    if (l < 2):
        return(0);


    s = 0;
    e = 1;
    sign = arr[e] - arr[s];
    count = 0;

    while (e < l):
        while(e < l & arr[e] - arr[e-1] != 0 & samesign(arr[e] - arr[e-1], sign)):
            sign = -1 * sign;
            e = e +1;
  
  
    size = e - s;
    count = count + (size * (size - 1)/2); 
    s = e - 1;
    e = s + 1;

    return(count);

arr = [1,2,1,2,1]; 
#print("Hello");
countSeq(arr);
