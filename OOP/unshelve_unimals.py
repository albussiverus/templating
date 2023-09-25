import shelve

if __name__ == '__main__':

    dbsh = shelve.open('dbl')
    print(f"Cound of objects: {len(dbsh)}")
    print("items:", dbsh.items())
    # print("keys:", dbsh.keys())
    # print("values:", dbsh.values())
    #
    #
    # for i in dbsh.items():
    #     print(i)
    #
    # for i in dbsh.values():
    #     print(i)
    #
    # for k in dbsh.keys():
    #     print(dbsh[k])
    #     dbsh[k].move()
    #
    # print(list(dbsh.items()))
    cat_tom = dbsh.get("tom", None)
    print(cat_tom)
