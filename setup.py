from setuptools import setup, find_packages

setup(
    name='llm_streaming-client',
    version='0.1.0',
    author='ThubanTech',
    author_email='aortiz@thubantech.com',
    description='A simplified client for llm-streaming services.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'setuptools',
        'requests==2.32.3',
        'python-dotenv==1.0.1',
        'python-socketio==5.12.1'

    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    license='MIT',
    python_requires='>=3.9',
)