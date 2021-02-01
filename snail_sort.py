def snail(snail_map):
    ls = []
    while len(snail_map) > 0:

        ls.append(snail_map[0])
        del snail_map[0]

        ls.append([x[-1] for x in snail_map])
        for x in snail_map:
            del x[-1]

        if snail_map:
            ls.append(list(reversed(snail_map[-1])))
            del snail_map[-1]

            ls.append(list(reversed([x[0] for x in snail_map])))
            for x in snail_map:
                    del x[0]

    return sum(ls, [])
