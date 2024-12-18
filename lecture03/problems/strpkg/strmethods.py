from typing import List


class StringMethods:
    @staticmethod
    def capitalize_method(entry_str:str) -> str:
        _entry_str = entry_str
        _result = _entry_str.capitalize()
        return _result

    @staticmethod
    def casefold_method(entry_str:str) -> str:
        _entry_str = entry_str
        _result = _entry_str.casefold()
        return _result

    @staticmethod
    def center_method(entry_str:str,entry_length: int) -> str:
        _entry_str = entry_str
        _result = _entry_str.center(entry_length)
        return _result

    @staticmethod
    def count_method(entry_str:str, search_word) -> int:
        _entry_str = entry_str
        _search_word = search_word
        _result = _entry_str.count(_search_word)
        return _result

    @staticmethod
    def encode_method(entry_str:str) -> bytes:
        _entry_str = entry_str
        _result = _entry_str.encode()
        return _result

    @staticmethod
    def endswith_method(entry_str:str, ends_with:str) -> bool:
        _entry_str = entry_str
        _result = _entry_str.endswith(ends_with)
        return _result

    @staticmethod
    def expandtabs_method(entry_str:str, expand:int) -> str:
        _entry_str = entry_str
        _result = _entry_str.expandtabs(expand)
        return _result

    @staticmethod
    def strip_method(entry_str:str, entry_str_one:str) -> str:
        if entry_str_one == "None":
            _entry_str = entry_str
            _result = _entry_str.strip()
            return _result
        elif entry_str_one != "None":
            _entry_str = entry_str
            _result = _entry_str.strip(entry_str_one)
            return _result

    @staticmethod
    def lstrip_method(entry_str:str, entry_str_one:str) -> str:
        if entry_str_one == "None":
            _entry_str = entry_str
            _result = _entry_str.lstrip()
            return _result
        elif entry_str_one != "None":
            _entry_str = entry_str
            _result = _entry_str.lstrip(entry_str_one)
            return _result

    @staticmethod
    def rstrip_method(entry_str:str, entry_str_one:str) -> str:
        if entry_str_one == "None":
            _entry_str = entry_str
            _result = _entry_str.rstrip()
            return _result
        elif entry_str_one != "None":
            _entry_str = entry_str
            _result = _entry_str.rstrip(entry_str_one)
            return _result

    @staticmethod
    def len_str_method(entry_str:str) -> int:
        _entry_str = entry_str
        _result = len(_entry_str)
        return _result

    @staticmethod
    def in_operator_method(entry_str:str, check_str:str) -> bool:
        _entry_str = entry_str
        _result = check_str in _entry_str
        return _result

    @staticmethod
    def split_method(entry_str:str) -> List:
        _entry_str = entry_str
        _result = _entry_str.split()
        return _result



























