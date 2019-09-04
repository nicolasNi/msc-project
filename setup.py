from setuptools import setup, find_packages
import io
import os

install_requires = [
    "rasa==1.0.9",
    "mailchimp3~=3.0.2",
    "oauth2client~=4.1.2",
    "gspread~=3.0.0",
    "beautifulsoup4~=4.6.3",
    "requests~=2.21.0",
    "geopy~=1.18.1",
    "pandas~=0.24.1",
]

extras_requires = {
    'spacy': ["scikit-learn",
              "sklearn-crfsuite",
              "scipy",
              "spacy>2.0",
              ],
    'tensorflow': ["scikit-learn",
                   "tensorflow",
                   ]
}

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="Msc project Chatbot",
    classifiers=[
        "Development Status :: 4 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        # supported python versions
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    packages=find_packages(),
    version="1.1",
    install_requires=install_requires,
    description="Msc project Chatbot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Kaihua Ni",
    author_email="ml17kn@leeds.ac.uk",
    maintainer="Kaihua Ni",
    maintainer_email="ml17kn@leeds.ac.uk",
    license="GNU General Public License v3.0",
    url="https://github.com/nicolasNi/msc-project",
    download_url="https://github.com/nicolasNi/msc-project/archive/master.zip",
    project_urls={
        "Source": "https://github.com/nicolasNi/msc-project",
    },
)
