from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Story(Base):
    __tablename__ = 'story'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)

    chapters = relationship("Chapter", back_populates="story")


class Chapter(Base):
    __tablename__ = 'chapter'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    content = Column(String(255), nullable=False)
    story_id = Column(Integer, ForeignKey('story.id'), nullable=False)
    
    story = relationship("Story", back_populates="chapters")

