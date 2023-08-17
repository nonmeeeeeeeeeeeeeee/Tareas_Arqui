line = "45.5;-5.353"

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
    Convierte un número binario en su equivalente decimal.
    '''
    binNum.reverse()
    num = 0
    for x in range(len(binNum)):
        num += ((2**x)*binNum[x])
    return num

def operate_bin(bin1, bin2):
    '''
    ***
    *  bin1  : list
    *  bin2  : list
    ***
    Realiza operaciones en números binarios IEEE 754 de 32 bits y retorna el resultado.
    '''
    sign = bin[:1]
    exp1 = bin1[1:9]
    exp2 = bin2[1:9]
    mant1 = bin1[9:]
    mant2 = bin2[9:]

    expNum1 = bin_to_int(exp1)
    expNum2 = bin_to_int(exp2)

    if expNum1 > expNum2:
        finalExp = exp1
        positionsToMove = expNum1 - 127
    else:
        finalExp = exp2
        positionsToMove = expNum2 - 127

    int1, decimal1 = cut_mantissa(mant1, positionsToMove)
    int2, decimal2 = cut_mantissa(mant2, positionsToMove)
 
    """
    
    Trabajar desde aqui!!!!

    Falta:

    1) finalizar la funcion sum bin, lo que haria yo seria 
    1ro dar vuelta las listas de binarios para operar en orden, 
    luego operar los 0 y unos y si sobra uno colocarlo alfinal. 
    2do dar vuelta denuevo la lista y 3ro retornar el numero 
    binario en forma de lista

    2) para la suma de las partes decimales de los numeros, si se
    arrastra un 1 alfinal agrandando el decimal (por ejemplo 0.9 + 0.9 = 1.9),
    hay que sumar ese uno a la suma de las partes enteras, y sacarlo de la lista de decimales
    Se me ocurre que se podria hacer con la funcion sum_bin entre el resultado
    del paso 1 y una lista que sea lst = [0, 0 , ... , 1], que el largo de la
    lista sea del mismo largo que la suma de los enteros.

    3) unir las listas de entero y decimal y cortarla para que tenga largo 24 y 
    sacar el primer termino de la lista (puede quedar con con mas de 24 0's y 1's 
    por eso hay que cortar, y el primer termino seca por una propiedad de la mantisa)

    4) unir la lista del paso 3 con sign y finalExp de la forma:
    finalBin = sign + finalExp + listaPaso3

    5) crear una funcion que pase las listas de binarios que tenemos a string

    6) crear una funcion main que abra el archivo a leer y cree el archivo con las respuestas (esto lo puedo hacer yo)

    """
    return

def sum_bin(bin1, bin2):
    '''
    ***
    *  bin1  : list
    *  bin2  : list
    ***
    Realiza la suma de dos números binarios en notación binaria IEEE 754 de 32 bits.
    '''
    
    return




#print(decimal_to_binary(('+', '42', '87')))
test1 = [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1]
test2 = [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0]
print(sum_bin(test1, test2))
