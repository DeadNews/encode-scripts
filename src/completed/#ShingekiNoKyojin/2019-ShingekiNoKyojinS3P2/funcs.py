import dnfunc as dn


def ext_nc(epname):
    jpn = dn.source(f"./in/{epname}.mp4").std.AssumeFPS(fpsnum=24000, fpsden=1001)
    usa = dn.source(f"./in/usa/{epname}.mp4")[24:].std.AssumeFPS(fpsnum=24000, fpsden=1001)

    return dn.average([jpn, usa, jpn, jpn, jpn])


def get_maps(epname):
    maps = {
        "e2": [(5327, 5662)],
        "e3": [(30467, 30664)],
        "e6": [
            (482, 581),
            (656, 746),
            (776, 860),
            (884, 962),
            (1080, 1167),
            (1340, 1436),
            (1576, 1655),
            (1681, 1759),
            (1777, 1857),
            (2195, 2285),
            (2345, 2446),
            (2677, 2814),
            (2964, 3043),
            (3080, 3168),
            (3256, 3335),
            (3466, 3532),
            (3692, 3791),
            (3981, 4100),
        ],
        "e8": [
            (671, 790),
            (812, 949),
            (1104, 1218),
            (1246, 1346),
            (1383, 1473),
            (1490, 1578),
            (1794, 1892),
            (1923, 2012),
            (2071, 2155),
            (2173, 2252),
            (2373, 2462),
            (2514, 2615),
            (2633, 2726),
            (2756, 2853),
            (3032, 3123),
            (3365, 3460),
            (3647, 3739),
            (3773, 3862),
        ],
        "e9": [
            (32125, 32190),
            (32211, 32274),
            (32302, 32376),
            (32397, 32469),
            (32497, 32595),
            (32626, 32691),
            (32725, 32814),
            (32833, 32922),
            (32960, 33024),
            (33040, 33106),
            (33124, 33199),
            (33214, 33321),
            (33339, 33417),
            (33458, 33535),
            (33557, 33637),
            (33659, 33750),
            (33782, 33880),
            (33934, 34045),
        ],
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
