"""Setup file"""

import setuptools

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="vboo_info_bot",
    version="0.0.1",
    author="Joost Sijm",
    author_email="joostsijm@gmail.com",
    description="VBOO Telegram info bot for Rival Regions",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="gogs@git.craftbroec.nl:joostsijm/vboo_info_bot.git",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': ['vboo-info-bot=vboo_info_bot.__main__:main'],
    },
    install_requires=[
        "python-telegram-bot",
        "python-dotenv",
        "hyperlink",
        "rival-regions-wrapper",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
