import setuptools

# Reading the contents of the README.md file
with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.1"
REPO_NAME = "Text-Summarization_EndToEnd"
SRC_REPO = "textSummarizer"
AUTHOR_NAME = "HasancanCakicioglu"
AUTHOR_EMAIL = "hckecommerce@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarization End to End",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"",
    project_urls={
        "Bug Tracker": "https://github.com/HasancanCakicioglu/Text-Summarization_EndToEnd/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)

