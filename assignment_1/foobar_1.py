from operator import le


def solution(data, n): 
    In_data=data
    Out_data=[]
    al=int(n)
    count=1
    if len(In_data)<100:
        for j in In_data:
            count=In_data.count(int(j))
            if count<=al:
                Out_data.append(int(j))
    #print (Out_data)          
    return Out_data

