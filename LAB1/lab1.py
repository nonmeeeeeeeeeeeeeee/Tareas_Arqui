line = "45.5;-5.353"

def line_to_list(line):
    line = line.split(";", -1)
    for x in range(len(line)):
        line[x] = line[x].split(".", -1)
        if "-" in line[x][0]:
            left, right = line[x][0][:1], line[x][0][1:]
            line[x] = left, right, line[x][1]
        else:
            line[x] = "+", line[x][0], line[x][1]
    return line

def decimal_to_binary(lst):
    integer_part = int(lst[1])
    decimal_part = float(("0." + lst[2]))
    binNum = []
    if integer_part or decimal_part:
        integer_part = integer_part_to_bin(integer_part)
        integer_part.pop(0)
        decimal_part = decimal_part_to_bin(decimal_part, 23-len(integer_part))
        exp = exponent(len(integer_part))

        binNum = exp + integer_part + decimal_part
        if lst[0] == "-":
            binNum.insert(0, 1)
        else:
            binNum.insert(0, 0)
    else:
        if lst[0] == "-":
            binNum.insert(0, 1)
        else:
            binNum.insert(0, 0)
        binNum += [0,0,0,0,0,0,0,0] + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    return binNum

def exponent(num):

    exp = integer_part_to_bin(127 + num)
    while len(exp) < 8:
        exp.insert(0,0)

    return exp

def integer_part_to_bin(num):
    lst = []
    while num:
        lst.insert(0, num%2)
        num = num // 2
    return lst

def decimal_part_to_bin(num, maxlen):
    lst = []
    
    while len(lst) < maxlen: 
        if num:
            result = num * 2
            if result >= 1:
                lst.append(1)
                num = result - 1
            else:
                lst.append(0)
                num = result
        else:
            lst.append(0)
    return lst

def sum_bin(bin1, bin2):

    exp1 = bin1[1:9]
    exp2 = bin2[1:9]
    mant1 = bin1[9:]
    mant2 = bin2[9:]







print(len(decimal_to_binary(('+', '54', '25'))))