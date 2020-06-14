"""Common functions"""


def telegram_format_article(article):
    """Format article object for telegram"""
    formatted_article = '*{}* by: {}\n_{}_'.format(
        article['article_title'],
        article['author_name'],
        article['content_text'][0:50],
    )
    return formatted_article
