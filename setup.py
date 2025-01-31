from setuptools import setup

setup(
    name="dogeart",
    version="3.7.1",
    url="https://github.com/TeleDoge/dogeart",
    author="Lowe Thiderman",
    author_email="lowe.thiderman@gmail.com",
    description=("wow very terminal doge"),
    license="MIT",
    packages=["doge"],
    package_data={"doge": ["static/*.txt"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
    ],
    entry_points={"console_scripts": ["doge = doge.core:main"]},
)
