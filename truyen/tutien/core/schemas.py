from pydantic import BaseModel
from typing import Optional

class StorySchema(BaseModel):
    id: int
    title: str
    description: str
    author: str
    # Add other fields as necessary

class ChapterSchema(BaseModel):
    id: int
    story_id: int
    title: str
    content: Optional[str] = None
