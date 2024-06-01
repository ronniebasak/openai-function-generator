from setuptools import setup, find_packages

setup(
    name="openai_tool_generator",
    version="0.2.0",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    entry_points={
        "console_scripts": [
            "generate_tool_definition=your_module.generate_tool_definition:main",
        ],
    },
    author="Sohan Basak",
    author_email="ronnie.basak96@gmail.com",
    description="Generate OpenAI Compatible tool definitions by parsing Python functions",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ronniebasak/openai-function-generator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)