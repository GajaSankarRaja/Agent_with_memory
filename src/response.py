from pydantic import BaseModel, Field
from typing import Optional

class ModelResponse(BaseModel):
    text : str = Field(description="Model response")

