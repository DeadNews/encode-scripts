#!/usr/bin/env zsh

# default
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
# ${vsx} --L op1_aa.vpy ed{1..2}_aa.vpy
# ${vsx} --rcloneUpload op1.vpy ed{1..2}.vpy
# ${vsx} --EVL --rcloneUpload an.vpy e{1..4}.vpy
# ${vsx} --unlinkMode op1_aa.vpy ed{1..2}_aa.vpy

# ${vsx} --L op1_aa.vpy ed1_aa.vpy
# ${vsx} --EVL --rcloneUpload e{1..4}.vpy
# ${vsx} --unlinkMode op1_aa.vpy ed1_aa.vpy

${vsx} --EVL --rcloneUpload e4.vpy
