def NULL_not_found(object: any) -> int:
    t = type(object)

    if object is None:
        print("Nothing: None", t)
    elif t is float and object != object:
        print("Cheese: nan", t)
    elif object == 0 and t is int:
        print("Zero: 0", t)
    elif t is str and len(object) == 0:
        print("Empty:", t)
    elif object is False and t is bool:
        print("Fake: False", t)
    else:
        print("Type not Found")
        return 1

    return 0
