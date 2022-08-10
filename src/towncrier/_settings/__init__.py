"""Subpackage to handle settings parsing."""

from towncrier._settings import load


load_config = load.load_config
ConfigError = load.ConfigError
load_config_from_options = load.load_config_from_options
load_config_from_file = load.load_config_from_file


__all__ = [
    "load_config",
    "ConfigError",
    "load_config_from_options",
    "load_config_from_file",
]
