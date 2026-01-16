import os
import json


class ConfigReader:
    _config = None
    CONFIG_PATH = "config.json"

    @classmethod
    def load_config(cls):
        if cls._config is None:
            dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            full_path = os.path.join(dir_path, cls.CONFIG_PATH)

            if not os.path.exists(full_path):
                raise FileNotFoundError(f"Config file not found: {full_path}")

            with open(full_path) as f:
                cls._config = json.load(f)
        return cls._config

    @classmethod
    def get(cls, key, default=None):
        config = cls.load_config()
        return config.get(key, default)
