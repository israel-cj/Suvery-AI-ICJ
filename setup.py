from setuptools import setup, find_packages

setup(
    name="Survey AI-ICJ",
    version="0.0.1",
    packages=find_packages(),
    description="Create a suvery paper based on LLM",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Israel Campero Jurado",
    author_email="learsi1911@gmail.com",
    url="https://github.com/israel-cj/Suvery-AI-ICJ.git",
    python_requires=">=3.10",
    install_requires=[
        "openai",
    ],
)

