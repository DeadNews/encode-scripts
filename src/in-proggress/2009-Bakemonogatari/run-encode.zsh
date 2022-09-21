#!/usr/bin/env zsh

# default
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
# ${vsx} --rcloneUpload --L --staticName  op{2,3,5}_aa.py op4{a,b}_aa.py ed{1..3}_aa.py ed_e{5,8}.py op3_filt.py
# ${vsx} --rcloneUpload --EVL  e{1..15}.py op{2,3,5}.py op4{a,b}.py ed{1..3}.py ed_e{5,8}.py
# ${vsx} --unlinkMode op{2,3,5}_aa.py op4{a,b}_aa.py ed{1..3}_aa.py ed_e{5,8}.py op3_filt.py

# ${vsx} --staticName   --L    op{2,3,5}_aa.py op4{a,b}_aa.py ed{1..3}_aa.py ed_e{5,8}.py op3_filt.py
# ${vsx} --rcloneUpload --EVL  e{1..2}.py
# ${vsx} --rcloneUpload --E    op{2,3,5}.py op4{a,b}.py ed{1..3}.py ed_e{5,8}.py

${vsx} --rcloneUpload --EVL e1.py
