# -*- coding: utf-8 -*-

from setuptools import setup
import ziwia.version

setup(name="ziwia",
      version= ziwia.version.__version__,
      description="API client for Kraken cryptocurrency trading site.",
      url="http://github.com/malja/ziwia",
      author="Jan Malčák",
      author_email="jan@malcakov.cz",
      license="MIT",
      packages=["ziwia"],
      requires=["requests"],
      classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Topic :: Internet",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Natural Language :: English",

            "Operating System :: Microsoft :: Windows",
            "Operating System :: POSIX :: Linux",
      ],
      keywords="kraken bitcoin cryptocurrency exchange client api rest",
      zip_safe=True)
