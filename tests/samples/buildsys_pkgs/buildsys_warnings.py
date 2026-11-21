"""Test "backend" defining nothing other than a hook that logs a warning.
"""

import warnings


def get_requires_for_build_wheel(config_settings):
    warnings.warn("this is my example warning")
    return []


def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    warnings.warn("deprecated build option", FutureWarning)
    raise RuntimeError("wheel build failed")
