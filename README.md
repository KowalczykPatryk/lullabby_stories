# Lullaby Stories


A small Python project that uses Stable Diffusion to generate images for my YouTube videos.

---

## 🔧 Prerequisites

- Python ≥ 3.8  
- NVIDIA GPU (optional; CPU fallback is very slow)  
- Git  

---

## ⚙️ Installation

1. Clone this repo:  
   ```bash
   git clone https://github.com/KowalczykPatryk/lullabby_stories.git
   cd lullabby_stories
````

2. Create and activate a virtual environment:
    ```bash
   python3 -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows
    ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with your Hugging Face token:

   ```bash
   # .env
   HUGGINGFACE_TOKEN=hf_xxxYourTokenxxx
   ```

   **Important:** Do **not** commit `.env` to source control. It’s already in `.gitignore`.

---

## Usage

## 🛡️ Licensing & Attribution

This project uses Stable Diffusion under the **Stability AI Community License**:

* **Model**: Stable Diffusion 3.5 Large by Stability AI
* **Model page**: [https://huggingface.co/stabilityai/stable-diffusion-3.5-large](https://huggingface.co/stabilityai/stable-diffusion-3.5-large)
* **License**: [https://stability.ai/community-license](https://stability.ai/community-license)

**Powered by Stability AI**

