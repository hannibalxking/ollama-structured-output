"""
Pets management example using structured output from Ollama.
"""
from ollama import chat
from .models import Pet, PetList
from rich import print

def get_pets_list(description: str) -> PetList:
    """
    Extract structured pet information from a description using Ollama.
    """
    response = chat(
        messages=[
            {"role": "user", "content": description}
        ],
        model="llama3.2",
        format=PetList.model_json_schema(),
    )
    pets = PetList.model_validate_json(response.message.content)
    return pets

if __name__ == "__main__":
    description = (
        "I have two pets. A cat named Luna who is 5 years old and loves playing with yarn. "
        "She has grey fur. I also have a 2 year old black cat named Loki who loves tennis balls."
    )
    pets = get_pets_list(description)
    print(pets.json(indent=2))