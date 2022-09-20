#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
encodeAll() {
    ${vsx} --L --staticName op4_aa.vpy
    ${vsx} --rcloneUpload --EVL e{1..12}.vpy {op,ed}{1..3}.vpy op4.vpy
}
if [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --EVL op{1,2}.vpy ed1.vpy e{1..3}.vpy

elif [[ ${part} == '2' ]]; then
    ${vsx} --L --staticName op4_aa.vpy ed2_aa.vpy
    ${vsx} --rcloneUpload --EVL op{3,4}.vpy ed{2,3}.vpy e{4..12}.vpy

elif [[ ${part} == 'test' ]]; then
    ${vsx} --unlinkMode e1.vpy
    ${vsx} --rcloneUpload --staticName --L e1.vpy
    ${vsx} --rcloneUpload --E e1.vpy
    # ${vsx} --rcloneUpload --EVL e1.vpy

else
    encodeAll
fi
