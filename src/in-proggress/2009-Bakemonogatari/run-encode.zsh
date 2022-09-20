#!/usr/bin/env zsh

# default
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
# ${vsx} --rcloneUpload --L --staticName  op{2,3,5}_aa.vpy op4{a,b}_aa.vpy ed{1..3}_aa.vpy ed_e{5,8}.vpy op3_filt.vpy
# ${vsx} --rcloneUpload --EVL  e{1..15}.vpy op{2,3,5}.vpy op4{a,b}.vpy ed{1..3}.vpy ed_e{5,8}.vpy
# ${vsx} --unlinkMode op{2,3,5}_aa.vpy op4{a,b}_aa.vpy ed{1..3}_aa.vpy ed_e{5,8}.vpy op3_filt.vpy

# ${vsx} --staticName   --L    op{2,3,5}_aa.vpy op4{a,b}_aa.vpy ed{1..3}_aa.vpy ed_e{5,8}.vpy op3_filt.vpy
# ${vsx} --rcloneUpload --EVL  e{1..2}.vpy
# ${vsx} --rcloneUpload --E    op{2,3,5}.vpy op4{a,b}.vpy ed{1..3}.vpy ed_e{5,8}.vpy

${vsx} --rcloneUpload --EVL e1.vpy
