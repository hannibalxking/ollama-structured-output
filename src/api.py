"""
Flask API providing structured pet management endpoints using Ollama and Pydantic.
"""
import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from functools import wraps
from dotenv import load_dotenv
from .models import Pet, PetList
from ollama import chat

# Load environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
CORS(app)

# In-memory storage for pets
pet_database = []

def handle_errors(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return decorated_function

@app.route('/pets', methods=['POST', 'OPTIONS'])
@handle_errors
def add_pet():
    if request.method == 'OPTIONS':
        return '', 204
    data = request.json
    description = data.get('description', '')
    # Use Ollama to extract structured pet data
    response = chat(
        messages=[{'role': 'user', 'content': f'Extract pet information from this text: {description}'}],
        model='llama3.2',
        format=Pet.model_json_schema()
    )
    pet_data = json.loads(response.message.content)
    pet = Pet(**pet_data)
    pet_database.append(pet.model_dump())
    return jsonify(pet.model_dump()), 201

@app.route('/pets', methods=['GET'])
@handle_errors
def get_pets():
    animal_type = request.args.get('animal')
    min_age = request.args.get('min_age', type=int)
    filtered = pet_database
    if animal_type:
        filtered = [p for p in filtered if p['animal'].lower() == animal_type.lower()]
    if min_age is not None:
        filtered = [p for p in filtered if p['age'] >= min_age]
    return jsonify(PetList(pets=filtered).model_dump())

@app.route('/pets/<pet_name>', methods=['GET', 'PUT', 'DELETE', 'OPTIONS'])
@handle_errors
def manage_pet(pet_name):
    if request.method == 'OPTIONS':
        return '', 204
    index = next((i for i, p in enumerate(pet_database) if p['name'].lower() == pet_name.lower()), None)
    if index is None:
        return jsonify({'error': 'Pet not found'}), 404
    if request.method == 'GET':
        return jsonify(pet_database[index])
    elif request.method == 'PUT':
        data = request.json
        description = data.get('description', '')
        response = chat(
            messages=[{'role': 'user', 'content': f'Extract updated pet information from this text: {description}'}],
            model='llama3.2',
            format=Pet.model_json_schema()
        )
        updated_data = json.loads(response.message.content)
        pet = Pet(**updated_data)
        pet_database[index] = pet.model_dump()
        return jsonify(pet.model_dump())
    else:  # DELETE
        deleted = pet_database.pop(index)
        return jsonify(deleted)

@app.route('/analyze', methods=['POST', 'OPTIONS'])
@handle_errors
def analyze_pets():
    if request.method == 'OPTIONS':
        return '', 204
    data = request.json
    description = data.get('description', '')
    response = chat(
        messages=[{'role': 'user', 'content': f'Extract information about all pets from this text: {description}'}],
        model='llama3.2',
        format=PetList.model_json_schema()
    )
    pets_data = json.loads(response.message.content)
    pet_list = PetList(**pets_data)
    return jsonify(pet_list.model_dump())

if __name__ == '__main__':
    app.run(debug=True)
