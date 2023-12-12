from setuptools import setup, find_packages

setup(
    name="sqlalchemy-crud-base",
    version="0.1.2",
    author="HanSeul Jo",
    author_email="bryantjo1224@gmail.com",
    description="A SQLAlchemy-based CRUD package",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Seuleeee/sqlalchemy-crud-base",
    packages=find_packages(),
    install_requires=[
        "sqlalchemy>=2.0.0",
        "psycopg2-binary>=2.8",
        "python-dotenv>=1.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',  # Python 3.8 이상 필요
)
