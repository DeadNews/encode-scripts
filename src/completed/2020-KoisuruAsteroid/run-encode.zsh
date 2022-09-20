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
    ${vsx} --rcloneUpload --EVL {op,ed}.vpy e{1..12}.vpy
}
if [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.vpy
    ${vsx} --rcloneUpload --staticName --L e1.vpy
    ${vsx} --rcloneUpload --E --fast_mode e1.vpy
    ${vsx} --rcloneUpload --E --fast_mode --aq-strength 1.05 --cutree e1.vpy

elif [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --EVL e{1..3}.vpy {op,ed}1.vpy
    ${vsx} --rcloneUpload --EVL --aq-strength 0.85 t1.vpy

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --EVL {op,ed}2.vpy e{4..6}.vpy

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --EVL {op,ed}3.vpy e{7..9}.vpy

elif [[ ${part} == '4' ]]; then
    ${vsx} --unlinkMode e1.vpy
    ${vsx} --rcloneUpload --EVL e{10..12}.vpy

else
    encodeAll
fi
