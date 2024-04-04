
import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent.resolve()

PACKAGE_NAME = "techbyai"
AUTHOR = "Shaked Zychlinski"
AUTHOR_EMAIL = "shakedzy@gmail.com"
URL = f"http://shakedzy.xyz/{PACKAGE_NAME}"
DOWNLOAD_URL = f"https://pypi.org/project/{PACKAGE_NAME}/"

LICENSE = "CC BY-NC 4.0"
VERSION = (HERE / "VERSION").read_text(encoding="utf8").strip()
DESCRIPTION = "Tech new by AI"
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding="utf8")
LONG_DESC_TYPE = "text/markdown"

requirements = (HERE / "requirements.txt").read_text(encoding="utf8")
INSTALL_REQUIRES = [s.strip() for s in requirements.split("\n")]

MIN_PYTHON_MINOR = 11
MAX_PYTHON_MINOR = 12
CLASSIFIERS = [
    f"Programming Language :: Python :: 3.{str(v)}" for v in range(MIN_PYTHON_MINOR, MAX_PYTHON_MINOR+1)
]
PYTHON_REQUIRES = f">=3.{str(MIN_PYTHON_MINOR)}"

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    license=LICENSE,
    author_email=AUTHOR_EMAIL,
    url=URL,
    download_url=DOWNLOAD_URL,
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(),
    classifiers=CLASSIFIERS,
    package_data={
        PACKAGE_NAME: ['resources/*'],  
    },
    entry_points={
        'console_scripts': [
            f'run_routine = {PACKAGE_NAME}:main'
        ]
    }
)