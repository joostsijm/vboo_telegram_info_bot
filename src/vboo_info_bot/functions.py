"""Common functions"""

from telegram.utils.helpers import escape_markdown


def telegram_format_article(article):
    """Format article object for telegram"""
    title = '*[{}](https://m.rivalregions.com/#news/show/{})*'.format(
        escape_markdown(article['article_title'], 2),
        article['article_id'],
    )
    author = '[{}](https://m.rivalregions.com/#slide/profile/{})'.format(
        escape_markdown(article['author_name'], 2),
        article['author_id'],
    )
    underline = '{}, rating: {}, comments: {}'.format(
        escape_markdown(article['post_date'].strftime('%Y-%m-%d %H:%M'), 2),
        article['rating'],
        article['comments'],
    )
    if article['content_text'].strip():
        article_content = '_{}_'.format(escape_markdown(article['content_text'][0:144].strip(), 2))
    else:
        article_content = ''
    formatted_article = '{} by: {}\n{}\n{}'.format(
        title,
        author,
        underline,
        article_content,
    )
    print(formatted_article)
    return formatted_article
