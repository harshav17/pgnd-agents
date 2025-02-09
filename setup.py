from setuptools import setup, find_packages

# Read requirements.txt
with open('requirements.txt') as f:
    required = f.read().splitlines()

# Read README.md for long description
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="pgnd-agents",  # Replace with your project name
    version="0.1.0",
    author="Harsha Lingampally",
    author_email="harshav17@gmail.com",
    description="A playground for playing with different agents and frameworks around agents.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/harshav17/pgnd-agents",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[],
    python_requires=">=3.8",
    install_requires=required,
    extras_require={
        'dev': [
            'pytest>=7.0',
            'pytest-cov>=3.0',
            'black>=22.0',
            'isort>=5.0',
            'flake8>=4.0',
            'mypy>=0.9',
            'jupyter>=1.0.0',
        ],
        'docs': [
            'sphinx>=4.0',
            'sphinx-rtd-theme>=1.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'ai-server=src.server.main:main',  # Allows running the server with 'ai-server' command
        ],
    }
)