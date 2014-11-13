VERSION = (0, 0, 4)


def get_version(version=None):
    """Derives a PEP386-compliant version number from VERSION."""

    if version is None:
        version = VERSION

    return '.'.join(str(x) for x in version)
