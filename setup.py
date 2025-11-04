import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "end-to-end-ml-project"
AUTHOR_USER_NAME = "Deep401899"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "deeppaul3538@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,  # Fixed: was author_name
    description="A SMALL PYTHON PACKAGE FOR ML APP",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Fixed: was content
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    # Add your dependencies here if needed, but make sure they're valid packages
    install_requires=[
        # Remove any reference to 'puccinialin' here
        # Add only valid package names from your requirements.txt if needed
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

# import setuptools

# with open("README.md","r",encoding="utf-8") as f:
#     long_description = f.read()
    
    
# __version__="0.0.0"

# REPO_NAME="end-to-end-ml-project"
# AUTHOR_USER_NAME="Deep401899"
# SRC_REPO="mlProject"
# AUTHOR_EMAIL="deeppaul3538@gmail.com"


# setuptools.setup(
#     name=SRC_REPO,
#     version=__version__,
#     author=AUTHOR_USER_NAME,
#     author_name=AUTHOR_EMAIL,
#     description="A SMALL PYTHON PACKAGE FOR ML APP",
#     long_description=long_description,
#     long_description_content="text/markdown",
#     url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
#     project_urls={
#         "Bug tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
#     },
#     package_dir={"":"src"},
#     packages=setuptools.find_packages(where="src")
# )

