import re
from setuptools import setup


def get_version():
    with open('iterpipe/__init__.py', "r") as vfh:
        vline = vfh.read()
    vregex = r"^__version__ = ['\"]([^'\"]*)['\"]"
    match = re.search(vregex, vline, re.M)
    if match:
        return match.group(1)
    else:
        raise RuntimeError("Unable to find version string in __init__")


setup(
    name="iterpipe",
    version=get_version(),
    author="Matthew Perry",
    author_email="perrygeo@gmail.com",
    description="iterpipe",
    license="BSD",
    keywords="parallel multiprocessing functional",
    url="https://github.com/perrygeo/iterpipe",
    package_dir={'': '.'},
    packages=['iterpipe'],
    long_description="compose pipeline of functions to apply to iterables",
    install_requires=[],
    tests_require=['pytest', 'pytest-cov'],
    classifiers=[
        "Development Status :: 4 - Beta",
        'Intended Audience :: Developers',
        "License :: OSI Approved :: BSD License",
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        "Topic :: Utilities"])
