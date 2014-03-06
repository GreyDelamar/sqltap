from setuptools import setup

long_description = """
sqltap is a library that allows you to profile and introspect the
queries that your application makes using SQLAlchemy.

sqltap helps you quickly understand:

   * how many times a sql query is executed
   * how much time your sql queries take
   * where your application is issuing sql queries from

Full HTML documentation can be generated by sphinx, or browsed online at: https://sqltap.you-compete.com

SQLTap is hosted on github at: https://github.com/inconshreveable/sqltap
"""

setup(
    name = "sqltap",
    version = "0.3",
    description = "Profiling and introspection for applications using sqlalchemy",
    long_description = long_description,
    author = "inconshreveable",
    author_email = "alan@inconshreveable.com",
    url = "https://github.com/inconshreveable/sqltap",
    packages = ["sqltap"],
    package_data = {"sqltap" : ["templates/*.mako"]},
    install_requires = [
        "SQLAlchemy >= 0.8",
        "Mako >= 0.4.1"
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Database'
    ]
)

