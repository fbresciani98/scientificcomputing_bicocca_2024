from setuptools import setup, find_packages

setup(
    name="mypackage-francesca-test",  # nome unico su Test PyPI
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Francesca",
    description="Pacchetto di esempio",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.8"
)

