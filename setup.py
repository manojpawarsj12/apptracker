from setuptools import setup, find_packages
from os import path
import sys
here = path.abspath(path.dirname(__file__))
if sys.platform in ['Windows', 'win32', 'cygwin']:
    pass
else:
    print("this package is for windows users \n")
    exit(0)
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='apptracker',
    version='0.0.5',
    description=long_description,
    url='https://github.com/manojpawarsj12/apptracker',
    author='Manoj Pawar SJ',
    author_email='manojpawarsj.mp11@gmail.com',
    license="MIT",
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: Microsoft :: Windows',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: 3.8',
                 ],
    include_package_data=True,
    keywords='application tracker digitalwellbeing website tracker ',
    data_files=['apptracker/activities.json'],
    install_requires=['python-dateutil',
                      'plotly', "pywin32", 'uiautomation'],
    platform=['Windows',"win32"],
    packages=['apptracker'],
    zip_safe=False,
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/manojpawarsj12/apptracker/issues',
        'Source': 'https://github.com/manojpawarsj12/apptracker'
    },
    entry_points='''
        [console_scripts]
        apptracker=apptracker.__init__:main
        '''
)
