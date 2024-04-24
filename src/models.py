"""
Data models for structured output using Pydantic.
"""
from pydantic import BaseModel
from typing import List, Optional

class Country(BaseModel):
    name: str
    capital: str
    languages: List[str]

class Pet(BaseModel):
    name: str
    animal: str
    age: int
    color: Optional[str] = None
    favorite_toy: Optional[str] = None

class PetList(BaseModel):
    pets: List[Pet]

class PetDescription(BaseModel):
    description: str
    extracted_info: Pet
