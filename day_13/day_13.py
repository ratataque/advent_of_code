import json

data = open("day_13/data.txt", "r").read().split("\n\n") 
lines = [ line.split("\n") for line in data]
paquets = [[json.loads(l) for l in line] for line in lines]


right_order = []

def is__in__the_right_order(paquet_number, p1, p2):

    try:
        for left, right in zip(p1,p2, strict=True):            
            if isinstance(left, list) or isinstance(right, list):
                
                left = left if isinstance(left, list) else [left]
                right = right if isinstance(right, list) else [right]
                
                test = is__in__the_right_order(paquet_number, left, right)

                if test == None:
                    continue
                else:
                    return test

            else:
                if left < right:
                    return True
                elif left > right:
                    return False

    except:
        if len(p1) == 0 and len(p2) == 0:
            return None
        if len(p1) < len(p2):
            return True
        else:
            return False
    
    return None

if __name__ == "__main__":
    
    
    divider = [1, 1]
    for index, paquet in enumerate(paquets, start=1):
        if is__in__the_right_order(index, paquet[0], paquet[1]):
            right_order.append(index)

        for p in paquet:
            divider[0] = divider[0] + 1 if is__in__the_right_order(index, p, [[2]]) else divider[0]
            divider[1] = divider[1] + 1 if is__in__the_right_order(index, p, [[6]]) else divider[1]
        
        
print("P1: ", sum(right_order))
print("P2: ", divider[0]*(divider[1]+1))
