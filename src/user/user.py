from dataclasses import dataclass

@dataclass
class User:
    '''
    Class for users.
    '''
    id : int
    '''Unique ID of the user.'''
    name : str
    '''Name of the user (firstname & lastname)'''

    def set_group(self, newGroup : str):
        '''
        Sets new group for the user.

        Args:
            newGroup (str): Name of the new group. This cannot be empty or "".
        
        Returns:
            bool: True if user was added to the group and otherwise False.
        '''
        if not newGroup:
            return False
        return True