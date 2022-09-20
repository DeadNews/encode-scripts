#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
encodeAll() {
    ${vsx} --staticName --L
    ${vsx} --rcloneUpload --EVL
}
if [[ ${part} == 'test' ]]; then
    ${vsx} --unlinkMode e1.vpy
    # ${vsx} --rcloneUpload --staticName --L e1.vpy
    # ${vsx} --rcloneUpload --E  --fast_mode e1.vpy
    ${vsx} --rcloneUpload --EVL e1.vpy

elif [[ ${part} == '1' ]]; then
    ${vsx} --unlinkMode e1.vpy
    ${vsx} --staticName --L {op,ed}_aa.vpy
    ${vsx} --rcloneUpload --EVL pv.vpy e{1..4}.vpy

elif [[ ${part} == '2' ]]; then
    ${vsx} --staticName --L {op,ed}_aa.vpy
    ${vsx} --rcloneUpload --EVL op.vpy e{5..8}.vpy

elif [[ ${part} == '3' ]]; then
    ${vsx} --staticName --L {op,ed}_aa.vpy
    ${vsx} --rcloneUpload --EVL ed.vpy e{9..12}.vpy

else
    encodeAll
fi
