#!/usr/bin/env zsh

# default
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
# ${vsx} --L op{1,3}_aa.vpy ed{1..2}_aa.vpy
# ${vsx} --rcloneUpload e{1..13}.vpy ed{1..2}.vpy op{1..4}.vpy

# ${vsx} --L --staticName e2.vpy
# ${vsx} --rcloneUpload e{2,4,10,12}.vpy
# ${vsx} --unlinkMode e2.vpy

${vsx} --EVL --rcloneUpload e{4,10,12}.vpy
rm -R ./temp
