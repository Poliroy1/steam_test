from enum import StrEnum

class Lang(StrEnum):
    EN = "en"
    RU = "ru"

    @staticmethod
    def normalize(value: str):
        """
        Приводит любое представление языка к одному из поддерживаемых.
        Поддерживает форматы:
        - en / EN / En
        - en-US / en_US
        - english / English
        - ru / russian / Русский / ru-RU / ru_RU / РУ / РФ
        """

        if not value:
            raise ValueError("Language value is empty")

        v = value.lower().replace("-", "_").strip()

        # Вариации русского
        ru_variants = {
            "ru", "ru_ru", "russian", "русский", "рус", "ру", "рф"
        }

        # Вариации английского
        en_variants = {
            "en", "en_us", "english", "английский", "инглиш"
        }

        if v in ru_variants:
            return Lang.RU

        if v in en_variants:
            return Lang.EN

        raise ValueError(f"Unknown language value: {value}")