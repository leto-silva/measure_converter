from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="measure_converter",
    version="0.0.1",
    author="Wellington",
    author_email="wellingtoneugenio@gmail.com",
    description="Teste cricao package",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leto-silva/measure_converter.git"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=2.8',
)