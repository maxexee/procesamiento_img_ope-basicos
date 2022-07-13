import  os
import  time
import  numpy   as      np
from    PIL     import  Image

def reiniciar():
    re  =   input('¿Reiniciar?(s/n):    ')
    if  re  ==  's' or  re  ==  'S' or  re  ==  'si'    or  re  ==  'Si'    or  re  ==  'SI':
        os.system('clear')
        main()
    else:
        os.abort()
def arr_numpy():
    img1    =   Image.open('src/original.jpg')
    img2    =   img1.convert('L')
    img_arr =   np.array(img2)
    temp    =   [img_arr,img1.size]
    print('\nORIGINAL\n')
    print(temp[0])
    print('\n---------------------------------------\n')
    return  temp

def newImg(matriz):
    img_res =   Image.fromarray(matriz)
    img_res.show()

#1-OPERADOR DE IDENTIDAD.
def opI():
    img_arr_t   =   arr_numpy()
    img_arr_t   =   img_arr_t[0]
    img_opI_1   =   np.array([1  *   img_arr_t[i]  for i   in  range(len(img_arr_t))])
    print('OPERADOR DE IDENTIDAD\n')
    print(img_opI_1)
    newImg(img_opI_1)

#2-OPERADOR INVERSO O NEGATIVO.
def opN():
    img_arr_t   =   arr_numpy()
    img_arr_t   =   img_arr_t[0]
    img_opN_1   =   np.array([255-img_arr_t[i]   for i   in  range(len(img_arr_t))])
    print('OPERADOR INVERSO O NEGATIVO\n')
    print(img_opN_1)
    newImg(img_opN_1)

#3-OPERADOR UMBRAL.
def opU(p1):
    temp        =   []
    img_arr_t_G   =   arr_numpy()
    img_arr_t   =   img_arr_t_G[0]
    for i   in  range(len(img_arr_t)):
        for j   in  img_arr_t[i]:
            if      j   <=  p1:
                j   =   0
                temp.append(j)
            elif    j   >   p1:
                j   =   255
                temp.append(j)
    img_opU_1   =   np.array(temp).astype(np.uint8)
    img_opU_1   =   img_opU_1.reshape(img_arr_t_G[1][::-1])
    print('OPERADOR UMBRAL\n')
    print(img_opU_1)
    newImg(np.array(img_opU_1))

#4-OPERADOR INTERVALO UMBRAL BINARIO.
def opUB(p1, p2):
    temp        =   []
    img_arr_t_G   =   arr_numpy()
    img_arr_t   =   img_arr_t_G[0]
    for i   in  range(len(img_arr_t)):
        for p   in  img_arr_t[i]:
            if  (p   <=  p1)  | (p  >=  p2):
                p   =   255
                temp.append([p])
            elif    p1<p<p2:
                p   =   0
                temp.append([p])
    img_opUB_1  =   np.array(temp).astype(np.uint8)
    img_opUB_1  =   img_opUB_1.reshape(img_arr_t_G[1][::-1])
    print('OPERADOR INTERVALO UMBRAL BINARIO\n')
    print(img_opUB_1)
    newImg(img_opUB_1)

#5-OPERADOR INTERVALO UMBRAL BINARIO INVERTIDO.
def opUBI(p1,p2):
    temp    =   []
    img_arr_t_G   =   arr_numpy()
    img_arr_t   =   img_arr_t_G[0]
    for i   in  range(len(img_arr_t)):
        for p   in  img_arr_t[i]:
            if  (p<=p1) |   (p>=p2):
                p=0
                temp.append(p)
            elif    p1<p<p2:
                p   =   255
                temp.append(p)
    img_opUBI_1 =   np.array(temp).astype(np.uint8)
    img_opUBI_1 =   img_opUBI_1.reshape(img_arr_t_G[1][::-1])
    print('OPERADOR INTERVALO UMBRAL BINARIO INVERTIDO\n')
    print(img_opUBI_1)
    newImg(img_opUBI_1)

#6-OPERADOR UMBRAL ESCALA DE GRISES.
def opUEG(p1,p2):
    temp    =   []
    img_arr_t_G   =   arr_numpy()
    img_arr_t   =   img_arr_t_G[0]
    for i   in  range(len(img_arr_t)):
        for p   in  img_arr_t[i]:
            if  (p<=p1) |   (p>=p2):
                p=255
                temp.append(p)
            elif    p1<p<p2:
                p   =   p
                temp.append(p)
    img_opUEG_1 =   np.array(temp).astype(np.uint8)
    img_opUEG_1 =   img_opUEG_1.reshape(img_arr_t_G[1][::-1])
    print('OPERADOR UMBRAL ESCALA DE GRISES\n')
    print(img_opUEG_1)
    newImg(img_opUEG_1)

#7-OPERADOR UMBRAL ESCALA DE GRISES INVERTIDO.
def opUEGI(p1,p2):
    temp    =   []
    img_arr_t_G   =   arr_numpy()
    img_arr_t   =   img_arr_t_G[0]
    for i   in  range(len(img_arr_t)):
        for p   in  img_arr_t[i]:
            if  (p<=p1) |   (p>=p2):
                p=255
                temp.append(p)
            elif    p1<p<p2:
                p   =   255-p
                temp.append(p)
    img_opUEGI_1 =   np.array(temp).astype(np.uint8)
    img_opUEGI_1 =   img_opUEGI_1.reshape(img_arr_t_G[1][::-1])
    print('OPERADOR UMBRAL ESCALA DE GRISES INVERTIDO\n')
    print(img_opUEGI_1)
    newImg(img_opUEGI_1)

#8-OPERADOR EXTENSIÓN.
def opE(p1,p2):
    temp    =   []
    img_arr_t_G   =   arr_numpy()
    img_arr_t   =   img_arr_t_G[0]
    for i   in  range(len(img_arr_t)):
        for p   in  img_arr_t[i]:
            if  (p<=p1) |   (p>=p2):
                p   =   0
                temp.append(p)
            elif    p1<p<p2:
                p   =   (255*(p-p1)/(p2-p1))
                temp.append(p)
    img_opE_1   =   np.array(temp).astype(np.uint8)
    img_opE_1   =   img_opE_1.reshape(img_arr_t_G[1][::-1])
    print('OPERADOR EXTENSIÓN\n')
    print(img_opE_1)
    newImg(img_opE_1)

def main():
    print('----------------------------------------------------------------')
    print('----------------------------------------------------------------')
    print('-----                    MENÚ DE OPERADORES                -----')
    print('----------------------------------------------------------------')
    print('-----                                                      -----')
    print('-----                1-OPERADOR DE IDENTIDAD               -----')
    print('-----            2-OPERADOR INVERSO O NEGATIVO             -----')
    print('-----                3-OPERADOR UMBRAL                     -----')
    print('-----        4-OPERADOR INTERVALO UMBRAL BINARIO           -----')
    print('-----    5-OPERADOR INTERVALO UMBRAL BINARIO INVERTIDO     -----')
    print('-----        6-OPERADOR UMBRAL ESCALA DE GRISES            -----')
    print('-----    7-OPERADOR UMBRAL ESCALA DE GRISES INVERTIDO      -----')
    print('-----                8-OPERADOR EXTENSIÓN                  -----')
    print('-----                                                      -----')
    print('----------------------------------------------------------------')
    print('-----                                                      -----')
    print('-----                0-TODOS LOS OPERADORES                -----')
    print('-----            (SE APLICARÁ SOLO UN P1 Y P2              -----')
    print('-----             PARA TODOS LOS OPERADORAS)               -----')
    print('-----                                                      -----')
    print('----------------------------------------------------------------')
    print('-----                                                      -----')
    print('----- SELECCIONA EL NÚMERO DEL OPERADOR                    -----')
    print('-----                                                      -----')
    print('----------------------------------------------------------------')
    print('----------------------------------------------------------------')
    try:
        ope =   int(input('Número de operador:'))
        if      ope ==  1:
            opI()
            reiniciar()
        elif    ope ==  2:
            opN()
            reiniciar()
        elif    ope ==  3:
            p1_3  =   int(input('P1:  '))
            opU(p1_3)
            reiniciar()
        elif    ope ==  4:
            p1_4  =   int(input('P1:  '))
            p2_4  =   int(input('P2:  '))
            opUB(p1_4,  p2_4)
            reiniciar()
        elif    ope ==  5:
            p1_5  =   int(input('P1:  '))
            p2_5  =   int(input('P2:  '))
            opUBI(p1_5,  p2_5)
            reiniciar()
        elif    ope ==  6:
            p1_6  =   int(input('P1:  '))
            p2_6  =   int(input('P2:  '))
            opUEG(p1_6,  p2_6)
            reiniciar()
        elif    ope ==  7:
            p1_7  =   int(input('P1:  '))
            p2_7  =   int(input('P2:  '))
            opUEGI(p1_7,  p2_7)
            reiniciar()
        elif    ope ==  8:
            p1_8  =   int(input('P1:  '))
            p2_8  =   int(input('P2:  '))
            opE(p1_8,  p2_8)
            reiniciar()
        elif    ope ==  0:
            p1_0  =   int(input('P1:  '))
            p2_0  =   int(input('P2:  '))
            opI()
            opN()
            opU(p1_0)
            opUB(p1_0,p2_0)
            opUBI(p1_0,p2_0)
            opUEG(p1_0,p2_0)
            opUEGI(p1_0,p2_0)
            opE(p1_0,p2_0)
            reiniciar()
        else:
            print('Caracter o número incorrecto')
            print('Reiniciando...')
            time.sleep(1.5)
            reiniciar()

    except  Exception   as  e:
        print(e)
main()
