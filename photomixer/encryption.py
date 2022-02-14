from copy import copy

sbox = [
   0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
   0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
   0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
   0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
   0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
   0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
   0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
   0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
   0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
   0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
   0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
   0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
   0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
   0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
   0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
   0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]
   
table = [[2,1,1,3],[3,2,1,1],[1,3,2,1],[1,1,3,2]]


def subBytes(matrix):
    for row in range(4):
	    for col in range(4):
		    matrix[row][col] = sbox[matrix[row][col]]
		    print(matrix[row][col])
			
    return matrix

def shiftRows(matrix):
    returnVal = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	
    for x in range(4):
        returnVal[0][x] = matrix[0][x]
	
    returnVal[1][3] = matrix[1][0]
    for x in range(3):
        returnVal[1][x] = matrix[1][x+1]

    for x in range(2):
        returnVal[2][x] = matrix[2][x+2]
        returnVal[2][x+2] = matrix[2][x]
	
    returnVal[3][0] = matrix[3][3]	
    for x in range(3):
        returnVal[3][x+1] = matrix[3][x]

    return(returnVal)	


'''
This function mix the colums with the table
Input: matrix
Output: encryted matrix
'''
def galoisMult(a, b):
    p = 0
    hiBitSet = 0
    for i in range(8):
        if b & 1 == 1:
            p ^= a
        hiBitSet = a & 0x80
        a <<= 1
        if hiBitSet == 0x80:
            a ^= 0x1b
        b >>= 1
    return p % 256
	
def mixColumn(column):
    temp = copy(column)
    column[0] = galoisMult(temp[0],2) ^ galoisMult(temp[3],1) ^ galoisMult(temp[2],1) ^ galoisMult(temp[1],3)
    column[1] = galoisMult(temp[1],2) ^ galoisMult(temp[0],1) ^ galoisMult(temp[3],1) ^ galoisMult(temp[2],3)
    column[2] = galoisMult(temp[2],2) ^ galoisMult(temp[1],1) ^ galoisMult(temp[0],1) ^ galoisMult(temp[3],3)
    column[3] = galoisMult(temp[3],2) ^ galoisMult(temp[2],1) ^ galoisMult(temp[1],1) ^ galoisMult(temp[0],3)
    return (column)

    
'''
This function add the key to the matrix
Input: key array, matrix
Output: encryted matrix
'''
def addRoundKey(key, matrix):
    returnVal = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    hexKey = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] 
    mat = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] 
    i=0
    
    #convert the key from string to hex
    for x in range(4):
        for y in range(4):
            hexKey[y][x] = hex(ord(key[i]))
            i += 1
			
    i=0
    
    #convert the key from string to hex
    for x in range(4):
        for y in range(4):
            mat[y][x] = hex(ord(matrix[i]))
            i += 1			
	
    #add the key to the matrix
    for x in range(4):
        for y in range(4):
            returnVal[y][x] = hex(int(mat[y][x], 16) ^ int(hexKey[y][x], 16)) #xor
            
    return (returnVal)
    
	
def encryptionForEachPart(key, HexArr):
    matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] 
    i = 0	

    for x in range(4):
        for y in range(4):
            matrix[y][x] = HexArr[i]
            i = i + 1
			
    matrix = addRoundKey(key, matrix)
	
    for x in range(9):
        matrix = subBytes(matrix)
        matrix = shiftRows(matrix)
        matrix = mixColumn(matrix)
        matrix = addRoundKey(matrix)
		
    matrix = subBytes(matrix)
    matrix = shiftRows(matrix)
    matrix = addRoundKey(key, matrix)
	
    return matrix;
	
def encrytion(key, pictureHexArr):
    keyArr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] 
    i = 0
    
    for letter in key:
        keyArr[i] = letter
        i += 1
        
    i = 0

    for x in len(pictureHexArr):
        arr[i] = pictureHexArr[x]
		
        if (x / 16 == 0):
            matrix = encryptionForEachPart(keyArr, arr)
            i = 0
			
            # need to put the matrix back to the pictureHexArr or create new picture .....


#pictureHexArr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# matrix = "Two One Nine Two"
# key = "Thats my Kung Fu"
# matrix = addRoundKey(key, matrix)
# print(matrix)
matrix = [[0x63,0x2F,0xAF,0xA2],[0xEB,0x93,0xC7,0x20],[0x9F,0x92,0xAB,0xCB],[0xA0,0xC0,0x30,0x2B]]
matrix = mixColumn(g)
for x in range(4):
    for y in range(4):
        matrix[y][x] = hex(matrix[y][x])
print(matrix)
