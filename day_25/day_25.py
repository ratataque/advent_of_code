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
    # inverse_snafu(sum,0,snafu_num)

def inverse_snafu(number: int, base: int, snafu_num: str):
    if number == 0:
        return snafu_num
    for n in range(number):
        diff = somme_power(n)
        if number > base:
            number = number-base
            if (number-diff) <= 5**n <= (number+diff): 
                p = 5**n 
                snafu_num += "1"
                break
                
            if (number-diff) <= 2*(5**n) <= (number+diff): 
                p = 2*(5**n)
                snafu_num += "2"
                break
        else: 
            number = abs(number-base)
            if (number-diff) <= 5**n <= (number+diff): 
                p = -5**n 
                snafu_num += "-"
                break
                
            if (number-diff) <= 2*(5**n) <= (number+diff): 
                p = -2*(5**n)
                snafu_num += "="
                break
    
    snafu_num = inverse_snafu(number, p,snafu_num)
    return snafu_num
        
    print(snafu_num)                
    
    
def somme_power(n):
    total = 0
    for i in range(n):
        total += 2*(5**i)
    
    return total
if __name__ == "__main__":
    part_1(data, dico)

    snafu_num = ""
    print(inverse_snafu(906,0,snafu_num))
