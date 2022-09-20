import dnfunc as dn
from lvsfunc import misc


def ef(clip):
    planes = dn.split(clip)

    y = planes[0].edgefixer.Continuity(top=1, radius=1).edgefixer.Continuity(top=2, bottom=1)
    u = planes[1].edgefixer.Continuity(top=1, radius=1)
    v = planes[2].edgefixer.Continuity(top=1, radius=1)

    yuv = dn.join([y, u, v])
    ref = yuv.std.BoxBlur(hradius=1, hpasses=3, vpasses=0)

    return misc.wipe_row(yuv, ref, pos=(0, 0), size=(1920, 1))


def ef_ed(clip):
    planes = dn.split(clip)

    y = planes[0].edgefixer.Continuity(top=1, bottom=1)
    u = planes[1].edgefixer.Continuity(top=1, radius=1)
    v = planes[2].edgefixer.Continuity(top=1, radius=1)

    return dn.join([y, u, v])
