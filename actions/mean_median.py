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