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
    # ${vsx} --unlinkMode e1.vpy
    ${vsx} --rcloneUpload --staticName --L e1.vpy
    ${vsx} --rcloneUpload --E --fast_mode e1.vpy
    ${vsx} --rcloneUpload --E --fast_mode --aq-mode 2 --aq-strength 1.25 e1.vpy

elif [[ ${part} == '1' ]]; then
    # ${vsx} --unlinkMode e1.vpy
    ${vsx} --rcloneUpload --EVL e{1..6}.vpy

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --EVL e{7..12}.vpy

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --EVL e{13..18}.vpy

elif [[ ${part} == '4' ]]; then
    ${vsx} --rcloneUpload --EVL op.vpy e{19..23}.vpy pv{1..3}.vpy
    ${vsx} --rcloneUpload --EVL --keyint -1 --psy-rdoq 1 m{1..4}.vpy

else
    encodeAll
fi
