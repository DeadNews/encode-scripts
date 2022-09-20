#!/usr/bin/env zsh

# default
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
${vsx} --L --staticName op1_aa.py ed{1..2}_aa.py
${vsx} --EVL --rcloneUpload ed{1..2}.py op1.py e{1..13}.py
