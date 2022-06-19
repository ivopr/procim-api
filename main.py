from base64 import b64encode
from io import BytesIO, StringIO
from fastapi import FastAPI, File, Request, UploadFile, Response

from actions.yiq import rgb_to_yiq, yiq_to_rgb

app = FastAPI()

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