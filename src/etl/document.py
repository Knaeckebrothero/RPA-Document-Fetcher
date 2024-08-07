"""
This module holds the document class.
"""


class Document:
    """
    The Document class represents a document.
    It holds the file, text, attributes, name, and type of the document.
    """
    def __init__(self, file: bytes, filetype: str = None, name: str = None):
        """
        The constructor for the Document class.

        :param file: The file to be processed.
        :param filetype: The type of the file.
        :param name: The name of the file.
        """
        self._filetype: str = filetype
        self._name: str = name
        self._raw: bytes = file
        self._text: str = ""
        self._attributes: dict = {}

    def __str__(self):
        string_form = f"Document: {self._name}, {self._filetype}, {len(self._attributes.keys())} attributes"
        return string_form

    def get_type(self) -> str:
        return self._filetype

    def get_name(self) -> str:
        return self._name

    def get_file(self) -> bytes:
        return self._raw

    def get_text(self) -> str:
        return self._text

    def get_attributes(self, attributes: list[str] = None) -> dict:
        """
        Get the attributes of the document.
        If a list of attributes is provided, only those attributes will be returned.

        :param attributes: Optional list of attributes to return.
        :return: All attributes of the document. Or only the attributes in the list.
        """
        if attributes:
            return {key: value for key, value in self._attributes.items() if key in attributes}
        else:
            return self._attributes

    def set_type(self, filetype: str):
        self._filetype = filetype

    def set_name(self, name: str):
        self._name = name

    def add_attributes(self, attributes: dict):
        """
        Set the attributes of the document.

        :param attributes: The attributes to be set.
        """
        self._attributes.update(attributes)

    def update_attributes(self, attributes: dict):
        """
        Update the attributes of the document.

        :param attributes: The attributes to be updated.
        """
        self._attributes.update(attributes)

    def delete_attributes(self, attributes: list[str] = None):
        """
        Delete the attributes of the document.

        :param attributes: The attributes to be deleted.
        """
        if attributes:
            for attribute in attributes:
                self._attributes.pop(attribute)
        else:
            self._attributes.clear()
