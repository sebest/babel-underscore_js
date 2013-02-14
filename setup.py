from setuptools import setup

setup(
    name='underscore_html',
    py_modules=['underscore'],
    entry_points="""
    [babel.extractors]
    underscore = underscore:babel_extract
    """
)
    
