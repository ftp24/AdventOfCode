def main():
    total = 0
    with open("input.txt","r") as file:
        for line in file:
            line = line.strip()
            total += find_max_joltage(line)
    print(total) 

def find_max_joltage(joltages):
    left_max = 0
    right_max = 0
    n = len(joltages)
    for index, value in enumerate(joltages):
        # left_max should get the highest priority (higher digit)
        # right_max has priority only for the last value
        # until then second highest can be assigned to right_max
        num = int(value)
        if num > left_max and index < (n-1):
            left_max = num
            # reset right_max value to maintain order
            right_max = 0
        elif num > right_max:
            right_max = num
    joltage_value = (left_max * 10) + right_max
    return joltage_value

if __name__ == "__main__":
    main()

