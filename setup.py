import setuptools

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name='LogoRestClient',
    version="0.0.6",
    author="Yaşar Özyurt",
    author_email="blueromans@gmail.com",
    description='Logo Rest Client Python package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/blueromans/LogoRestClient.git',
    project_urls={
        "Bug Tracker": "https://github.com/blueromans/LogoRestClient/issues",
    },
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['logorestclient.service', 'logorestclient.helper', 'logorestclient'],
    python_requires=">=3.6",
)
