#!/usr/bin/env zsh

# rename
rename -v s1nc s1 */*
rename -v s1e e */*
rename -v s1o o */*

# default
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
${vsx} --L op1_aa.vpy ed{1..2}_aa.vpy
${vsx} --EVL --rcloneUpload ed{1..2}.vpy op1.vpy e{1..13}.vpy
# --staticName
