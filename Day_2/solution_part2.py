def main():
    # Split the text in each configuration, compare and if equal, add to current total 
    total = 0
    invalid_set = set()
    with open("input.txt","r") as file:
        id_ranges = file.read().strip().split(",")
        for id_range in id_ranges:
            #fetch the lower and upper limits of the range
            ll = id_range.split("-")[0]
            ul = id_range.split("-")[1]
            for id in range(int(ll), int(ul)+1):
                id_str = str(id)
                # Skip processing if this id has already been marked previously
                if id_str in invalid_set:
                    total+=id
                elif isInvalidId(id_str):
                    invalid_set.add(id_str)
                    total+=id
    print(total)
def isInvalidId(id_str):
    n = len(id_str)
    # Have a split value that iterates from 1 upto n/2+1
    for split in range(1, (n//2+1)):
        isInvalid = True
        # We can skip values where it cannot be evenly split
        if n % split != 0:
            continue
        left_substring = id_str[:split]
        for i in range(split, n, split):
            # In each round, compare the previous substring with the current and ensure they are all equal
            right_substring = id_str[i:i+split]
            if left_substring != right_substring:
                isInvalid = False
            left_substring = right_substring
        if isInvalid == True:
            return isInvalid
    return False
    
if __name__ == "__main__":
    main()
