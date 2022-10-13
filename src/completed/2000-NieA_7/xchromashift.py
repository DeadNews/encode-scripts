import dnfunc as dn

# -----in----- #
epname = "e13"

epis = dn.source(f"./in/{epname}.mp4")
epis = epis.std.CropRel(left=240, right=240)

fix = dn.chromashift(epis, cx=2.5, cy=0)
epis_back = epis
epis = dn.adaptive_chromashift(epis, fix, pw_mode=True)

if epname == "e1":
    epis_back_map = "3190 [6499 6584] [5336 5981] [7940 8565] [7113 7223]"
    fix_map = [(10384, 10388), (4022, 4116)]

elif epname == "e2":
    epis_back_map = [
        (2692, 2751),
        (3003, 3110),
        (9727, 10032),
        (15549, 15604),
        (18161, 18193),
        (21746, 21780),
        (25670, 25801),
        (30852, 30971),
    ]
    fix_map = [(18038, 18131), (25502, 25669), (27333, 27440), (28312, 28479)]

elif epname == "e3":
    epis_back_map = [(15371, 15478)]
    fix_map = [(29630, 29964)]

elif epname == "e4":
    epis_back_map = [(13154, 13415)]
    fix_map = [(0, 1)]

elif epname == "e5":
    epis_back_map = [(9447, 9518), (15198, 15228)]
    fix_map = [(0, 1)]

elif epname == "e6":
    epis_back_map = [(2304, 2420)]
    fix_map = [(0, 1)]

elif epname == "e7":
    epis_back_map = [(3150, 3217), (21069, 21158)]
    fix_map = [(10494, 10768), (20952, 21068), (27721, 27775)]

elif epname == "e8":
    epis_back_map = [(7325, 7635), (14369, 15481), (18737, 18814)]
    fix_map = [(2533, 2650), (15768, 15833), (17739, 17846), (17847, 18067)]

elif epname == "e9":
    epis_back_map = [
        (4651, 4689),
        (5216, 5359),
        (9919, 9982),
        (22464, 22650),
        (26812, 27318),
        (28235, 28325),
    ]
    fix_map = [(8348, 8644), (11142, 11236), (17941, 18132), (19837, 19881), (30463, 30606)]

elif epname == "e10":
    epis_back_map = [
        (16652, 16733),
        (20534, 20660),
        (23611, 23774),
        (23932, 24074),
        (26083, 26265),
        (26978, 27104),
        (29231, 29390),
        (29852, 30671),
    ]
    fix_map = [(26575, 26734)]

elif epname == "e11":
    epis_back_map = [(2330, 2897), (15411, 15619), (30697, 30881)]
    fix_map = [(0, 1)]

elif epname == "e12":
    epis_back_map = [(2927, 3056), (10779, 10866), (11746, 12663), (12664, 12784), (17758, 17918)]
    fix_map = [(0, 1)]

elif epname == "e13":
    epis_back_map = [(2054, 2179), (8835, 8923)]
    fix_map = [(0, 1)]

epis = dn.rfs(epis, epis_back, epis_back_map)
epis = dn.rfs(epis, fix, fix_map)

epis.set_output()
# epis_back.set_output()
