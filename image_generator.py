import torch

from PIL import Image, ImageDraw, ImageFont
from diffusers import StableDiffusionPipeline

try:
    pipe = StableDiffusionPipeline.from_pretrained( "CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16).to("cuda")
except Exception as e:
    pipe = None
    print(f"Error loading model: {e}. A fallback image will be used.")

def image_creator(prompt, filename):
    try:
        if pipe:
            image = pipe(prompt).images[0]
        else:
            raise RuntimeError("StableDiffusionPipeline not available.")
    except Exception as e:
        print(f"Error generating image: {e}. Creating fallback image.")
        image = Image.new("RGB", (512, 512), color=(255, 255, 255))
        draw = ImageDraw.Draw(image)
        draw.text((10, 10), f"Image for:\n{prompt}", fill=(0, 0, 0))
    image.save(f"images/{filename}.png")