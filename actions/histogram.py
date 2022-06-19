from PIL import Image
from io import BytesIO
import numpy

# d. Expansão e equalização do histograma;
def expansion(image):
  PILimage = Image.open(BytesIO(image))
  if (PILimage.mode == "RGB"):
    (R, G, B) = PILimage.split()
    R = numpy.asarray(R)
    G = numpy.asarray(G)
    B = numpy.asarray(B)

    # FAÇA AS ALTERAÇÕES EM R, G E B
    rmin = R.min()
    rmax = R.max()
    R = [[(((r - rmin) * 1) / (rmax - rmin)) for r in row] for row in R]
    
    gmin = G.min()
    gmax = G.max()
    G = [[(((r - gmin) * 1) / (gmax - gmin)) for r in row] for row in G]
    
    bmin = B.min()
    bmax = B.max()
    B = [[(((r - bmin) * 1) / (bmax - bmin)) for r in row] for row in B]

    R = numpy.asarray(R) * 255
    G = numpy.asarray(G) * 255
    B = numpy.asarray(B) * 255
    # END FAÇA AS ALTERAÇÕES EM R, G E B

    NPimage = numpy.zeros([PILimage.height, PILimage.width, 3], dtype=numpy.uint8)
    NPimage[:, :, 0] = R
    NPimage[:, :, 1] = G
    NPimage[:, :, 2] = B
  else:
    NPimage = numpy.asarray(PILimage.convert("L"))

    # FAÇA AS ALTERAÇÕES EM NPimage
    npmin = NPimage.min()
    npmax = NPimage.max()
    NPimage = [[(((r - npmin) * 1) / (npmax - npmin)) for r in row] for row in NPimage]
    NPimage = numpy.asarray(NPimage) * 255
    # END FAÇA AS ALTERAÇÕES EM NPimage

  # Transforma o array numpy (que é uma matriz) novamente em uma imagem
  PILimage = Image.fromarray(numpy.uint8(NPimage))
  return PILimage

def equalization(image):
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