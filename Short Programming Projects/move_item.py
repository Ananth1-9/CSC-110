def move_item(swap_list, index, direction):
    if index < 0 or index >= len(swap_list):
        return 'Error: Index out of range' 
    item_to_move = swap_list[index]

    if direction == "left":
        destination_index = index - 1
        while destination_index >= 0 and swap_list[destination_index] == 0:
            destination_index -= 1

        if destination_index < 0:
            destination_index = 0

        swap_list[index] = 0
        swap_list[destination_index] = item_to_move

    elif direction == "right":
        destination_index = index + 1
        while destination_index < len(swap_list) and swap_list[destination_index] == 0:
            destination_index += 1

        if destination_index >= len(swap_list):
            destination_index = len(swap_list) - 1

        swap_list[index] = 0
        swap_list[destination_index] = item_to_move

    return swap_list
