from setuptools import setup
from setuptools import setup, find_packages

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read()

with open('README.rst') as readme_file:
    README = readme_file.read()

setup(
    name="pyinstaller_scripts_runner",
    version="0.0.1",
    description="pyinstaller_scripts_runner",
    long_description=README,
    long_description_content_type="text/markdown",
    url="",
    author="Klajdi Beqiraj, Marco Sanguineti",
    author_email="",
    license="MIT",
    classifiers=[],
    packages=["pyinstaller_scripts_runner"],
    include_package_data=True,
    install_requires=requirements,
    entry_points={"console_scripts": ["mechopt=pyinstaller_scripts_runner.__main__:main"]},
)