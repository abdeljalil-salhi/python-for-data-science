def all_thing_is_obj(object: any) -> int:
    _type = type(object)
    if _type is list:
        print("List :", type(object))
    elif _type is tuple:
        print("Tuple :", type(object))
    elif _type is set:
        print("Set :", type(object))
    elif _type is dict:
        print("Dict :", type(object))
    elif _type is str:
        print(f"{object} is in the kitchen :", type(object))
    else:
        print("Type not found")
    return 42
