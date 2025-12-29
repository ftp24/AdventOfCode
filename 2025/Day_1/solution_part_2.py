def rotate(curr_position, rotations, zero_position_count):
    if rotations[0] == 'L':
        zero_position_count, curr_position= left_rotate(curr_position, int(rotations[1:]), zero_position_count)
    elif rotations[0] == 'R':
        zero_position_count, curr_position = right_rotate(curr_position, int(rotations[1:]), zero_position_count)
    return zero_position_count, curr_position 

def left_rotate(curr_position, rotation, zero_position_count):
    if rotation < curr_position:
        curr_position -= rotation
    else:
        # Reset current position to 0 and add a count if it was not already zero
        rotation -= curr_position
        if curr_position != 0:
            zero_position_count += 1
        # Add a count for each full rotation 
        zero_position_count += rotation // 100
        rotation %= 100
        curr_position = (100 - rotation) % 100
    return zero_position_count, curr_position

def right_rotate(curr_position, rotation, zero_position_count):
    if (curr_position + rotation) < 100:
        curr_position += rotation
    else:
        # Reset current position to 0 and add a count if it was not already zero
        rotation -= ((100 - curr_position) % 100)
        if curr_position != 0:
            zero_position_count += 1
        # Add a count for each full rotation 
        zero_position_count += (rotation // 100)
        rotation %= 100
        curr_position = rotation
    return zero_position_count, curr_position

def main():
    curr_position = 50
    zero_position_count = 0
    with open("input.txt","r") as file:
        for line in file:
            zero_position_count, curr_position = rotate(curr_position, line.strip(), zero_position_count)
    print(zero_position_count) 

if __name__ == "__main__":
    main()

