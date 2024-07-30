from setuptools import find_packages,setup

setup(
    name="mcqgenerator",
    version='0.0.1',
    author='fyaaaz',
    author_email='fyaazbobat@homtail.com',
    install_requires=["openai","langchain_community","langchain","steamlit","python=dotenv","PyPDF2"],
    packages=find_packages()
)