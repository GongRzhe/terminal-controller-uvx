# Uploading to PyPI

This guide explains how to upload the Terminal Controller UVx package to PyPI, making it available for installation via `pip` and `uvx`.

## Prerequisites

Before uploading to PyPI, ensure you have the following:

1. A PyPI account
2. The `build` and `twine` packages installed:
   ```bash
   pip install build twine
   ```

## Build the Package

First, build the package:

```bash
python -m build
```

This will create both a source distribution (.tar.gz) and a wheel file (.whl) in the `dist` directory.

## Upload to PyPI

### Test PyPI (Recommended First)

To upload to Test PyPI first (for testing):

```bash
python -m twine upload --repository testpypi dist/*
```

You'll be prompted for your TestPyPI username and password.

Then, you can install the package from TestPyPI with:

```bash
pip install --index-url https://test.pypi.org/simple/ terminal-controller-uvx
```

### Production PyPI

When you're ready to make the package publicly available, upload to the main PyPI repository:

```bash
python -m twine upload dist/*
```

You'll be prompted for your PyPI username and password.

## UVx Registry

If UVx has a separate registry system, you might need to register your package with UVx as well. Check the UVx documentation for specific instructions.

Typically, this might involve:

```bash
uvx publish
```

## Versioning

Remember to update the version number in the following files before building a new release:

- `pyproject.toml`
- `terminal_controller_uvx/__init__.py`
- `uvx.json`

Follow semantic versioning (MAJOR.MINOR.PATCH).

## Automating with GitHub Actions

For automated releases, you can set up a GitHub Actions workflow. Create a file `.github/workflows/pypi-publish.yml` with the following content:

```yaml
name: Publish Python Package

on:
  release:
    types: [created]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install build twine
    - name: Build and publish
      env:
        TWINE_USERNAME: ${{ secrets.PYPI_USERNAME }}
        TWINE_PASSWORD: ${{ secrets.PYPI_PASSWORD }}
      run: |
        python -m build
        twine upload dist/*
```

Remember to add your PyPI username and password as GitHub repository secrets.