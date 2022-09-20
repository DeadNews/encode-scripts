#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
encodeAll() {
    ${vsx} --staticName --L op_aa.vpy
    ${vsx} --rcloneUpload --EVL {op,ed}.vpy e{1..12}.vpy
}
if [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.vpy
    ${vsx} --rcloneUpload --staticName --L e1.vpy
    ${vsx} --rcloneUpload --E --fast_mode e1.vpy
    ${vsx} --rcloneUpload --E --fast_mode --cutree --aq-strength 1.15 e1.vpy

elif [[ ${part} == '1' ]]; then
    # ${vsx} --unlinkMode e1.vpy
    ${vsx} --staticName --L op_aa.vpy
    ${vsx} --rcloneUpload --EVL {op,ed}.vpy e{1..6}.vpy

elif [[ ${part} == '2' ]]; then
    ${vsx} --staticName --L op_aa.vpy
    ${vsx} --rcloneUpload --EVL e{7..12}.vpy

elif [[ ${part} == 'e11' ]]; then
    ${vsx} --rcloneUpload --EVL e11.vpy

else
    encodeAll
fi
