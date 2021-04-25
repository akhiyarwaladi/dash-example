# assume value is a decimal
def transform_to_rupiah_format(value):
    
    str_value = str(value)
    #print(len(str_value))
    unit = ''


    separate_decimal = str_value.split(".")
    after_decimal = separate_decimal[0]
    before_decimal = separate_decimal[1]

    reverse = after_decimal[::-1]
    temp_reverse_value = ""

    for index, val in enumerate(reverse):
        if (index + 1) % 3 == 0 and index + 1 != len(reverse):
            temp_reverse_value = temp_reverse_value + val + "."
        else:
            temp_reverse_value = temp_reverse_value + val

    temp_result = temp_reverse_value[::-1]

    if len(str_value) >= 12:
        unit = 'jt'
        show_result = temp_result.split('.')[0] + "." + temp_result.split('.')[1] 
    elif len(str_value) >= 8:
        unit = 'jt'
        show_result = temp_result.split('.')[0]
    elif len(str_value) >= 5:
        unit = 'rb'
        show_result = temp_result.split('.')[0]
        
    return "Rp " + show_result + unit

def transform_format(value):
    str_value = str(value)
    separate_decimal = str_value.split(".")
    after_decimal = separate_decimal[0]
    before_decimal = separate_decimal[1]

    reverse = after_decimal[::-1]
    temp_reverse_value = ""

    for index, val in enumerate(reverse):
        if (index + 1) % 3 == 0 and index + 1 != len(reverse):
            temp_reverse_value = temp_reverse_value + val + "."
        else:
            temp_reverse_value = temp_reverse_value + val

    temp_result = temp_reverse_value[::-1]

    #return "Rp " + temp_result + "," + before_decimal
    return temp_result