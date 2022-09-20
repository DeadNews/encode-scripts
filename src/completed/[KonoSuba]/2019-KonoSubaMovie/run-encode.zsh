#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
encodeAll() {
    # ${vsx} --unlinkMode e1.vpy
    ${vsx} --rcloneUpload --L --staticName e1.vpy
    ${vsx} --rcloneUpload --E e1.vpy
    ${vsx} --rcloneUpload --EVL --aq-strength 0.85 --keyint 350 pv1.vpy
}
if [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.vpy
    ${vsx} --rcloneUpload --staticName --L e1.vpy
    ${vsx} --rcloneUpload --E --fast_mode e1.vpy

elif [[ ${part} == 'aa' ]]; then
    ${vsx} --rcloneUpload --L --staticName e1_aa.vpy

# elif [[ ${part} == 'ttt' ]]; then
#     ${vsx} --rcloneUpload --T e1.vpy

else
    encodeAll
fi
