from sqlalchemy import Column, Integer, String, ForeignKey, Index
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Story(Base):
    __tablename__ = 'story'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    code = Column(String(255), nullable=False, unique=True)

    chapters = relationship("Chapter", back_populates="story")


class Chapter(Base):
    __tablename__ = 'chapter'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False, index=True)
    content = Column(String(255), nullable=False)
    story_id = Column(Integer, ForeignKey('story.id'), nullable=False, index=True)
    
    story = relationship("Story", back_populates="chapters")
