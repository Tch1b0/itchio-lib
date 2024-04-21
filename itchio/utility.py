def satisfy_dict(have_dict: dict, want_dict: dict) -> dict:
    """
    Make sure the have_dict satisfies the keys of want_dict.

    If a key is missing, the want_dict value is assigned to the key.
    """
    new_dict = have_dict.copy()
    for key, value in want_dict:
        if key not in have_dict:
            new_dict[key] = value
    return new_dict
