from prob4_active_directory import Group, is_user_in_group


def _create_group(g_name, u_names):
    group = Group(g_name)
    for u_name in u_names:
        group.add_user(u_name)
    return group

def _create_default_group_scheme(*groupname_users_pairs):
    # Creates a hierarchy of groups, where each group consists multiple users and only one subgroup.
    groups_to_return = []
    group = _create_group(*groupname_users_pairs[0])
    for i in range(1, len(groupname_users_pairs)):
        groups_to_return.append(group)
        current_group = _create_group(groupname_users_pairs[i][0], groupname_users_pairs[i][1])
        group.add_group(current_group)
        group = current_group

    groups_to_return.append(group)
    return groups_to_return


def test_regular_case():
    groups = _create_default_group_scheme(("parent", []), ("child", []), ("subchild", ["sub_child_user"]))
    user_to_search = "sub_child_user"
    for group in groups:
        _test_valid(user_to_search, group)  # Should print "is in" for all groups.


def test_edge_cases():
    groups = _create_default_group_scheme(("parent", []), ("child", []), ("subchild", ["sub_child_user"]))
    user_to_search = "varien"
    for group in groups:
        _test_valid(user_to_search, group)  # Should print "is not in" for all groups.

    user_to_search = ""
    for group in groups:
        try:
            _test_valid(user_to_search, group)
        except Exception:
            print("Empty user test pass")  # Should print here.


def _test_valid(user_to_search, group):
    if not is_user_in_group(user_to_search, group):
        print(f"{user_to_search} is not in {group.get_name()}")
    else:
        print(f"{user_to_search} is in {group.get_name()}")


if __name__ == "__main__":
    print("Testing regular case...")
    test_regular_case()
    print("Testing edge cases...")
    test_edge_cases()