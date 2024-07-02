from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    a_long_descript = fh.read()

AURTHOR1_NAMES = 'ROTIMI OLAKUNLE AWOMODU'

AURTHOR2_NAMES = 'MARTINS OKWUAKU'

SCR_REPO = 'src'

LIST_OF_ALL_REQUIREMENTS = ['sreamlit']

setup(
    name = SCR_REPO,
    version = '0.0.2',
    authors = AURTHOR1_NAMES + " " + AURTHOR2_NAMES,
    aurthors_email = 'rotimiawomodu@gmail.com' + ", " + 'martinsobinna9@gmail.com',
    descriptions = 'A simle web application for a Movie Recommendation System',
    a_long_description = a_long_descript,
    description_type_of_content = 'text/markdown',
    package = [SCR_REPO]
    p
)