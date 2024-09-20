from setuptools import setup, find_packages # type: ignore

setup(
    name='my_python_project',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'truffleHog',
        'pre-commit',
        'GitPython',
        'truffleHogRegexes',
    ],
    entry_points={
        'console_scripts': [
            # Add any command-line scripts here if needed
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
