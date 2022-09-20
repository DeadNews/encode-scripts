#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
encodeAll() {
    ${vsx} --rcloneUpload --EVL e{1..12}.vpy {op,ed}.vpy
}
if [[ ${part} == '1' ]]; then
    ${vsx} --unlinkMode e1.vpy
    ${vsx} --staticName --L ed_aa.vpy
    ${vsx} --rcloneUpload --EVL {op,ed}.vpy e{1..6}.vpy

elif [[ ${part} == '2' ]]; then
    ${vsx} --unlinkMode ed_aa.vpy
    ${vsx} --staticName --L ed_aa.vpy
    ${vsx} --rcloneUpload --EVL ed.vpy e{7..12}.vpy pv{1..3}.vpy

elif [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.vpy
    ${vsx} --rcloneUpload --staticName --L e1.vpy
    ${vsx} --rcloneUpload --E e1.vpy
    # ${vsx} --rcloneUpload --EVL e1.vpy
else
    encodeAll
fi
