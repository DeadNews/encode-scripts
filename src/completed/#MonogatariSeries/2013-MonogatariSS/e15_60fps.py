import dnfunc as dn
import easyvfr

clip = dn.source("./temp/e15_lossless.mp4")
# smooth = dn.to60fps(clip, mode='svp')
# clip = dn.to60fps(clip, mode='mv')
# smooth.std.Trim(27196, 28996).set_output()

# 60 fps: [0:2733] [4269:5977] [7603:11725] [13819:14754]  [16426:17338] [17728:18535]  [23368:24572] [26272:28103]

clips = [
    dn.to60fps(clip[:2734]),
    clip[2734:4269],
    dn.to60fps(clip[4269:5978]),
    clip[5978:7603],
    dn.to60fps(clip[7603:11726]),
    clip[11726:13819],
    dn.to60fps(clip[13819:14755]),
    clip[14755:16426],
    dn.to60fps(clip[16426:17339]),
    clip[17339:17728],
    dn.to60fps(clip[17728:18536]),
    clip[18536:23368],
    dn.to60fps(clip[23368:24573]),
    clip[24573:26272],
    dn.to60fps(clip[26272:27856]),
    clip[27856:27886],
    dn.to60fps(clip[27886:28104]),
    clip[28104:37481],
]
vfr = easyvfr.EasyVFR(clips)
vfr.write_tcq("./tcq/files")
vfr.splice_clips().set_output()
