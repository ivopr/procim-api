from base64 import b64encode
from io import BytesIO, StringIO
from fastapi import FastAPI, File, Request, UploadFile, Response
from actions.histogram import expansion
from actions.negative import negative

from actions.yiq import rgb_to_yiq, yiq_to_rgb

app = FastAPI()

# Para retornar a imagem ao inves da base64
# return Response(content = bytes_image.getvalue(), media_type="image/png")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/rgb-yiq")
async def RGBtoYIQ(file: UploadFile = File(...)):
    ret = rgb_to_yiq(await file.read())
    bytes_image = BytesIO()
    ret.save(bytes_image, format="PNG")

    img_str = b64encode(bytes_image.getvalue())

    return img_str

@app.post("/yiq-rgb")
async def YIQtoRGB(file: UploadFile = File(...)):
    ret = yiq_to_rgb(await file.read())
    bytes_image = BytesIO()
    ret.save(bytes_image, format="PNG")

    img_str = b64encode(bytes_image.getvalue())

    return img_str

@app.post("/negative")
async def neg(file: UploadFile = File(...)):
    ret = negative(await file.read())
    bytes_image = BytesIO()
    ret.save(bytes_image, format="PNG")

    img_str = b64encode(bytes_image.getvalue())

    return img_str


@app.post("/expansion")
async def histexp(file: UploadFile = File(...)):
    ret = expansion(await file.read())
    bytes_image = BytesIO()
    ret.save(bytes_image, format="PNG")

    img_str = b64encode(bytes_image.getvalue())

    return img_str