import scrapy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from ..items import TutienItem, StoryItem, ChapterItem
from slugify import slugify
from core import models

class MySpider(scrapy.Spider):
    name = 'hehe'
    start_urls = [
        'https://truyen.tangthuvien.vn/doc-truyen/dai-phung-da-canh-nhan',
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        engine = create_engine('postgresql://postgres:thanhnhan1911@localhost:5432/nhon')
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def parse(self, response):
        story_item = StoryItem()
        story_item['title'] = response.css('h1::text').extract()
        author_info = response.css('.author-photo')

        # Extract author name and profile URL
        story_item['author'] = author_info.css('p a::text').get()
        description = response.css('.Story-intro p::text').getall()
        story_item['description'] = ' '.join(description).strip()

        story_item['code'] = slugify(response.url.split('/')[-1])

        yield story_item

        # Extract chapter titles and content
        all_chapters = response.css('ul.cf li a')

        for chapter in all_chapters:
            chapter_url = chapter.css('::attr(href)').extract_first()

            yield scrapy.Request(chapter_url, callback=self.parse_chapter)

    def parse_chapter(self, response):
        story = self.get_story_by_code('dai-phung-da-canh-nhan')

        chapter_item = ChapterItem()
        chapter_item['title'] = response.css('h5 a::text').get()

        chapter_item['content'] = " ".join(response.css('.box-chap::text').extract())
        chapter_item['story_id'] = story.id
        print("alskjfffffffffalkffff", story.id)
        yield chapter_item

    
    def get_story_by_code(self, code):
        return self.session.query(models.Story).filter(models.Story.code == code).first()