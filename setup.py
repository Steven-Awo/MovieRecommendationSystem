from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR1_NAME = 'ROTIMI OLAKUNLE AWOMODU'
AUTHOR2_NAME = 'MARTINS OKWUAKU'

SRC_REPO = 'src'

LIST_OF_ALL_REQUIREMENTS = ['streamlit']

setup(
    name=SRC_REPO,
    version='0.0.2',
    author=AUTHOR1_NAME + " and " + AUTHOR2_NAME,
    author_email='rotimiawomodu@gmail.com, martinsobinna9@gmail.com',
    description='A simple web application for a Movie Recommendation System',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    python_requires='>=3.11.5',
    install_requires=LIST_OF_ALL_REQUIREMENTS
)
