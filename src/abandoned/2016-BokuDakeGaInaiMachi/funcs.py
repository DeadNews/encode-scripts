#!/usr/bin/env python

import dnfunc as dn


def efix(clip, zone):
    clip = clip.std.CropRel(top=130, bottom=130)

    planes = dn.split(clip)

    y = planes[0].std.CropRel(top=1, bottom=1)
    y = y.edgefixer.Continuity(top=1, bottom=1, radius=1).edgefixer.Continuity(top=3, bottom=3)
    y = dn.aa(y, zone=zone)
    y = y.std.AddBorders(top=1, bottom=1)

    u = planes[1].edgefixer.Continuity(top=1, bottom=1, radius=1)
    v = planes[2].edgefixer.Continuity(top=1, bottom=1, radius=1)

    return dn.join([y, u, v]).std.AddBorders(top=130, bottom=130, color=[4096, 32768, 32768])


def get_maps(epname):
    maps = dict(
        e1=[
            (24, 4525),
            (4588, 4692),
            (4697, 4786),
            (4790, 4894),
            (4896, 15561),
            (15583, 22377),
            (22403, 29663),
            (30735, 30771),
            (30838, 30965),
            (30975, 32611),
            (32617, 32642),
            (32652, 32758),
            (32763, 32869),
        ],
        e2=[
            (0, 482),
            (495, 911),
            (1032, 2700),
            (2708, 3188),
            (7295, 7328),
            (7762, 7791),
            (9894, 10252),
            (10915, 11129),
            (15468, 15549),
            (15944, 16015),
            (16521, 16588),
            (21198, 22399),
            (23737, 23759),
            (27274, 27462),
            (30281, 30422),
            (30771, 31611),
            (31662, 31770),
            (31775, 32245),
            (32247, 32251),
            (32253, 32845),
        ],
        e3=[
            (751, 3274),
            (3282, 3764),
            (7144, 7263),
            (11084, 11204),
            (13916, 14056),
            (14448, 14529),
            (18247, 18316),
            (26738, 26871),
            (30771, 31611),
            (31662, 31770),
            (31775, 32245),
            (32247, 32251),
            (32253, 32846),
        ],
        e4=[
            (24, 1016),
            (1188, 1462),
            (1558, 3226),
            (3234, 3716),
            (12766, 12818),
            (13662, 13684),
            (14229, 14479),
            (14761, 14967),
            (15805, 15890),
            (16112, 16183),
            (18023, 18106),
            (25086, 25332),
            (30795, 31635),
            (31686, 31794),
            (31799, 32269),
            (32271, 32275),
            (32277, 32869),
        ],
        e5=[
            (2254, 3922),
            (3930, 4410),
            (8165, 8283),
            (11757, 11952),
            (11955, 11979),
            (11982, 20000),
            (20021, 28672),
            (28676, 30688),
            (30771, 31611),
            (31662, 31770),
            (31775, 32245),
            (32247, 32251),
            (32253, 32845),
        ],
        e6=[
            (0, 2676),
            (2684, 6068),
            (6089, 6344),
            (6358, 10672),
            (10718, 10935),
            (10944, 11119),
            (11123, 30689),
            (30772, 31612),
            (31663, 31771),
            (31776, 32246),
            (32248, 32252),
            (32254, 32846),
        ],
        e7=[
            (24, 1629),
            (3285, 4953),
            (4961, 5442),
            (10297, 10436),
            (12536, 12798),
            (21099, 21170),
            (27384, 27886),
            (30797, 31637),
            (31688, 31796),
            (31801, 32271),
            (32273, 32277),
            (32279, 32871),
        ],
        e8=[
            (1630, 3298),
            (3306, 3788),
            (15503, 16763),
            (28406, 28407),
            (28453, 28454),
            (30773, 31613),
            (31664, 31772),
            (31777, 32247),
            (32249, 32253),
            (32255, 32847),
        ],
        e9=[
            (1702, 3370),
            (3378, 3860),
            (13404, 13476),
            (15803, 16066),
            (28665, 28826),
            (29021, 29074),
            (30773, 31613),
            (31664, 31772),
            (31777, 32247),
            (32249, 32253),
            (32255, 32849),
        ],
        e10=[
            (24, 3012),
            (3020, 3500),
            (10155, 10285),
            (11398, 11466),
            (20548, 20619),
            (24510, 25270),
            (25336, 25417),
            (29714, 29987),
            (29998, 30108),
            (30116, 30668),
            (30796, 31636),
            (31687, 31795),
            (31800, 32270),
            (32272, 32276),
            (32278, 32870),
        ],
        e11=[
            (44, 2083),
            (2115, 3261),
            (3285, 4953),
            (4961, 11830),
            (11841, 16434),
            (16459, 26955),
            (26964, 30688),
            (30771, 31611),
            (31662, 31770),
            (31775, 32245),
            (32247, 32251),
            (32253, 32845),
        ],
        e12=[
            (0, 402),
            (430, 3418),
            (3426, 26931),
            (26964, 28913),
            (29080, 29133),
            (29223, 29277),
            (29378, 29538),
            (29906, 32845),
        ],
    )

    return maps.get(epname)