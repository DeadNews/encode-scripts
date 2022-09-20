import dnfunc as dn

# -----in----- #
epname = "e1"
jpn = dn.source(f"./in/{epname}.mp4")
ita = dn.source(f"./in/2nd/{epname}.mp4")
epis = dn.average([jpn, ita])

planes = dn.split(epis)

y = planes[0]
u = planes[1]
v = planes[2]

y = (
    planes[0]
    .std.Crop(bottom=1)
    .edgefixer.Continuity(top=3, bottom=3, left=3, right=3)
    .std.AddBorders(bottom=1)
)
u = planes[1].edgefixer.Continuity(top=1.5, bottom=1.5, left=1.5, right=1.5)
v = planes[2].edgefixer.Continuity(top=1.5, bottom=1.5, left=1.5, right=1.5)
#
# epis_ef = dn.join([y, u, v])

v.set_output()
# 17621

# dn.join([y, u, v]).set_output()
# epis.set_output()

# core.std.Interleave([jpn, ita]).set_output()
