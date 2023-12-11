# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from collections import OrderedDict
import scrapy


class ProblemItem(scrapy.Item):
    problem_id = scrapy.Field()
    problem_title = scrapy.Field()
    problem_info = scrapy.Field()
    problem_answer_num = scrapy.Field()
    problem_submit_num = scrapy.Field()
    problem_answer_rate = scrapy.Field()


class UserItem(scrapy.Item):
    user_rank = scrapy.Field()
    user_id = scrapy.Field()
    status_message = scrapy.Field()
    user_answer_num = scrapy.Field()
    user_submit_num = scrapy.Field()
    user_answer_rate = scrapy.Field()

    def __init__(self, *args, **kwargs):
        super(UserItem, self).__init__(*args, **kwargs)
        self._values = OrderedDict()


class WorkbookItem(scrapy.Item):
    workbook_rank = scrapy.Field()
    workbook_id = scrapy.Field()
    user_id = scrapy.Field()
    workbook_title = scrapy.Field()
    problem_id = scrapy.Field()
    problem_title = scrapy.Field()

    def __init__(self, *args, **kwargs):
        super(WorkbookItem, self).__init__(*args, **kwargs)
        self._values = OrderedDict()


class ProblemDetailItem(scrapy.Item):
    problem_id = scrapy.Field()
    problem_title = scrapy.Field()
    problem_lang = scrapy.Field()
    tag_display_lang = scrapy.Field()
    tag_name = scrapy.Field()
    problem_titles_isOriginal = scrapy.Field()
    problem_isSolvable = scrapy.Field()
    problem_isPartial = scrapy.Field()
    problem_answer_num = scrapy.Field()
    problem_level = scrapy.Field()
    problem_votedUserCount = scrapy.Field()
    problem_sprout = scrapy.Field()
    problem_givesNoRating = scrapy.Field()
    problem_isLevelLocked = scrapy.Field()
    problem_averageTries = scrapy.Field()
    problem_official = scrapy.Field()
    tag_key = scrapy.Field()