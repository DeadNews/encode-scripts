#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
encodeAll() {
    ${vsx} --staticName --L op{1,2}_aa.vpy
    ${vsx} --rcloneUpload --EVL {op,ed}{1,2}.vpy e{1..24}.vpy
}
if [[ ${part} == 'test' ]]; then
    ${vsx} --unlinkMode e1.vpy
    ${vsx} --rcloneUpload --staticName --L e1.vpy
    ${vsx} --rcloneUpload --E --fast_mode e1.vpy

elif [[ ${part} == '1' ]]; then
    ${vsx} --unlinkMode e1.vpy
    ${vsx} --staticName --L op1_aa.vpy
    ${vsx} --rcloneUpload --EVL op1.vpy e{1..6}.vpy

elif [[ ${part} == '2' ]]; then
    ${vsx} --staticName --L op1_aa.vpy
    ${vsx} --rcloneUpload --EVL ed1.vpy e{7..12}.vpy

elif [[ ${part} == '3' ]]; then
    ${vsx} --staticName --L op2_aa.vpy
    ${vsx} --rcloneUpload --EVL op2.vpy e{13..18}.vpy

elif [[ ${part} == '4' ]]; then
    ${vsx} --staticName --L op2_aa.vpy
    ${vsx} --rcloneUpload --EVL ed2.vpy e{19..24}.vpy

elif [[ ${part} == 'e1' ]]; then
    ${vsx} --rcloneUpload --EVL e1.vpy

else
    encodeAll
fi
