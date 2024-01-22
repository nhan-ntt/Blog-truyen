from pydantic import BaseModel
from typing import Optional

class Story(BaseModel):
    id: int
    title: str
    author: str
    # Add other fields as necessary

class Chapter(BaseModel):
    id: int
    story_id: int
    title: str
    content: Optional[str] = None
    # Add other fields as necessary