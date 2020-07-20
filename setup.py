import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="visual_kinematics",
    version="0.0.7",
    author="Yue QI",
    author_email="dbddqy@gmail.com",
    description="A package for calculating robot kinematics and visualizing trajectory in just a few lines of code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dbddqy/visual_kinematics",
    packages=setuptools.find_packages(),
    keywords = ['robotics', ' kinematics', 'inverse kinematics', 'trajectory planning', 'visualization'],
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
