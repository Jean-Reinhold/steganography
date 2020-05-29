import cv2 as cv 
import numpy as np

def form_pixel (color_pixel): 
    gray_pixel = 0
    
    gray_pixel += (color_pixel [0] % 10) * 100
    gray_pixel += (color_pixel [1] % 10) * 10 
    gray_pixel += (color_pixel [2] % 10)  
        
    return gray_pixel 

carrier = cv.imread("carrier.png") 
coluns, rows = carrier.shape[:2] 

message = np.zeros( (coluns, rows) )



for colun in range(coluns) : 
    for row in range (rows): 
        message [colun] [row] += form_pixel( carrier [colun] [row] [:] )
        
cv.imwrite("mensagem_decodificada.png", message)