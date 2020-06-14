"""VBOO Info Bot"""

from vboo_info_bot import LOGGER, telegram_bot


def main():
    """Main function"""
    LOGGER.info('Starting application')
    telegram_bot.run()

if __name__ == '__main__':
    main()
