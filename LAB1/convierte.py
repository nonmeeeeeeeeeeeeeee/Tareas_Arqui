def line_to_list(line):
    '''
    ***
    *  line  : str
    ***
    Convierte un string en una lista de elementos separados por punto y coma (";"), dividiendo cada elemento en signo, parte entera y parte decimal.
    '''
    line = line.split(";", -1)
    for x in range(len(line)):
        line[x] = line[x].split(".", -1)
        if "-" in line[x][0]:
            left, right = line[x][0][:1], line[x][0][1:]
            line[x] = left, right, line[x][1]
        else:
            line[x] = "+", line[x][0], line[x][1]
    return line

def integer_part_to_bin(num):
    '''
    ***
    *  num  : int
    ***
    Convierte la parte entera de un número en su representación binaria.
    '''
    lst = []
    while num:
        lst.insert(0, num%2)
        num = num // 2
    return lst

def exponent(num):
    '''
    ***
    *  num  : int
    ***
    Calcula el exponente en notación binaria IEEE 754 de 8 bits.
    '''
    exp = integer_part_to_bin(127 + num)
    while len(exp) < 8:
        exp.insert(0,0)

    return exp

def decimal_part_to_bin(num, maxlen):
    '''
    ***
    *  num    : int
    *  maxlen : int
    ***
    Convierte la parte decimal de un número en su representación binaria, con una longitud máxima dada por `maxlen`.
    '''
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

def decimal_to_binary(lst):
    '''
    ***
    *  lst  : list
    ***
    Convierte un numero float en su representación binaria IEEE 754 de 32 bits.
    '''
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

def cut_mantissa(mant, positions):
    '''
    ***
    *  mant      : list
    *  positions : int
    ***
    Divide la mantisa de un número binario en parte entera y parte decimal, basado en la cantidad de posiciones a mover.
    '''
    integerPart = [1] + mant[:positions]
    decimalPart = mant[positions:]
    toRet = (integerPart, decimalPart)
    return toRet

        
def bin_to_int(binNum):
    '''
    ***
    *  binNum  : list
    ***
    Convierte un número binario que corresponde a la parte entera de la masntissa a su equivalente numero entero.
    '''
    binNum.reverse()
    num = 0
    for x in range(len(binNum)):
        num += ((2**x)*binNum[x])
    return num

def bin_to_float(bin_num):
    '''
    ***
    *  bin_num  : list
    ***
    Convierte un número binario que corresponde a la parte decimal de la mantissa a su equivalente decimal.
    '''
    i=1
    num = 0.0
    while (i <= len(bin_num)):
        if bin_num[i -1] == 1:
            num += 1/(2**i)
        i += 1
    num = str(num)
    if len(num) > 5:
        return num[2:5]
    else:
        return num[2:]

def sum_mantissa(mant_1, mant_2):
    '''
    ***
    *  mant_1  : list
    *  mant_2  : list
    ***
    Realiza la suma de dos mantissas en notación binaria IEEE 754.
    '''
    i = -1
    carry = 0
    mantissa = []
    while (-len(mant_1) <= i):
        num = mant_1[i] + mant_2[i] + carry
        carry = 0
        if ( num == 0):
            mantissa.insert(0, num)
        elif ( num == 1):
            mantissa.insert(0, num)
        elif ( num == 2):
            mantissa.insert(0, 0)
            carry = 1
        else:
            mantissa.insert(0, 1)
            carry = 1
        i -= 1
    return mantissa

def operate_bin(bin1, bin2):
    '''
    ***
    *  bin1  : list
    *  bin2  : list
    ***
    Realiza operaciones en números binarios IEEE 754 de 32 bits y retorna el resultado.
    '''
    exp1 = bin1[1:9]
    exp2 = bin2[1:9]
    mant1 = bin1[9:]
    mant2 = bin2[9:]

    expNum1 = bin_to_int(exp1)
    expNum2 = bin_to_int(exp2)
    
    positionsToMove = max(expNum1, expNum2)

    if ( len(mant1) > 23):
        del mant1[23:]
    if ( len(mant2) > 23):
        del mant2[23:]
    
    mant1.insert(0, 1)
    mant2.insert(0, 1)

    exp = expNum1 - expNum2
    if (exp < 0):
        i = 0
        while ( i < -exp):
            mant1.insert(0, 0)
            del mant1[-1]
            i += 1
    elif (exp > 0):
        i = 0
        while ( i < exp):
            mant2.insert(0, 0)
            del mant2[-1]
            i += 1    
    mant = sum_mantissa(mant1, mant2)
    if len(mant) == 24:
        del mant[0]
    exponente = integer_part_to_bin(positionsToMove)
    entero = mant[:positionsToMove]
    decimal = mant[positionsToMove:]
    return ([bin1[0]] + exponente + entero + decimal)

def list_to_string(binary_list):
    '''
    ***
    *  binary_list  : list
    ***
    Convierte el numero binario contenido en la lista a una cadena de caracteres, retornando el string del correspondiente numero binario
    '''
    cadena = ""
    for digito in binary_list:
        cadena += str(digito)
    return cadena

archivo = open("operaciones.txt", "r")
desarrollo = open("resultados.txt", "w")
lines = archivo.readlines()

sumas_realizadas = 0
sumas_invalidas = 0

for line in lines:
    num1, num2 = line.strip().split(";")
    line = line_to_list(line.strip())
    binary1 = decimal_to_binary(line[0])
    binary2 = decimal_to_binary(line[1])
    if line[0][0] != line[1][0]:
        string_binary1 = list_to_string(binary1)
        string_binary2 = list_to_string(binary2)
        desarrollo.write(num1 + "/" + string_binary1 + ";" + num2 + "/" + string_binary2 + '\n')
        sumas_invalidas += 1
    else:
        sum_binary = operate_bin(binary1, binary2)
        entero, decimal = cut_mantissa(sum_binary[9:], bin_to_int(sum_binary[1:9])-127)
        signo = sum_binary[0]
        if signo == 0:
            signo = ''
        else:
            signo = '-'
        desarrollo.write(signo + str(bin_to_int(entero)) + '.' + bin_to_float(decimal) + "/" + list_to_string(sum_binary) + '\n')
        sumas_realizadas += 1

archivo.close()
desarrollo.close()
print("Se procesaron", len(lines), "lineas")
print("Fue posible hacer", sumas_realizadas, "sumas")
print("No se pudo procesar", sumas_invalidas, "sumas")