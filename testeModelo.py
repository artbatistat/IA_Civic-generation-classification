import numpy as np
import cv2
from keras.models import load_model

# Carrega a imagem
imgOrignal = cv2.imread("ImageForTest/teste.png")
imgHeight,imgWitdh,imgChannel = imgOrignal.shape

# Carrega o modelo
model = load_model('modelo.h5')

# Funções de pré-processamento
def grayscale(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img

def equalize(img):
    img = cv2.equalizeHist(img)
    return img

def preprocessing(img):
    img = grayscale(img)
    img = equalize(img)
    img = img / 255
    return img

# Função para obter o nome da classe
def getClassName(classNo):
    if classNo == 0:
        return 'Honda Civic G5'
    elif classNo == 1:
        return 'Honda Civic G6'
    elif classNo == 2:
        return 'Honda Civic G7'
    elif classNo == 3:
        return 'Honda Civic G8'
    elif classNo == 4:
        return 'Honda Civic G9'
    elif classNo == 5:
        return 'Honda Civic G10'

# Pré-processamento da imagem
img = np.asarray(imgOrignal)
img = cv2.resize(img,(160,160))
img = preprocessing(img)
img = img.reshape(1, 160, 160, 1)

# Faz a predição
predictions = model.predict(img)
indexVal = np.argmax(predictions)
probabilityValue = np.amax(predictions)
print(indexVal, probabilityValue)

# Imprime o resultado na imagem
className = getClassName(indexVal)
cv2.putText(imgOrignal, "Classe: "+className, (120, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5, cv2.LINE_AA)
cv2.putText(imgOrignal, "Probabilidade:"+str(round(probabilityValue * 100, 2)) + "%", (120, 160), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 8, cv2.LINE_AA)
print("Classe: "+className)
print("Probabilidade:"+str(round(probabilityValue * 100, 2)) + "%")


# Mostra a imagem com o resultado
nova_largura = 800
proporcao = nova_largura / imgOrignal.shape[1]
nova_altura = int(imgOrignal.shape[0] * proporcao)
img_redimensionada = cv2.resize(imgOrignal, (nova_largura, nova_altura))
cv2.imshow("Resultado", img_redimensionada)
while cv2.waitKey(1) != ord('q'):
    pass

