from setuptools import setup

def get_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()

setup(
    name='aiodathost',
    version='3.0.0',
    description='Asynchronous dathost API wrapper.',
    author='WardPearce',
    author_email='contact@districtnine.host',
    install_requires=get_requirements(),
    license='GPL v3',
    packages=['aiodathost'],
    zip_safe=False
)
