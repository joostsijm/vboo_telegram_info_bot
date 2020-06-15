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
    return formatted_article

def abbreviate(string, max_lenght):
    """Abriviate string to only first letters"""
    if len(string) <= max_lenght:
        return string
    abbreviation = ''
    for word in string.split(' '):
        abbreviation += word[0:1].upper()
    return abbreviation

def format_state_region(side):
    """Format state and region name"""
    state = '*[{}](https://m.rivalregions.com/#state/details/{})*'.format(
        abbreviate(side['state_name'], 4),
        side['state_id'],
    )
    region = '[{}](http://m.rivalregions.com/#map/details/{})'.format(
        side['region_name'],
        side['region_id'],
    )
    return '{} {}'.format(state, region)

def roundk(integer):
    """Round down number"""
    thousand = 1
    while integer >= 999:
        thousand += 1
        decimal = str(integer)[-3:-2]
        integer = int(str(integer)[:-3])
    return '{}\\.{}{}'.format(integer, decimal, 'k' * thousand)


def telegram_format_war(war):
    """Format war object for article"""
    if 'region_name' in war['attack']:
        title = '{} vs {}'.format(
            format_state_region(war['attack']),
            format_state_region(war['defend'])
        )
    else:
        title = '{} vs {}'.format(
            '*{}*'.format(war['type']),
            format_state_region(war['defend'])
        )
    damage = '{} *vs* {} \\= {}'.format(
        roundk(war['attack']['damage']),
        roundk(war['defend']['damage']),
        roundk(war['damage']),
    )

    link = '{} \\| {}'.format(
        '[mobile](https://m.rivalregions.com/#war/details/{})'.format(war['war_id']),
        '[desktop](http://rivalregions.com/#war/details/{})'.format(war['war_id']),
    )

    formatted_war = '\n'.join([
        title,
        damage,
        'finish: {} UTC'.format(escape_markdown(war['finish_date'].strftime('%Y-%m-%d %H:%M'), 2)),
        'time left: {}'.format(escape_markdown(str(war['time_left']))),
        link,
    ])
    return formatted_war
