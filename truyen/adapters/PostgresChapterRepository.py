from sqlalchemy.orm import Session
from core.models import Chapter
from ports.ChapterRepository import ChapterRepository
from typing import List

class PostgresChapterRepository(ChapterRepository):
    def __init__(self, session: Session):
        self.session = session

    def create_chapter(self, chapter: Chapter) -> Chapter:
        self.session.add(chapter)
        self.session.commit()
        return chapter

    def read_chapter_by_id(self, chapter_id: int) -> Chapter:
        return self.session.query(Chapter).filter(Chapter.id == chapter_id).first()

    def read_chapters_of_story(self, story_id: int) -> List[Chapter]:
        return self.session.query(Chapter).filter(Chapter.story_id == story_id).all()

    def update_chapter(self, chapter_id: int, updated_chapter: Chapter) -> Chapter:
        exist_chapter = self.session.query(Chapter).filter(Chapter.id == chapter_id).first()
        if exist_chapter:
            existing_chapter.title = updated_chapter.title
            existing_chapter.content = updated_chapter.content

            self.session.commit()
        return existing_chapter

    def delete_chapter(self, chapter_id: int):
        self.session.query(Chapter).filter(Chapter.id == chapter_id).delete()
        self.session.commit()
