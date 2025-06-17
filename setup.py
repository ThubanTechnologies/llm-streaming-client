from setuptools import setup, find_packages

setup(
    name="llm_streaming-client",
    version="1.0.0",
    author="Alba Marco Ugarte",
    author_email="amarco@thubantech.com",
    description="A simplified client for llm-streaming services.",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "setuptools",
        "requests>=2.32.3",
        "python-dotenv>=1.1.0",
        "python-socketio==5.12.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    python_requires=">=3.9",
)
