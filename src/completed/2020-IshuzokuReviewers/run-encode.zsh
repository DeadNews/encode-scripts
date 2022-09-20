#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
encodeAll() {
    # ${vsx} --staticName --L {op,ed}_aa.vpy
    # ${vsx} --rcloneUpload --EVL {op,ed}.vpy e{1..12}.vpy
}
if [[ ${part} == 'test' ]]; then
    ${vsx} --unlinkMode e1.vpy
    ${vsx} --rcloneUpload --staticName --L e1.vpy
    ${vsx} --rcloneUpload --E e1.vpy

elif [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --EVL op.vpy e{1..3}.vpy

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --EVL ed.vpy e{4..6}.vpy

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --EVL m{1..3}.vpy e{7..9}.vpy

elif [[ ${part} == '4' ]]; then
    ${vsx} --rcloneUpload --EVL ed_e12.vpy e{10..12}.vpy

else
    encodeAll
fi
