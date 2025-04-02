from setuptools import setup, find_packages

setup(
    name='file-manager-client',
    version='0.1.0',
    author='ThubanTech',
    author_email='aortiz@thubantech.com',
    description='A simplified client for file management services.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)