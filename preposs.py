import cv2 as cv 

#leitura das imagens 
#argumento "0", imagem lida em tons de cinza 
cachorro_cinza = cv.imread("cachorro.png", 0) 
gato_colorido = cv.imread("gato.png") 

#resize do cachorro para tamanho do gato 
#metodo shape retorna o numero de dimensões, queremos apenas largura e altura
colunas, linhas = gato_colorido.shape[:2]
cachorro_cinza = cv.resize(cachorro_cinza, (linhas, colunas))

#check visual se a imagem tá realmente do mesmo tamanho 
cv.imshow("cachorro", cachorro_cinza)
cv.imshow("gato", gato_colorido)

#faz com que o programa não seja interrompido até o usuário pressionar uma tecla
key = cv.waitKey(0) 

if key == ord("k"): 
    cv.imwrite("cachorro.png", cachorro_cinza)
    cv.imwrite("gato.png", gato_colorido)