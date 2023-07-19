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

    @classmethod
    def loads(cls, text: str) -> dict[str, dict[str, str]]:
        lines = [line for line in text.split('\n') if line]
        data = {}
        current_section = ''
        for line in lines:
            if line.startswith('[') and line.endswith(']'):
                current_section = line[1:-1]
                data[current_section] = {}
            else:
                key, value = line.split('=')
                data[current_section][key] = value
        return data



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