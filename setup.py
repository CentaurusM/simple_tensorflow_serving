# Update the code and upload the package to pypi
# 1. python ./setup.py sdist --format=gztar
# 2. twine upload dist/simple_tensorflow_serving-1.0.0.tar.gz

try:
  from setuptools import setup
  setup()
except ImportError:
  from distutils.core import setup

setup(
    name="simple_tensorflow_serving",
    version="0.2.1",
    author="tobe",
    author_email="tobeg3oogle@gmail.com",
    url="https://github.com/tobegit3hub/simple_tensorflow_serving",
    install_requires=["tensorflow>=1.0.0"],
    description=
    "The simpler and easy-to-use serving service for TensorFlow models",
    packages=[
        "simple_tensorflow_serving", "simple_tensorflow_serving.gen_sdk"
    ],
    entry_points={
        "console_scripts": [
            "simple_tensorflow_serving=simple_tensorflow_serving.server:main",
        ],
    })
