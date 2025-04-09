import os
import sys
import base64

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.llm_streaming_client.client import LLMStreamingClient
from src.llm_streaming_client.config.config import CONFIG

def main():
    base_url = CONFIG.BASE_URL
    timeout = CONFIG.TIMEOUT

    client = LLMStreamingClient(base_url, timeout)

    try:
        text = "La mañana comenzó con un cielo nublado y una brisa suave que anunciaba la llegada de la lluvia. A pesar del clima, la ciudad se mantenía activa, con personas apresuradas caminando por las aceras y el ruido constante de los autos en las avenidas. Había una especie de calma dentro del movimiento, como si ese tipo de días invitan a la introspección."
        action_key = "summarize"
        llm_name = "openai"
        model_name = "gpt-4o-mini"

        response = client.handle_request(
            text=text,
            action_key=action_key,
            llm_name=llm_name,
            model_name=model_name,
        )
        print("Response from handle_request (summarize):", response)
    except Exception as e:
        print("Error handling request (summarize):", e)

    try:
        action_key = "extract"
        llm_name = "openai"
        model_name = "gpt-4o-mini"

        image_path = os.path.join(os.path.dirname(__file__), "example_image.png")
        with open(image_path, "rb") as image_file:
            image_base64 = base64.b64encode(image_file.read()).decode("utf-8")

        response = client.handle_request(
            text=None,  
            action_key=action_key,
            llm_name=llm_name,
            model_name=model_name,
            image_object=image_base64, 
        )
        print("Response from handle_request (extract):", response)
    except Exception as e:
        print("Error handling request (extract):", e)

if __name__ == "__main__":
    main()