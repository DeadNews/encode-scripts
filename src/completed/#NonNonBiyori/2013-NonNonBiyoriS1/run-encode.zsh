#!/usr/bin/env zsh

# rename
rename -v s1nc s1 */*
rename -v s1e e */*
rename -v s1o o */*

# default
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
${vsx} --L op1_aa.py ed{1..2}_aa.py
${vsx} --EVL --rcloneUpload ed{1..2}.py op1.py e{1..13}.py
# --staticName
