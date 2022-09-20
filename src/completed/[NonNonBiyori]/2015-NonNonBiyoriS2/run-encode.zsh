#!/usr/bin/env zsh

# default
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
${vsx} --L --staticName op1_aa.vpy ed{1..2}_aa.vpy
${vsx} --EVL --rcloneUpload ed{1..2}.vpy op1.vpy e{1..13}.vpy
