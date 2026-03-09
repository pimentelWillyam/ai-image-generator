from diffusers import StableDiffusionPipeline
import torch

class ImageService:

    def __init__(self):
        self.pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float16
        ).to("cuda")

    def generate(self, prompt: str):
        image = self.pipe(prompt).images[0]
        return image