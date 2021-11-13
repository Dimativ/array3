def input_data_from_console(count_data):
    list_data = []
    for i in range(count_data):
        list_data += [int(input('Enter ' + str(i+1) + ' value:'))]
    return list_data