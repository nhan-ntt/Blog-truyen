from fastapi import FastAPI, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

from core.schemas import Story, Chapter
from adapters.PostgresStoryRepository import PostgresStoryRepository 
from adapters.PostgresChapterRepository import PostgresChapterRepository

DATABASE_URL = "postgresql://postgres:admin@localhost:5432/nhon"
Base = declarative_base()

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Sessionlocal = sessionmaker(bind=engine)

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

# Dependency to get the story repository
def get_story_repository(db: Session = Depends(get_db)):
    return PostgresStoryRepository(db)

# Dependency to get the chapter repository
def get_chapter_repository(db: Session = Depends(get_db)):
    return PostgresChapterRepository(db)

# API routes for Story
@app.post("/stories/", response_model=Story)
def create_story(story: Story, story_repo: PostgresStoryRepository = Depends(get_story_repository)):
    return story_repo.create_story(story)

@app.get("/stories/{story_id}", response_model=Story)
def read_story(story_id: int, story_repo: PostgresStoryRepository = Depends(get_story_repository)):
    return story_repo.read_story_by_id(story_id)

@app.get("/stories/", response_model=list)
def read_all_stories(story_repo: PostgresStoryRepository = Depends(get_story_repository)):
    return story_repo.read_all_stories()

@app.put("/stories/{story_id}", response_model=Story)
def update_story(story_id: int, updated_story: Story, story_repo: PostgresStoryRepository = Depends(get_story_repository)):
    return story_repo.update_story(story_id, updated_story)

@app.delete("/stories/{story_id}")
def delete_story(story_id: int, story_repo: PostgresStoryRepository = Depends(get_story_repository)):
    story_repo.delete_story(story_id)
    return {"message": "Story deleted successfully"}

# API routes for Chapter
@app.post("/chapters/", response_model=Chapter)
def create_chapter(chapter: Chapter, chapter_repo: PostgresChapterRepository = Depends(get_chapter_repository)):
    return chapter_repo.create_chapter(chapter)

@app.get("/chapters/{chapter_id}", response_model=Chapter)
def read_chapter(chapter_id: int, chapter_repo: PostgresChapterRepository = Depends(get_chapter_repository)):
    return chapter_repo.read_chapter_by_id(chapter_id)

@app.get("/chapters/story/{story_id}", response_model=list)
def read_chapters_of_story(story_id: int, chapter_repo: PostgresChapterRepository = Depends(get_chapter_repository)):
    return chapter_repo.read_chapters_of_story(story_id)

@app.put("/chapters/{chapter_id}", response_model=Chapter)
def update_chapter(chapter_id: int, updated_chapter: Chapter, chapter_repo: PostgresChapterRepository = Depends(get_chapter_repository)):
    return chapter_repo.update_chapter(updated_chapter)

@app.delete("/chapters/{chapter_id}")
def delete_chapter(chapter_id: int, chapter_repo: PostgresChapterRepository = Depends(get_chapter_repository)):
    chapter_repo.delete_chapter(chapter_id)
    return {"message": "Chapter deleted successfully"}