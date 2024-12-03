from dynaconf import Dynaconf
from typing import List
from .color_logger import get_logger


_CONFIG_FILES_PATHS: List[str] = []


def init_settings(config_files: List[str]) -> None:
    global _CONFIG_FILES_PATHS
    _CONFIG_FILES_PATHS = config_files


class Settings:
    """
    A Singleton class for settings
    """
    _instance = None
    _settings = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            if not _CONFIG_FILES_PATHS:
                raise ValueError('No config files supplied to an uninitialized instance!')
            else:
                get_logger().info(f'Loading config files: {str(_CONFIG_FILES_PATHS)}')
                cls._settings = Dynaconf(
                    settings_files=_CONFIG_FILES_PATHS,
                    environments=False,
                    merge_enabled=True
                )
            cls._instance = super(Settings, cls).__new__(cls)
        return cls._instance

    def __getattr__(self, name):
        try:
            return getattr(self._settings, name)
        except AttributeError:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
    
    def __setattr__(self, name, value):
        if name == '_settings':
            # Handle setting the '_settings' attribute directly.
            # Use super().__setattr__() to avoid infinite recursion.
            super().__setattr__(name, value)
        else:
            # Attempt to set the attribute on the '_settings' object.
            try:
                setattr(self._settings, name, value)
            except AttributeError:
                # If it fails, set the attribute normally.
                super().__setattr__(name, value)