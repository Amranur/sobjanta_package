# setup.py

from setuptools import setup, find_packages

setup(
    name="sobjanta",  # Replace with your package name
    version="0.1.0",
    description="A FastAPI package for handling search queries with API keys",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/your_package_name",  # Replace with your GitHub URL
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'run-your-package=your_package_name.main:app',
        ],
    },
)
