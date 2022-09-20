#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
encodeAll() {
    ${vsx} --staticName --L {op,ed}_aa.vpy
    ${vsx} --rcloneUpload --EVL pv{1..3}.vpy {op,ed}.vpy e{1..12}.vpy s{1..6}.vpy
}
if [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.vpy
    ${vsx} --rcloneUpload --staticName --L e1.vpy
    ${vsx} --rcloneUpload --E e1.vpy

elif [[ ${part} == '1' ]]; then
    ${vsx} --staticName --L {op,ed}_aa.vpy
    ${vsx} --rcloneUpload --EVL s{1..6}.vpy e{1..6}.vpy

elif [[ ${part} == '2' ]]; then
    ${vsx} --staticName --L {op,ed}_aa.vpy
    ${vsx} --rcloneUpload --EVL pv{1..3}.vpy {op,ed}.vpy e{7..12}.vpy

else
    encodeAll
fi
