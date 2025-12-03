import json
import os
from utils.language_enum import Lang

class ConfigReader:
    def __init__(self, config_path=None):
        base_dir = os.path.dirname(__file__)

        if config_path is None:
            config_path = os.path.join(base_dir, "config.json")

        with open(config_path, "r", encoding="utf-8") as f:
            self.config = json.load(f)

    # Таймаут
    @property
    def timeout(self):
        return self.config.get("timeout", 30)

    # Языки
    @property
    def languages(self):
        raw_langs = self.config.get("languages", [])
        return [Lang.normalize(l) for l in raw_langs]

    # URL
    @property
    def base_url(self):
        return self.config.get("urls", {}).get("base", "")

    # Получить URL с языком
    def url_for_lang(self, lang):
        return f"{self.base_url}?l={lang}"

    # Настройки браузера
    def browser_setting(self, key, default=False):
        return self.config.get("browser", {}).get(key, default)
