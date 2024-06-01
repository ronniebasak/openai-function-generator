from setuptools import setup, find_packages

setup(
    name="openai_tool_generator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    entry_points={
        "console_scripts": [
            "generate_tool_definition=your_module.generate_tool_definition:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool generator for OpenAI tools",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your_username/your_project_name",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)