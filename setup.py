from setuptools import setup, find_packages

setup(
    name="aws-service-explorer",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests>=2.26.0",
    ],
    entry_points={
        "console_scripts": [
            "aws-service-explorer=aws_service_explorer:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python program to explore AWS services and their API actions",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/aws-service-explorer",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)