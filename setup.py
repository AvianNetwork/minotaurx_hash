from setuptools import setup, Extension
import os


# Read the README for the long description
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            return f.read()
    return "MinotaurX proof-of-work hash function"


minotaurx_hash_module = Extension(
    "minotaurx_hash",
    sources=[
        "minotaurx_module.c",
        "minotaurx.c",
        "sha3/blake.c",
        "sha3/bmw.c",
        "sha3/groestl.c",
        "sha3/jh.c",
        "sha3/keccak.c",
        "sha3/skein.c",
        "sha3/cubehash.c",
        "sha3/echo.c",
        "sha3/luffa.c",
        "sha3/simd.c",
        "sha3/hamsi.c",
        "sha3/hamsi_helper.c",
        "sha3/fugue.c",
        "sha3/shavite.c",
        "sha3/shabal.c",
        "sha3/whirlpool.c",
        "sha3/sha2big.c",
        "yespower/sha256.c",
        "yespower/yespower.c",
    ],
    include_dirs=[".", "./sha3", "./yespower"],
)

setup(
    name="minotaurx_hash",
    version="1.1.0",
    description="MinotaurX proof-of-work hash function for blockchain mining",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/AvianNetwork/minotaurx_hash",
    author="Avian Network",
    author_email="contact@avn.network",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Security :: Cryptography",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="hash crypto blockchain mining proof-of-work",
    project_urls={
        "Documentation": "https://github.com/AvianNetwork/minotaurx_hash#readme",
        "Source": "https://github.com/AvianNetwork/minotaurx_hash",
        "Tracker": "https://github.com/AvianNetwork/minotaurx_hash/issues",
    },
    python_requires=">=3.6",
    ext_modules=[minotaurx_hash_module],
)
