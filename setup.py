from setuptools import setup

setup(
    name="itchio",
    version="1.1.0",
    description="Interact with the REST-API of itch.io",
    long_description=open("./README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    author="Johannes Pour",
    url="https://github.com/Tch1b0/itchio-lib",
    author_email="Johannes@ben11.de",
    packages=["itchio"],
    install_requires=["requests==2.25.1"]
)