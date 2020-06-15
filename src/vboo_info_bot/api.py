"""API function"""


from rival_regions_wrapper.api_wrapper import Article, War

from vboo_info_bot import API_WRAPPER

def get_article(article_id):
    """Get article by id"""
    return Article(API_WRAPPER).info(article_id)

def get_war(war_id):
    """Get war by id"""
    return War(API_WRAPPER).info(war_id)
