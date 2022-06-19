from PIL import Image
from io import BytesIO
import numpy

# c. Filtros de média e mediana de ordem n x n;
def mean(image, n):
  PILimage = Image.open(BytesIO(image))

  if (PILimage.mode == "RGB"):
    (R, G, B) = PILimage.split()
    R = numpy.asarray(R)
    G = numpy.asarray(G)
    B = numpy.asarray(B)
    
    newR = numpy.pad(R, [n, n], mode="constant")
    newG = numpy.pad(G, [n, n], mode="constant")
    newB = numpy.pad(B, [n, n], mode="constant")

    for i in range(n, newR.shape[0] - n):
      for j in range(n, newR.shape[1] - n):
        newR[i][j] = numpy.mean(newR[i - n : i + n, j - n : j + n], dtype=numpy.float32)
        newG[i][j] = numpy.mean(newG[i - n : i + n, j - n : j + n], dtype=numpy.float32)
        newB[i][j] = numpy.mean(newB[i - n : i + n, j - n : j + n], dtype=numpy.float32)
    # FAÇA AS ALTERAÇÕES EM R, G E B
    # END FAÇA AS ALTERAÇÕES EM R, G E B

    NPimage = numpy.zeros([PILimage.height, PILimage.width, 3], dtype=numpy.uint8)
    NPimage[:, :, 0] = newR[n:newR.shape[0]-n,n:newR.shape[1]-n]
    NPimage[:, :, 1] = newG[n:newR.shape[0]-n,n:newR.shape[1]-n]
    NPimage[:, :, 2] = newB[n:newR.shape[0]-n,n:newR.shape[1]-n]
  else:
    NPimage = numpy.asarray(PILimage.convert("L"))

    # FAÇA AS ALTERAÇÕES EM NPimage
    NPimageAux = numpy.pad(NPimage, [n, n], mode="constant")
    for i in range(n, NPimageAux.shape[0] - n):
      for j in range(n, NPimageAux.shape[1] - n):
        NPimageAux[i][j] = numpy.mean(NPimageAux[i - n : i + n, j - n : j + n], dtype=numpy.float32)
    
    NPimage = NPimageAux[n:NPimageAux.shape[0]-n,n:NPimageAux.shape[1]-n]
    # END FAÇA AS ALTERAÇÕES EM NPimage

  # Transforma o array numpy (que é uma matriz) novamente em uma imagem
  PILimage = Image.fromarray(numpy.uint8(NPimage))
  return PILimage

def median(image):
  PILimage = Image.open(BytesIO(image))
  if (PILimage.mode == "RGB"):
    (R, G, B) = PILimage.split()
    R = numpy.asarray(R)
    G = numpy.asarray(G)
    B = numpy.asarray(B)

    # FAÇA AS ALTERAÇÕES EM R, G E B

    # END FAÇA AS ALTERAÇÕES EM R, G E B

    NPimage = numpy.zeros([PILimage.height, PILimage.width, 3], dtype=numpy.uint8)
    NPimage[:, :, 0] = R
    NPimage[:, :, 1] = G
    NPimage[:, :, 2] = B
  else:
    NPimage = numpy.asarray(PILimage.convert("L"))

    # FAÇA AS ALTERAÇÕES EM NPimage

    # END FAÇA AS ALTERAÇÕES EM NPimage

  # Transforma o array numpy (que é uma matriz) novamente em uma imagem
  PILimage = Image.fromarray(numpy.uint8(NPimage))
  return PILimage