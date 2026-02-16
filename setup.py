from setuptools import setup, find_packages

setup(
    name="telegram-downloader",
    version="3.5.0",
    author="Aviel.AI",
    description="Professional Telegram media downloader with PyQt6 UI",
    packages=find_packages(),
    install_requires=[
        "PyQt6>=6.4.0",
        "telethon>=1.34.0",
        "cryptg>=0.4.0",
        "humanize>=4.0.0"
    ],
    python_requires=">=3.8",
)
