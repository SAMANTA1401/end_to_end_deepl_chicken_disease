import setuptools

with open('README.md', "r", encoding="utf-8") as f:
    long_description = f.read()


__versio__ = "0.0.0"

REPO_NAME = "end_to_end_deepl_chicken_disease"
AUTHOR_USER_NAME = "SAMANTA1401"
SRC_REPO = "cnnClassifier"

setuptools.setup(
    name=SRC_REPO,
    version=__versio__,
    author=AUTHOR_USER_NAME,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
