from setuptools import setup

from regex_reader import VERSION

setup(
        name = 'CountESS Plugin: Regex Reader',
        version = VERSION,
        author = 'CountESS Developers',
        maintainer = 'Nick Moore',
        maintainer_email = 'nick@zoic.org',
        packages = [ '.' ],
        entry_points = {
            'countess_plugins': [
                'regex_reader = regex_reader:RegexReaderPlugin',
            ],
        },
        install_requires = [
            'countess>=0.0.2',
        ],
        license = 'BSD',
        license_files = ('LICENSE.txt',),
        classifiers = [
            'Intended Audience :: Science/Research',
            'License :: Public Domain',
            'Operating System :: OS Independent',
            'Topic :: Scientific/Engineering :: Bio-Informatics',
        ],
)

