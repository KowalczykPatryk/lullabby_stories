from prompt_llm import prompt_llm
from image_generate import generate_image
from TTS_generate import generate_voice_file
import json

def build_video():
    with open("prompts/story_idea_prompt.txt") as f:
        prompt = f.read()
    story_idea = prompt_llm(prompt)
    with open("prompts/story_prompt.txt") as f:
        prompt = f.read().replace("<story_idea>", story_idea)
    story_json = json.loads(prompt_llm(prompt))
    with open("promots/image_prompt.txt") as f:
        prompt = f.read()
        for i, text in enumerate(story_json["paragraphs"]):
            prompt = prompt.replace("<SCENE_DESCRIPTION>", text)
            generate_image(prompt,i)
            generate_voice_file(text,i)

if __name__=="__main__":
    build_video()