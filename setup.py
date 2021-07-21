from setuptools import setup

setup(
    name="itchio",
    version="0.1",
    description="Interact with the REST-api of itch.io",
    license="MIT",
    author="Johannes Pour",
    url="https://github.com/Tch1b0/itchio-lib",
    author_email="Johannes@ben11.de",
    packages=["itchio"],
    package_requires=["requests==2.25.1"]
)