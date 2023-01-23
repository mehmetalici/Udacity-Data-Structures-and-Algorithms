class Group:
    def __init__(self, name):
        self.name = name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user: str, group: Group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user == "":
        raise Exception("User is empty")
    if user in group.get_users():
        return True
    if len(group.get_groups()) == 0:
        return False
    
    for subgroup in group.get_groups():
        if is_user_in_group(user, subgroup):
            return True


