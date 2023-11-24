import json

class File():
    @staticmethod
    def json_load(path: str, mode: str, level: str) -> list[dict]:

        with open(path, mode, encoding='utf-8') as json_file:
            level_setting = json.load(json_file).get(level)[0]
        return level_setting
    
    def create_property_list(path: str, mode: str, level: str,clase_deseada):
        json_file = File.json_load(path, mode, level)
        empty_list = []
        for key in json_file.get(f"{clase_deseada}").values():
            empty_list.append(key)    
        return empty_list    