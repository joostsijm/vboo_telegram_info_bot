"""Common functions"""

from telegram.utils.helpers import escape_markdown


def telegram_format_article(article):
    """Format article object for telegram"""
    title = '*[{}](https://m.rivalregions.com/#news/show/{})*'.format(
        article['article_title'],
        article['article_id'],
    )
    author = '[{}](https://m.rivalregions.com/#slide/profile/{})'.format(
        article['author_name'],
        article['author_id'],
    )
    formatted_article = '{} by: {}\n_{}_'.format(
        title,
        author,
        escape_markdown(article['content_text'][0:144].strip(), 2),
    )
    return formatted_article
