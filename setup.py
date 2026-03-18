from setuptools import setup
import site, sys
import pathlib

site.ENABLE_USER_SITE = "--user" in sys.argv[1:]

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="gitex",
    version="0.0.2",
    description="This package adds 'definetly useful' new git subcommands to your system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/reon04/gitex",
    author="reon04",
    author_email="larsmichels04@gmail.com",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14'
    ],
    packages=["gitex"],
    license="MIT",
    python_requires=">=3.8, <4",
    install_requires=[],
    entry_points={
        "console_scripts": ["git-yeet=gitex:yeet"]
    }
)