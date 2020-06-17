"""Wrapper test"""

from rival_regions_wrapper.api_wrapper import Article, War
from telegram import ParseMode
import pytest

from vboo_info_bot import functions


@pytest.fixture
def article_keys():
    """Standard key fro article"""
    return ['article_id', 'article_title', 'newspaper_id', 'newspaper_name', \
        'author_name', 'author_id', 'region_name', 'region_id', 'content_text', 'content_html', \
        'language']

@pytest.mark.vcr()
def test_article_info_one(api_wrapper, article_keys):
    """Test article info"""
    article_id = 2708696
    response = Article(api_wrapper).info(article_id)

    assert isinstance(response, dict), "The resonse should be a dict"
    assert set(article_keys).issubset(response.keys()), "All keys should be in the response"
    assert isinstance(response['article_id'], int), "Article id should be an integer"
    assert isinstance(response['article_title'], str), "Article title should be a str"
    assert isinstance(response['newspaper_id'], int), "Newspaper id should be an integer"
    assert isinstance(response['newspaper_name'], str), "Newspaper name should be a string"
    assert isinstance(response['author_name'], str), "Author name should be a string"
    assert isinstance(response['author_id'], int), "Author id should be an integer"
    assert isinstance(response['region_name'], str), "Region name should be a string"
    assert isinstance(response['region_id'], int), "Region id should be an integer"
    assert isinstance(response['content_text'], str), "Content text should be a string"
    assert isinstance(response['content_html'], str), "Content html should be a string"
    assert isinstance(response['language'], str), "Language should be a string"
    assert isinstance(response['content_html'], str), "Content html should be a string"
    assert isinstance(response['language'], str), "Language should be a string"
    assert isinstance(response['rating'], int), "Rating should be an integer"

@pytest.mark.vcr()
def test_article_info_two(api_wrapper, article_keys):
    """Test article info"""
    article_id = 2862982
    response = Article(api_wrapper).info(article_id)

    assert isinstance(response, dict), "The resonse should be a dict"
    assert set(article_keys).issubset(response.keys()), "All keys should be in the response"
    assert isinstance(response['article_id'], int), "Article id should be an integer"
    assert isinstance(response['article_title'], str), "Article title should be a str"
    assert response['newspaper_id'] is None, "Newspaper id should be none"
    assert response['newspaper_name'] is None, "Newspaper name should be none"
    assert isinstance(response['author_name'], str), "Author name should be a string"
    assert isinstance(response['author_id'], int), "Author id should be an integer"
    assert isinstance(response['region_name'], str), "Region name should be a string"
    assert isinstance(response['region_id'], int), "Region id should be an integer"
    assert isinstance(response['content_text'], str), "Content text should be a string"
    assert isinstance(response['content_html'], str), "Content html should be a string"
    assert isinstance(response['language'], str), "Language should be a string"
    assert isinstance(response['content_html'], str), "Content html should be a string"
    assert isinstance(response['language'], str), "Language should be a string"
    assert isinstance(response['rating'], int), "Rating should be an integer"

@pytest.mark.message
@pytest.mark.vcr()
def test_send_article_message(api_wrapper, telegram_bot, telegram_channel):
    """Test format war"""
    article_id = 2867567
    response = Article(api_wrapper).info(article_id)

    assert isinstance(response, dict), "The response should be a dict"
    formatted_article = functions.telegram_format_article(response)
    if telegram_channel:
        telegram_bot.sendMessage(
            telegram_channel,
            formatted_article,
            parse_mode=ParseMode.MARKDOWN_V2
        )

@pytest.mark.message
@pytest.mark.vcr()
def test_send_war_ground_message(api_wrapper, telegram_bot, telegram_channel):
    """Test format war"""
    war_id = 329541
    response = War(api_wrapper).info(war_id)

    assert isinstance(response, dict), "The response should be a dict"
    formatted_war = functions.telegram_format_war(response)
    if telegram_channel:
        telegram_bot.sendMessage(telegram_channel, formatted_war, parse_mode=ParseMode.MARKDOWN_V2)

@pytest.mark.message
@pytest.mark.vcr()
def test_send_war_coup_message(api_wrapper, telegram_bot, telegram_channel):
    """Test format war"""
    war_id = 329518
    response = War(api_wrapper).info(war_id)

    assert isinstance(response, dict), "The response should be a dict"
    formatted_war = functions.telegram_format_war(response)
    if telegram_channel:
        telegram_bot.sendMessage(telegram_channel, formatted_war, parse_mode=ParseMode.MARKDOWN_V2)
