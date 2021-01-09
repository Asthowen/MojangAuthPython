import setuptools

with open("README.md", "r", encoding="utf-8", errors="ignore") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MojangAuthPython",
    version="0.1.2",
    author="Asthowen",
    description="MojangAuthPython is a lib for mojang authentification.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Asthowen/MojangAuth-Python",
    packages=setuptools.find_packages(),
    python_requires='>= 3.6',
    include_package_data=True,
    install_requires=['requests']
)