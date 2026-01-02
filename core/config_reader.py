import json
import os


class ConfigReader:
    def __init__(self, config_path: str = "config/config.json"):
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self) -> dict:
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Config file not found: {self.config_path}")

        with open(self.config_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def get(self, key: str, default=None):
        return self.config.get(key, default)