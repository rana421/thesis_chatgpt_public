from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="thesis-chatgpt",
    version="2.0.0",
    author="rana421",
    author_email="u554980e@gmail.com",
    description="Retrieve a paper from the research paper platform, summarize it using ChatGPT, and send it to Skype.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rana421/thesis_chatgpt_public",
    packages=find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    install_requires=requirements,
    python_requires=">=3.6",
)
