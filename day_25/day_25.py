data = open("day_25/data.txt", "r").read().split("\n")
dico = {"2": 2, "1": 1, "0": 0,"-": -1, "=": -2}

def part_1(data: list, dico: dict):
    sum = 0
    for number in data:
        num = 0
        for i in range(len(number)-1, -1, -1):
            num += dico[number[len(number)-1-i]]*(5**i)
        # print(number, num)    
        sum += num
    
    print(sum)
    snafu_num = ""
    snafu_num = inverse_snafu(sum,0,snafu_num, 0)
    return snafu_num

def inverse_snafu(number: int, base: int, snafu_num: str, prime_n: int):
    if base == number:
        if prime_n == 1:
            snafu_num += "0"
            return snafu_num
        else:
            return snafu_num
    
    for n in range(number):
        diff = somme_power(n)
        if number > base:
            if (abs(number-base)-diff) <= 5**n <= (abs(number-base)+diff): 
                snafu_num += "0"*(prime_n-n-1)    
                p = base + 5**n 
                snafu_num += "1"
                break
                
            if (abs(number-base)-diff) <= 2*(5**n) <= (abs(number-base)+diff): 
                snafu_num += "0"*(prime_n-n-1)    
                p = base + 2*(5**n)
                snafu_num += "2"
                break
        else: 
            if (abs(number-base)-diff) <= 5**n <= (abs(number-base)+diff): 
                snafu_num += "0"*(prime_n-n-1)    
                p = base-5**n
                snafu_num += "-"
                break
                
            if (abs(number-base)-diff) <= 2*(5**n) <= (abs(number-base)+diff): 
                snafu_num += "0"*(prime_n-n-1)
                p = base-2*(5**n)
                snafu_num += "="
                break
    
    snafu_num = inverse_snafu(number=number, base=p,snafu_num=snafu_num, prime_n=n)
    
    return snafu_num
        
    
def somme_power(n):
    total = 0
    for i in range(n):
        total += 2*(5**i)
    
    return total


if __name__ == "__main__":
    p1 = part_1(data, dico)

    # snafu_num = ""
    # print(inverse_snafu(20,0,snafu_num,0))

    print("Part 1: ", p1)