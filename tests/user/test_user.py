from src.user.user import User

def test_user_creation_negative():
    '''
    User creation should fail when no parameters are set when trying to create a user.
    '''
    try:
        user = User()
        assert False
    except Exception as e:
        print(e)
        assert True

def test_user_creation_positive():
    '''
    User creation with parameters should succeed.
    '''
    try:
        user = User(1, "Aleksi")
        user.id = 2
        user.name = "Mark"
        assert True
    except Exception as e:
        print(e)
        assert False

def test_user_group_set():
    '''
    Setting user group should work.
    '''
    user = User(1, "Aleksi")
    assert user.set_group("admin")

def test_user_group_set_empty():
    '''
    Setting empty ("") user group should fail.
    '''
    user = User(1, "Aleksi")
    assert user.set_group("") == False

def test_user_group_set_none():
    '''
    Setting empty (None) user group should fail.
    '''
    user = User(1, "Aleksi")
    assert user.set_group(None) == False