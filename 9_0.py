data = {
    'Section1': {
        'key1': 'value1',
        'key2': 'value2',
    },
    'Section2': {
        'key3': 'value3',
        'key4': 'value4'
    }
}

class ConfigParser:

    def __init__(self, text: str) -> None:
        self.data = self.loads(text)

    def has_section(self, section: str) -> bool:
        if section in data:
            True
        else:
            False
        return section in self.data

    def has_section(self, section: str) -> bool:
        return section in self.data

    def has_param(self, section: str, param: str) -> bool:
        if param in section:
            True
        else:
            False
    def add_param(self, param, section: str) -> None:
        if self.has_section(param):
            raise ValueError
        else:
            self.data[param] = param