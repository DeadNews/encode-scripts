#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
encodeAll() {
    ${vsx} --staticName --L {op,ed}{1..4}_aa.vpy ed5_aa.vpy
    ${vsx} --rcloneUpload --EVL e{1..13}.vpy
}
if [[ ${part} == '1' ]]; then
    ${vsx} --staticName --L {op,ed}{1..2}_aa.vpy
    # ${vsx} --rcloneUpload --EVL {op,ed}{1..2}.vpy e{1..6}.vpy
    ${vsx} --rcloneUpload --EVL e{1..6}.vpy
elif [[ ${part} == '2' ]]; then
    ${vsx} --staticName --L {op,ed}{3..4}_aa.vpy ed5_aa.vpy
    # ${vsx} --rcloneUpload --EVL {op,ed}{3..4}.vpy ed5.vpy e{7..13}.vpy
    ${vsx} --rcloneUpload --EVL e{7..13}.vpy
elif [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.vpy
    # ${vsx} --rcloneUpload --staticName --L e1.vpy
    # ${vsx} --rcloneUpload --E e1.vpy
    ${vsx} --rcloneUpload --EVL e1.vpy
else
    encodeAll
fi
