def all_thing_is_obj(object: any) -> int:
    t = type(object)

    if t is list:
        print("List :", type(object))
    elif t is tuple:
        print("Tuple :", type(object))
    elif t is set:
        print("Set :", type(object))
    elif t is dict:
        print("Dict :", type(object))
    elif t is str:
        print(f"{object} is in the kitchen :", type(object))
    else:
        print("Type not found")

    return 42
