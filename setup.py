from setuptools import setup, find_packages
from os import path
import sys

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='apptracker',
    version='0.1.0',  # Updated version for new features
    description='A modern cross-platform application tracker',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/manojpawarsj12/apptracker',
    author='Manoj Pawar SJ',
    author_email='manojpawarsj.mp11@gmail.com',
    license="MIT",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    include_package_data=True,
    keywords='application tracker digitalwellbeing website tracker productivity',
    data_files=['apptracker/activities.json'],
    install_requires=[
        'python-dateutil',
        'plotly',
        'pywin32; platform_system=="Windows"',
        'uiautomation; platform_system=="Windows"',
        'pyobjc; platform_system=="Darwin"',
        'psutil; platform_system=="Linux"',
    ],
    packages=find_packages(),
    zip_safe=False,
    project_urls={
        'Bug Reports': 'https://github.com/manojpawarsj12/apptracker/issues',
        'Source': 'https://github.com/manojpawarsj12/apptracker',
    },
    entry_points={
        'console_scripts': [
            'apptracker=apptracker.main:main',
        ],
    },
)