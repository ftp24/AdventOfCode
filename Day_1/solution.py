def rotate(curr_position, input, zero_position_count):
    if input[0] == 'L' :
        return leftRotate(curr_position, int(input[1:]), zero_position_count)
    elif input[0] == 'R':
        return rightRotate(curr_position, int(input[1:]), zero_position_count)


def leftRotate(curr_position, input, zero_position_count):
    if(input < curr_position):
        curr_position -= input
    elif(input >= curr_position):
        # Reset the current position to 0 by subtracting the current position
        input -= curr_position
        # Set the position to the remaining rotation value
        curr_position = (100 - (input % 100))%100
    if(curr_position) == 0:
        zero_position_count+=1
    return zero_position_count, curr_position

def rightRotate(curr_position, input, zero_position_count):
    if(curr_position + input < 100):
        curr_position=curr_position + input
    elif((curr_position + input) >= 100):
        # Reset the current position to 0 (100) by subtracting the current position
        input -= (100-curr_position)
        # Set the position to the remaining rotation value
        curr_position = input % 100
    if(curr_position) == 0:
        zero_position_count+=1
    return zero_position_count, curr_position


def main():
    curr_position = 50
    zero_position_count=0
    with open("input.txt","r") as file:
        for line in file:
            zero_position_count, curr_position = rotate(curr_position, line.strip(), zero_position_count)
    print(zero_position_count)



if __name__ == "__main__":
    main()



