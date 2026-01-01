def main():
    paper_rolls = parse_input("input.txt")
    accessible_roll_count = count_accessible_rows(paper_rolls)

def count_accessible_rows(paper_rolls):
    total_count = 0
    visited_cells = set()
    # First check corner cells for '@'
    total_count = check_corner_cells(paper_rolls, total_count, visited_cells)
    # Repeat entire process untill total count no longer increases
    while True:
        prev_total_count = total_count
        # Loop through each cell to find a '.'. From there check its surrounding cells
        for i, row in enumerate(paper_rolls):
            for j, cell in enumerate(row):
                if cell == '.' and ((i, j) not in visited_cells):
                    total_count = check_surrounding_cells(i, j, paper_rolls, total_count, visited_cells)
                    visited_cells.add((i, j))
                elif cell == '@':
                    continue
        # Clear the visited cells in each run so as to recheck the cells in the next round
        visited_cells.clear()
        if total_count == prev_total_count:
            break
    # print_grid(paper_rolls)
    print(total_count)

# Check the 8 surrounding cells of a '.' cell, if they are accessible cells or not
def check_surrounding_cells(i, j, paper_rolls, total_count, visited_cells):
    # Need to check all surrounding cells of the . to cover all the @ cells
    total_count = check_current_cell(i+1, j, paper_rolls, total_count, visited_cells)
    total_count = check_current_cell(i+1, j+1, paper_rolls, total_count, visited_cells)
    total_count = check_current_cell(i+1, j-1, paper_rolls, total_count, visited_cells)
    total_count = check_current_cell(i-1, j, paper_rolls, total_count, visited_cells)
    total_count = check_current_cell(i-1, j+1, paper_rolls, total_count, visited_cells)
    total_count = check_current_cell(i-1, j-1, paper_rolls, total_count, visited_cells)
    total_count = check_current_cell(i, j+1, paper_rolls, total_count, visited_cells)
    total_count = check_current_cell(i, j-1, paper_rolls, total_count, visited_cells)
    return total_count


# Check if the current cell is accessible by checking surrounding cells for '.' or empty cells
def check_current_cell(i, j, paper_rolls, total_count, visited_cells):
    max_i = len(paper_rolls) - 1
    max_j = len(paper_rolls[0]) - 1
    curr_cell_count = 0

    # We have to check the surrounding 8 cells for '.'
    # Skip already checked cells

    if ((i, j) in visited_cells or i < 0 or j < 0 or i > max_i or j> max_j or paper_rolls[i][j] == '.'):
        return total_count

    # Add 3 count if it is a border cell
    elif i == 0 or i == max_i or j == 0 or j == max_j:
        curr_cell_count += 3

    # Check surrounding 8 cells, if not empty
    if j!= 0:
        if paper_rolls[i][j-1] == '.':
            curr_cell_count += 1
        if i!= max_i:
            if paper_rolls[i+1][j-1] == '.':
                curr_cell_count += 1

    if i!= 0:
        if paper_rolls[i-1][j] == '.':
            curr_cell_count += 1
        if j!= max_j:
            if paper_rolls[i-1][j+1] == '.':
                curr_cell_count += 1

    if i!= 0 and j != 0:
        if paper_rolls[i-1][j-1] == '.':
            curr_cell_count += 1

    if i != max_i and j != max_j:
        if paper_rolls[i+1][j+1] == '.':
            curr_cell_count += 1

    if i != max_i:
        if paper_rolls[i+1][j] == '.':
            curr_cell_count += 1

    if j != max_j:
        if paper_rolls[i][j+1] == '.':
            curr_cell_count += 1

    # if current cell is surrounded by 5 or more '.' or empty spaces, it is accessible
    if curr_cell_count > 4:
        total_count = set_accessible_cell(i, j, paper_rolls, total_count, visited_cells)

    visited_cells.add((i, j))
    return total_count

# Check if corner cells are '@' as they are accessible by default
def check_corner_cells(paper_rolls, total_count, visited_cells):
    max_i = len(paper_rolls) - 1
    max_j = len(paper_rolls[0]) - 1

    if paper_rolls[0][0] == '@':
        total_count = set_accessible_cell(0, 0, paper_rolls, total_count, visited_cells)
    if paper_rolls[0][max_j] == '@':
        total_count = set_accessible_cell(0, max_j, paper_rolls, total_count, visited_cells)
    if paper_rolls[max_i][0] == '@':
        total_count = set_accessible_cell(max_i, 0, paper_rolls, total_count, visited_cells)
    if paper_rolls[max_i][max_j] == '@':
        total_count = set_accessible_cell(max_i, max_j, paper_rolls, total_count, visited_cells)
    return total_count

# Increase the total count and mark the cell as visited
def set_accessible_cell(i, j, paper_rolls, total_count, visited_cells):
    if (i, j) not in visited_cells:
        visited_cells.add((i, j))
        paper_rolls[i][j] = '.'
        total_count += 1
    return total_count

def parse_input(input_file):
    result = []
    with open(input_file, "r") as file:
        for index, line in enumerate(file):
            line = line.strip()
            result.append(list(line))
    return result

# Helper function to print the grid neatly in a grid format
def print_grid(input):
    for row in input:
        print(" ".join(row))


if __name__ == "__main__":
    main()
