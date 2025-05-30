"""Cloudsmith Command Line Interface (CLI)."""

import os

from setuptools import find_packages, setup


def get_root_path():
    """Get the root path for the application."""
    root_path = __file__
    return os.path.dirname(os.path.realpath(root_path))


def read(path, root_path=None):
    """Read the specific file into a string in its entirety."""
    try:
        root_path = root_path or get_root_path()
        real_path = os.path.realpath(os.path.join(root_path, path))
        with open(real_path) as fp:
            return fp.read().strip()
    except OSError:
        return ""


def get_long_description():
    """Grok the readme, turn it into whine (rst)."""
    root_path = get_root_path()
    readme_path = os.path.join(root_path, "README.md")
    with open(readme_path) as fp:
        return fp.read()


setup(
    name="cloudsmith-cli",
    version=read("VERSION"),
    url="https://github.com/cloudsmith-io/cloudsmith-cli",
    license="Apache License 2.0",
    author="Cloudsmith Ltd",
    author_email="support@cloudsmith.io",
    description="Cloudsmith Command-Line Interface (CLI)",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests"]),
    package_data={
        "cloudsmith_cli": ["cloudsmith_cli/data/*", "cloudsmith_cli/templates/*"]
    },
    include_package_data=True,
    zip_safe=False,
    platforms=["any"],
    python_requires=">=3.9.0",
    install_requires=[
        "click>=7.0,!=8.0.2",
        "click-configfile>=0.2.3",
        "click-didyoumean>=0.0.3",
        "click-spinner>=0.1.7",
        "cloudsmith-api>=2.0.18,<3.0",  # Compatible upto (but excluding) 3.0+
        "keyring>=25.4.1",
        "requests>=2.18.4",
        "requests_toolbelt>=0.8.0",
        "semver>=2.7.9",
        "urllib3<2.0",
    ],
    entry_points={
        "console_scripts": ["cloudsmith=cloudsmith_cli.cli.commands.main:main"]
    },
    keywords=["cloudsmith", "cli", "devops"],
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        "Development Status :: 5 - Production/Stable",
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Internet",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
)
