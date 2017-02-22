# version contains Year and Month of API actualization
# last part is minor update, if needed
VERSION = (2017, 2, 0)


def get_version(version=None):
    """Derives a PEP386-compliant version number from VERSION."""

    if version is None:
        version = VERSION

    return '.'.join(str(x) for x in version)
