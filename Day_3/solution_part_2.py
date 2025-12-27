def main():
    total = 0
    with open("input.txt","r") as file:
        for line in file:
            line = line.strip()
            total += find_max_joltage(line)
    print(total)

# find max joltage value for a given list of joltages
def find_max_joltage(joltages):
    max_joltage_list = [0] * 12
    n = len(joltages)
    # set highest value to the leftmost index when possible
    # reset remaining smaller digit values to zero whenever a digit is set to the left
    for index, value in enumerate(joltages):
        num = int(value)
        for i, max_joltage in enumerate(max_joltage_list):
            remaining_digits = 12 - i - 1
            if num > max_joltage and index < (n - remaining_digits):
                max_joltage_list[i] = num
                if i != 11:
                    max_joltage_list[(-remaining_digits):] = [0] * remaining_digits
                break
    return convert_digits_to_integer(max_joltage_list)

# convert a list of integers into a single integer by treating each indexed value as a digit
def convert_digits_to_integer(digits):
    value = 0
    for digit in digits:
        value = (value * 10) + digit
    return value

if __name__ == "__main__":
    main()
