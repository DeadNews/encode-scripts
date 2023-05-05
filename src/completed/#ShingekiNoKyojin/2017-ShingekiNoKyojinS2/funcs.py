import dnfunc as dn


def ext_nc(epname):
    jpn = dn.source(f"./in/{epname}.mp4")
    usa = dn.source(f"./in/usa/{epname}.mp4")[24:]

    return dn.average([jpn, usa, jpn, jpn])


def get_maps(epname):
    maps = {
        "e1": [(11726, 11787), (11821, 11902)],
        "e2": [(4359, 4452), (4684, 4770)],
        "e3": [(6611, 6715), (10088, 10183), (12490, 12601)],
        "e4": [(3382, 3471)],
        "e6": [(18914, 18976), (18993, 19061)],
        "e8": [(5094, 5180)],
        "e12": [(25373, 25468)],
    }

    try:
        m = []
        for r in maps[epname]:
            start, end = r
            m.append((start - 6, end + 6))

    except Exception:
        return None
    else:
        return m
