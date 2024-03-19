from dataclasses import dataclass
from src.user.user import User

@dataclass
class Group:
    '''
    Class for groups.
    '''
    id : int
    '''Unique identifier of the group.'''
    name : str
    '''Name of the group.'''

    def add_user(self, user : User) -> bool:
        '''
        Adds the given user to this group.

        Args:
            user (User): User object which should be added to the group.
            
        Returns:
            bool: True if success, otherwise False.
        '''
        return True