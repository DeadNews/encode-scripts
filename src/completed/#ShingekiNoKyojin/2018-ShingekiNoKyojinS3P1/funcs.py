import dnfunc as dn


def ext_nc(epname):
    jpn = dn.source(f"./in/{epname}.mp4").std.AssumeFPS(fpsnum=24000, fpsden=1001)
    usa = dn.source(f"./in/usa/{epname}.mp4")[24:].std.AssumeFPS(fpsnum=24000, fpsden=1001)

    return dn.average([jpn, usa, jpn, jpn, jpn])


def get_maps(epname):
    maps = {
        "e1": [
            (9104, 9205),
            (32792, 32838),
            (32853, 32899),
            (32912, 32956),
            (32968, 33012),
            (33027, 33072),
            (33086, 33130),
            (33146, 33190),
            (33207, 33252),
            (33268, 33314),
            (33334, 33379),
            (33395, 33441),
            (33458, 33503),
            (33521, 33567),
            (33590, 33636),
            (33654, 33698),
            (33715, 33760),
            (33771, 33815),
            (33834, 33878),
        ],
        "e2": [(12286, 12379)],
        "e4": [(4994, 5070)],
        "e8": [(27421, 27489)],
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
