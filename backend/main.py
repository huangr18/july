import asyncio
import time
import uuid
from concurrent.futures import ProcessPoolExecutor
from functools import partial

import cv2
import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
import numpy as np
from PIL import Image

import config
import inference


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome from the API"}


async def combine_images(output, resized, name):
    final_image = np.hstack((output, resized))
    cv2.imwrite(name, final_image)


@app.post("/{style}")
async def get_image(style: str, file: UploadFile = File(...)):
    image = np.array(Image.open(file.file))
    model = config.STYLES[style]
    start = time.time()
    output, resized = inference.inference(model, image)
    name = f"/storage/{str(uuid.uuid4())}.jpg"
    print(f"name: {name}")
    # name = file.file.filename
    cv2.imwrite(name, output)
    #models = config.STYLES.copy()
    #del models[style]
    #asyncio.create_task(generate_remaining_models(models, image, name))
    return {"name": name, "time": time.time() - start}


async def generate_remaining_models(models, image, name: str):
    executor = ProcessPoolExecutor()
    event_loop = asyncio.get_event_loop()
    await event_loop.run_in_executor(
        executor, partial(process_image, models, image, name)
    )


def process_image(models, image, name: str):
    for model in models:
        output, resized = inference.inference(models[model], image)
        name = name.split(".")[0]
        name = f"{name.split('_')[0]}_{models[model]}.jpg"
        cv2.imwrite(name, output)

# **************************** Segmentation ************************
from segmentation_demo.segmentation import get_segmentator, get_segments
seg_model = get_segmentator()

@app.post("/segmentation/param")
async def get_segmentation_map(file: bytes = File(...)):
    """Get segmentation maps from image file"""
    segmented_image = get_segments(seg_model, file)
    bytes_io = io.BytesIO()
    segmented_image.save(bytes_io, format="PNG")
    return Response(bytes_io.getvalue(), media_type="image/png")



# ****************************** Sample ******************************

from aivision import runcv
@app.post("/{temp_file_to_save}")
def save_video(temp_file_to_save:str):
    result_file_name = runcv(temp_file_to_save)

    return result_file_name
    # start = time.time()
    # return {"name": name, "time": time.time() - start}




if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)