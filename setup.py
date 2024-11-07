# setup.py
from setuptools import setup, find_packages

setup(
    name="flask_api_example",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'Flask==3.0.3',
    ],
    entry_points={
        'console_scripts': [
            'flask_api_example=flask_api_example.app:main',
        ],
    },
    description='A simple Flask API example',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/flask_api_example',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Flask',
    ],
)
