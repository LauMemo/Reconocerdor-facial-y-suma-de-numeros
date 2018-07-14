import numpy as np
import cv2
from PIL import Imagen
num = 0
simplenum = 0

def crear_Registro():
    dector_cara = cv2.CascadeClassifier('Reconocedor_facial.xml')
    camara = cv2.VideoCapture(0)

    codigo = input("Ingrese el codigo de usuario: ")

    while(True):
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = dector_cara.detectMultiScale(gray, 1.3, 5)
 
        for (x,y,w,h) in faces:
            print (x,y,w,h)
            cv2.rectangle(img,(x,y),(x+w,y+h),(125,255,0),2)
            cv2.imwrite("Personas Registradas/" + Id +"/" + str(samplenum) + ".jpg", gray[y:y+h,x:x+w])
            simplenum = simplenum + 1
            cv2.imshow("Usuario se está registrado con exito",img)

            #cv2.imwrite("Registro/" + codigo + "_" + str(simplenum) + ".jpg", gray[y:y+h,x:x+w])
            #cv2.imwrite("Registro/Usuario_" + codigo + str(simplenum) + ".jpg", gray[y:y+h,x:x+w])

        if cv2.waitKey(50) & 0xFF == ord('q'):
            break
        else simplenum > 25:
            break

    camara.release()
    cv2.destroyAllWindows()
#asedgaeawe WDIuwuQWFP


def reconocer():
    reconocer = cv2.face.LBPHFaceRecognizer_create()
    reconocer.read('trainner/trainner.yml')
    cascadePath = "Reconocedor_facial.xml"
    perfilesCascade = cv2.CascadeClassifier(cascadePath)

    camara = cv2.VideoCapture(0)
    identificacion = False

    font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        ret, im = camara.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        perfiles = perfilesCascade.detectMultiScale(gray, 1.2,5)
        for(x, y, w, h) in perfiles:
            cv2.rectangle(im,(x, y),(x+w, y+h),(225, 0, 0), 2)
            Id, conf = reconocer.predict(gray[y:y+h,x:x+w])
            if(conf<50):
                if(Id==1):
                    Id="Laurie"
                    identificacion = True
                elif(Id==2):
                    Id="Amadís"
                    identificacion = True
            else:
                Id="Buscando..."
            cv2.putText(im,str(Id), org=(x,y+h),fontFace=font, color=(255,255,255), fontScale=1)

            if identificacion:
                break
        cv2.imshow('im',im)
        if identificacion:
            break
        if cv2.waitKey(10) & 0xFF==ord('q'):
            break


    camara.release()
    cv2.destroyAllWindows()

    return identificacion

