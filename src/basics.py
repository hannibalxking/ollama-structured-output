"""
Basic example of structured output with Ollama.
"""
from ollama import chat
from .models import Country

def get_country_info(country_name: str) -> Country:
    """
    Fetch structured country information using Ollama.
    """
    response = chat(
        messages=[{"role": "user", "content": f"Tell me about {country_name}."}],
        model="llama3.2",
        format=Country.model_json_schema(),
    )
    country = Country.model_validate_json(response.message.content)
    return country

if __name__ == "__main__":
    country = get_country_info("Canada")
    print(country.json(indent=2))