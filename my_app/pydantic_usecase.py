from pydantic import BaseModel, dataclasses, Field


class Agent(BaseModel):
    id: str = Field(
        ...,
        min_length=4,
        max_length=6
    )
    name: str
    description: str
    role: str

input_data = {"id":"11111111111111", "name":"HR Policy", "description":"validates", "role": "take decisions"}

agent_model = Agent(**input_data)

print(agent_model)

