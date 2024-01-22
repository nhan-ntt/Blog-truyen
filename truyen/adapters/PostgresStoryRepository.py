from sqlalchemy.orm import Session
from core.models import Story
from typing import List
from ports.StoryRepository import StoryRepository

class PostgresStoryRepository(StoryRepository):
    def __init__(self, session: Session):
        self.session = session

    def create_story(self, story: Story) -> Story:
        self.session.add(story)
        self.session.commit()
        return story

    def read_story_by_id(self, story_id: int) -> Story:
        return self.session.query(Story).filter(Story.id == story_id).first()

    def read_all_stories(self) -> List[Story]:
        return self.session.query(Story).all()

    def update_story(self, story_id: int, updated_story: Story) -> Story:
        exist_story = self.session.query(Story).filter(Story.id == story_id).first()
        if exist_story:
            existing_story.title = updated_story.title
            existing_story.description = updated_story.description
            existing_story.author = updated_story.author

            self.session.commit()
        return existing_story

    def delete_story(self, story_id: int):
        self.session.query(Story).filter(Story.id == story_id).delete()
        self.session.commit()

