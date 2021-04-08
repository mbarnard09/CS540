def readable(input_list):
    str = "On {} {}, {}, {}, {} recieved {} inches of precipitation".format(input_list[6],input_list[7],input_list[5],input_list[0],input_list[1],input_list[8])
    print(str)


####testing
readable(['Asheville', 'NC', 682.1, 35.5954, -82.5568, 2010, 'Jan', 1, 4.3])
