# Text-to-Image-Generator
This code utilizes the Stability API AI model to generate Images for free in Painting Fashion Most Often.

# Stable Diffusion Image Generation in Colab

This project allows you to generate images using the Stability AI's Stable Diffusion model via an API. The script takes a text description (prompt) and generates an image based on the prompt, displaying it within the Colab environment.

## Requirements

- Google Colab
- A valid API key from [Stability AI](https://stability.ai/)

## Setup Instructions

1. **Clone this repository** or upload the script to your Colab notebook.
   
2. **Install necessary libraries** by running the following cell in Colab:
    ```python
    !pip install requests pillow
    ```

3. **Set up your Stability AI API key:**
    - Go to [Stability AI](https://stability.ai/), sign up or log in, and obtain an API key.
    - Replace the `API_KEY` variable in the script with your API key:
      ```python
      API_KEY = "your_stability_ai_api_key_here"
      ```

4. **Run the Script:**
    - After setting the API key, run the script in your Colab environment.
    - It will prompt you to enter a text description for the image. After entering the description, it will generate an image and display it in the Colab notebook.

5. **Download the generated image (optional):**
    - If you wish to download the generated image, run:
      ```python
      from google.colab import files
      files.download("/content/generated_image.png")
      ```

## Usage Example

1. Run the script and enter a prompt when asked. For example:
    - **Prompt**: "A futuristic city with flying cars"
2. The script will generate an image based on your prompt and display it inline in the Colab notebook.

## Notes

- The generated image is saved in the `/content/` directory of your Colab environment.
- The image will automatically display within the notebook, and you can download it if needed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
