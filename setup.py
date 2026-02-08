from setuptools import setup, find_packages

setup(
    name="telegram-downloader",
    version="2.1.1",
    author="Aviel.AI",
    description="Professional Telegram media downloader with PyQt6 UI",
    packages=find_packages(),
    install_requires=[
        "PyQt6",
        "Telethon",
        "cryptg",
        "humanize"
    ],
    python_requires=">=3.8",
)
