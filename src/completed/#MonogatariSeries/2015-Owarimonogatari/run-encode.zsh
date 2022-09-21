#!/usr/bin/env zsh

# default
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
# ${vsx} --L op{1,3}_aa.py ed{1..2}_aa.py
# ${vsx} --rcloneUpload e{1..13}.py ed{1..2}.py op{1..4}.py

# ${vsx} --L --staticName e2.py
# ${vsx} --rcloneUpload e{2,4,10,12}.py
# ${vsx} --unlinkMode e2.py

${vsx} --EVL --rcloneUpload e{4,10,12}.py
rm -R ./temp
