"""Print out all the melons in our inventory."""


from melons import melons_dict


def print_melons_info(melons_dict):
    """Print each melon with corresponding attribute information."""

    for melon_name, attributes in melons_dict.items():
        print(melon_name.upper())

        for attribute, value in attributes.items():
            print(f"{attribute}: {value}")

print_melons_info(melons_dict)