import os
from typing import Optional
from dotenv import load_dotenv
from pydantic import BaseModel, Field
load_dotenv()

# Model's Configurations:
class ModelConfig(BaseModel):
    LLM : Optional[str] | None = Field(description="Name of the model", default="openai/gpt-oss-120b")
    EMBEDDING_MODEL : Optional[str] | None = Field(description="Embedding model", default="sentence-transformers/all-MiniLM-L6-v2")
    EMBEDDINGS_DIMS : Optional[int] | None = Field(description="Embedding dimensions", default=384)


# Parameter's Configurations:
class ParametersConfig(BaseModel):
    TEMPERATURE : Optional[float] | None = Field(description="Temperature", default=0.4)
    API_KEY : Optional[str] | None = Field(description="API key", default=os.getenv('GROQ_API_KEY'))