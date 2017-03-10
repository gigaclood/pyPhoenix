from setuptools import setup, find_packages

cmdclass = {}

try:
    from sphinx.setup_command import BuildDoc
    cmdclass['build_sphinx'] = BuildDoc
except ImportError:
    pass

def readme():
    with open('README.rst') as f:
        return f.read()

version = "0.9.4"

setup(
    name="pyPhoenix",
    version=version,
    description="python interface to Phoenix",
    long_description=readme(),
    author="Dimitri Capitaine",
    author_email="grytes29@gmail.com",
    url="https://github.com/Pirionfr/pyPhoenix",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    cmdclass=cmdclass,
    zip_safe=False,
    install_requires=['protobuf','sqlalchemy'],
    command_options={
        'build_sphinx': {
            'version': ('setup.py', version),
            'release': ('setup.py', version),
        },
    },

    entry_points={
        "sqlalchemy.dialects": [
            "phoenix = pyphoenix.sqlalchemy_phoenix:PhoenixDialect"
        ]
    },
)
