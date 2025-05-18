import sys
from llama_cpp import Llama

llm = Llama(
    model_path="../models/phi-2.Q5_K_M.gguf",
    n_ctx=4096,
    n_gpu_layers=16,
    n_batch=128,
    f16_kv=True,
    verbose=False
)

def prompt_llm(prompt: str, llm=llm) -> str:
    resp = llm(
        prompt,
        max_tokens=512,
        temperature=0.7,
        top_p=0.9,
        top_k=40,
    )
    return resp["choices"][0]["text"]

if __name__=="__main__":
    print("Output: "+str(prompt_llm(sys.argv[1])))