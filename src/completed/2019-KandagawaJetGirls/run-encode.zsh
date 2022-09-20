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
    ${vsx} --unlinkMode e1.vpy
    ${vsx} --staticName --L {op,ed}_aa.vpy
    ${vsx} --rcloneUpload --EVL e{1..4}.vpy
elif [[ ${part} == '2' ]]; then
    ${vsx} --staticName --L {op,ed}_aa.vpy
    ${vsx} --rcloneUpload --EVL e{5..7}.vpy op.vpy

elif [[ ${part} == '3' ]]; then
    ${vsx} --staticName --L {op,ed}_aa.vpy
    ${vsx} --rcloneUpload --EVL e{8..10}.vpy ed.vpy

elif [[ ${part} == '4' ]]; then
    ${vsx} --staticName --L {op,ed}_aa.vpy
    ${vsx} --rcloneUpload --EVL e{11..13}.vpy pv.vpy

else
    encodeAll
fi
