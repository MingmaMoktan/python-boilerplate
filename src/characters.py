class CharCreator:
    """
    A class to perform operations with characters and to create text.
    
    This class allows adding and removing characters, transforming the case of characters,
    and creating text from accumulated characters.
    
    Attributes:
        characters (list of str): A list to store characters.
    """
    
    def __init__(self):
        """Initializes the CharCreator with an empty list of characters."""
        self.characters = []
    
    def add_char(self, char: str) -> None:
        """
        Adds a single character to the list.
        
        Args:
            char (str): A single character to be added.
            
        Raises:
            ValueError: If the input is not a single character.
        """
        if len(char) == 1:
            self.characters.append(char)
        else:
            raise ValueError("Only single characters are allowed")
    
    def remove_char(self) -> None:
        """
        Removes the last character from the list.
        
        Raises:
            IndexError: If there are no characters to remove.
        """
        if self.characters:
            self.characters.pop()
        else:
            raise IndexError("No characters to remove")
    
    def uppercase_last(self) -> None:
        """
        Transforms the last character to uppercase.
        
        Raises:
            IndexError: If there are no characters to transform.
        """
        if self.characters:
            self.characters[-1] = self.characters[-1].upper()
        else:
            raise IndexError("No characters to transform")
    
    def lowercase_last(self) -> None:
        """
        Transforms the last character to lowercase.
        
        Raises:
            IndexError: If there are no characters to transform.
        """
        if self.characters:
            self.characters[-1] = self.characters[-1].lower()
        else:
            raise IndexError("No characters to transform")
    
    def create_text(self) -> str:
        """
        Constructs and returns text from the accumulated characters.
        
        Returns:
            str: The constructed text from accumulated characters.
        """
        return ''.join(self.characters)
    
    def clear(self) -> None:
        """
        Clears all characters from the list.
        """
        self.characters.clear()