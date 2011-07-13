from setuptools import setup, find_packages

setup(
    name = "JS Requirements",
    version = "0.1.0",
    description = """
    Import once all required js files from Django project templates at the end of generated html document for optimization purpose.
    Compatible with django-compressor.
    """,
    author = "Platypus Creation",
    author_email = "contact@platypus-creation.com",
    url = "https://github.com/platypus-creation/jsrequirements",
    packages = find_packages(),
)
