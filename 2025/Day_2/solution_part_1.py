def main():
    #Split the text in two, compare and if equal, add to current total 
    total = 0
    with open("input.txt","r") as file:
        id_ranges = file.read().strip().split(",")
        for id_range in id_ranges:
            #fetch the lower and upper limits of the range
            ll = id_range.split("-")[0]
            ul = id_range.split("-")[1]
            #since odd number of digits cannot be split, we can skip them
            if(isOddNumberOfDigits(ll) and isOddNumberOfDigits(ul)):
                continue
            for id in range(int(ll), int(ul)+1):
                id_str = str(id)
                if(isOddNumberOfDigits(id_str)):
                    continue
                if(isInvalidId(id_str)):
                    total+=id
    print(total)

def isOddNumberOfDigits(id):
    if(len(id)%2 == 1):
        return True
    else:
        return False

def isInvalidId(id_str):
    n = len(id_str)
    left_half = id_str[:(n//2)]
    right_half = id_str[(n//2):]
    if(left_half == right_half):
        return True
    else:
        return False 
    
if __name__ == "__main__":
    main()
