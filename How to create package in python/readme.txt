1)	First create __init__.py file in your folder and write your code there

2)	Second create setup.py file out of the folder and write 	from setuptools import setup
									setup(name="namu",
									version="0.2",
									description="This is code with harry package",
									long_description = "This is a very very long description",
									author="Vishal",
									packages=['namu'],
									install_requires=[])
	this code.

3)	Third run setup.y like = python setup.py sdist bdist_wheel  (Note: make sure you have wheel installed)

4)	Fourth there will be to folder created by above command (dist,build) go to dist folder and install the package pip install package_name

