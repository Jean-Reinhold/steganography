import cv2 as cv 
import numpy as np 

def get_digits(number) : 
    individual_digits = list() 
    
    #apropriação da caracteristica iteravel de strings
    number = str(number)
    
    #garantia para que todos os pixels cinzas tenham 3 digitos
    if len (number) < 3 : 
        if len (number) < 2 : 
            number = "00" + number 
        else :
            number  = "0" + number 
    
    #itera em uma string     
    for digit in number :
        individual_digits.append( int(digit) )
        
    #retorno de uma lista contendo os algarismos individuais de um numero em ordem decrescente de significancia
    return individual_digits

def blend (color_pixel, msg_digits) :   

    encrypted_pixel = list()
    
    #iterando nos tres canais de cor
    for i in range (3): 
        #retira o ultimo digito do valor do canal
        channel = int (color_pixel [i] / 10) 
        
        #substitui o ultimo digito pelo valor de um digito do pixel cinza
        channel = int (channel * 10 + msg_digits [i]) 
        
        #trunca os valores dos channels para que não haja o overflow de uint8
        if channel > 255: 
            channel = 255
        
        encrypted_pixel.append(channel)  
    
    return np.array(encrypted_pixel, np.uint8)


message = cv.imread("cachorro.png",0)
carrier = cv.imread("gato.png")

coluns, rows = message.shape

#iteração em cada pixel de encriptação 
for row in range ( rows ) : 
    for colun in range ( coluns ) : 
        gray_pixel = message [colun] [row] 
        color_pixel = carrier [colun] [row] [:]         
        carrier [colun] [row] [:] = blend(color_pixel, get_digits(gray_pixel) )

#escreve a mensagem encripyted         
cv.imwrite("carrier.png", carrier)
 


    