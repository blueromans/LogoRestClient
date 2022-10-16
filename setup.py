import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='LogoRestClient',
    version="0.0.1",
    author="Yaşar Özyurt",
    author_email="blueromans@gmail.com",
    description='Logo Rest Client Python package',
    long_description='Logo Rest Client Python package',
    url='https://github.com/BufiCoresite/LogoRest.git',
    project_urls={
        "Bug Tracker": "https://github.com/BufiCoresite/LogoRest/issues",
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
