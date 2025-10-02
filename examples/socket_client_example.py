import os
import sys
import uuid

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.llm_streaming_client.client import LLMStreamingClient
from src.llm_streaming_client.config.config import CONFIG


def token_printer(content: str, finished: bool):
    print(content, end="", flush=True)
    if finished:
        print("\n--- STREAM FINISHED ---")


if __name__ == "__main__":
    base_url = CONFIG.BASE_URL
    timeout = CONFIG.TIMEOUT
    action_key = "assistant"

    assistant = {
        "texts": [
            "Hola, me llamo Pepito.",
            "¿Cómo me llamo?",
            "¿Hace buen tiempo para ir en bicicleta?",
        ],
        "action_key": "assistant",
        "context_info": "El clima actual en Madrid es soleado con 25 grados.",
        "session_id": str(uuid.uuid4()),
    }

    extended = {
        "texts": [
            "¿Que cambios hay en el embarazo?",
            "¿Y que molestias suelen las mas frecuentes?",
        ],
        "action_key": "default",
        "context_info": """{
            "id": "30",
            "raw_text": "2. el embarazo 2.1 un cuerpo que cambia el embarazo es un proceso natural que implica cambios en el cuerpo y en la mente de la mujer. el cuerpo va a cambiar para adaptarse al bebé que crece, asegurando su desarrollo y maduración durante nueve meses, al mismo tiempo que se prepara para la lactancia. uno de los primeros cambios que se puede observar es un aumento de la pigmentación de la piel. también aumenta el tamaño de las mamas y de los pezones que se vuelven más sensibles y se oscurecen más que la areola que los rodea. otros cambios que se pueden producir son, el aumento de la temperatura corporal que suele ser algo más alta de lo habitual, la sensación de mayor fatiga y más sueño. puede aumentar la sensibilidad a los olores, aparecer nauseas y molestias al hacer la digestión. también puede aumentar la frecuencia y las ganas de orinar, y producirse cierto estreñimiento. estas molestias son debidas a cambios hormonales y al desplazamiento que sufren los órganos a medida que crece el feto en el útero. además de estos cambios físicos, durante el embarazo también hay cambios en las emociones y en el estado de ánimo. se suceden sensaciones positivas de alegría y satisfacción que se van alternando con sentimientos de duda, miedo, inseguridad y preocupación por el desarrollo del feto, el parto y la nueva etapa que llegará tras él. consultar con el personal sanitario que realiza el seguimiento del embarazo, puede ayudar a sobrellevar mejor estas incertidumbres. además de los autocuidados durante el embarazo, el parto y el postparto, la mujer requiere atención y cuidados del personal sanitario, de la familia y de las personas de su entorno.",
            "page_number": 4,
            "raw_text_ACR": [
                "[('CPU', 'unidad central de procesamiento'), ('DNA', 'ácido desoxirribonucleico')]"
            ],
            "creator": "Adobe InDesign CS5 (7.0)",
            "file_path": "data/repo/BVCM017286.pdf",
            "title": "BVCM017286_Para una maternidad saludable. Nueve meses para compartir. Edición actualizada 2012",
            "score": 0.85018337,
        },""",
        "session_id": str(uuid.uuid4()),
    }

    basic = {
        "texts": [
            "¿Cuál es la capital de Francia?",
            "¿Cuantos ciudadanos tiene Madrid capital?",
        ],
        "action_key": "sparql_query",
    }

    calls = [assistant, extended, basic]

    for call in calls:
        for text in call["texts"]:
            client = LLMStreamingClient(base_url, timeout)
            client.send_messages_via_socket(
                text=text,
                on_token=token_printer,
                session_id=call.get("session_id", None),
                action_key=call["action_key"],
                context_info=call.get("context_info", None),
            )
