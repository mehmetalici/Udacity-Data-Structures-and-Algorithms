def sort_012(input_list):
    if len(input_list) == 0:
        return []
    if not all(map(lambda elt: elt in [0, 1, 2], input_list)):
        raise Exception("List elements must be one of [0, 1, 2]")
        
    zero_idx = 0
    two_idx = len(input_list) - 1
    current_idx = 0
    while current_idx < two_idx:
        num = input_list[current_idx]
        if num == 0:
            probe = input_list[zero_idx]
            while probe == 0:
                zero_idx += 1
                probe = input_list[zero_idx]

            if current_idx > zero_idx:
                input_list[zero_idx] = num
                input_list[current_idx] = probe
            else:
                current_idx +=1

        elif num == 2:
            probe = input_list[two_idx]
            while probe == 2:
                two_idx -= 1
                probe = input_list[two_idx]
            
            if current_idx < two_idx:
                input_list[current_idx] = probe
                input_list[two_idx] = num
            else:
                current_idx += 1
        
        else:
            current_idx += 1

    return input_list

