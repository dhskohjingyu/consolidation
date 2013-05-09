def dec_to_bin(n):
    ''' function to convert a decimal number into a binary number and return it '''
    quotient = n
    binary = ""

    while quotient != 0:
        binary += str(n % 2)
        quotient = n//2

        n = quotient

    return binary[::-1]

def dec_to_oct(n):
    ''' function to convert a decimal number into a octary number and return it '''
    quotient = n
    octal = ""

    while quotient != 0:
        octal += str(n % 8)
        quotient = n//8

        n = quotient

    return octal[::-1]

def dec_to_hex(n):
    ''' function to convert a hexadecimal number into a decimal number and return it '''
    hex_number_base = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    
    quotient = n
    octal = ""

    while quotient != 0:
        octal += hex_number_base[n % 16]
        quotient = n//16

        n = quotient

    return octal[::-1]

def oct_to_dec(n):
    ''' function to convert a octal number into a decimal number and return it '''
    value = 0
    oct_string = str(n)

    for i in range(len(oct_string)):
        digit = int(oct_string[i])
        value += digit * (8 ** (len(oct_string) - i - 1))

    return value

def bin_to_dec(n):
    ''' function to convert a binary number into a decimal number and return it '''
    value = 0
    bin_string = str(n)

    for i in range(len(bin_string)):
        digit = int(bin_string[i])
        value += digit * (2 ** (len(bin_string) - i - 1))

    return value

def hex_to_dec(n):
    ''' function to convert a decimal number into a hexadecimal number and return it '''
    hex_number_base = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    
    value = 0

    for char in n:
        value += hex_number_base[char]

    return value

#print(dec_to_bin(20))
#print(bin_to_dec(10))
#print(dec_to_oct(25))
#print(oct_to_dec(31))
#print(dec_to_hex(100))
#print(hex_to_dec('A'))
