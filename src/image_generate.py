import torch
from diffusers import StableDiffusionPipeline


def generate_image(prompt, number):
    model_id = "Lykon/DreamShaper"  

    pipe = StableDiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float16
    ).to("cuda")

    pipe.enable_xformers_memory_efficient_attention()

    image = pipe(prompt, height=512, width=512, num_inference_steps=200, guidance_scale=7.5).images[0]

    image.save(f"images/image{number}.png")

if __name__=="__main__":
    generate_image()

