from pydantic import BaseModel, dataclasses


class Agent(BaseModel):
    id: str
    name: str
    description: str
    role: str

input_data = {"id":"1", "name":"HR Policy", "description":"validates", "role": "take decisions"}

agent_model = Agent(**input_data)

print(agent_model)

