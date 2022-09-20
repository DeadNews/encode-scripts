#!/usr/bin/env zsh

# default
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
# ${vsx} --L op1_aa.py ed{1..2}_aa.py
# ${vsx} --rcloneUpload op1.py ed{1..2}.py
# ${vsx} --EVL --rcloneUpload an.py e{1..4}.py
# ${vsx} --unlinkMode op1_aa.py ed{1..2}_aa.py

# ${vsx} --L op1_aa.py ed1_aa.py
# ${vsx} --EVL --rcloneUpload e{1..4}.py
# ${vsx} --unlinkMode op1_aa.py ed1_aa.py

${vsx} --EVL --rcloneUpload e4.py
