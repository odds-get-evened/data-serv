from setuptools import setup, find_packages

reqs = []

setup(
    name='data_server',
    description='',
    author='Chris Walsh',
    author_email='chris.is.rad@pm.me',
    packages=find_packages(),
    install_requires=reqs,
    setup_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.12'
)