#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
encodeAll() {
    ${vsx} --unlinkMode e1.vpy
    ${vsx} --rcloneUpload --EVL --keyint 700 --psy-rdoq 1 m1.vpy
    ${vsx} --rcloneUpload --L --staticName e1.vpy
    ${vsx} --rcloneUpload --E e1.vpy
}
if [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.vpy
    # ${vsx} --rcloneUpload --staticName --L e1.vpy
    # ${vsx} --rcloneUpload --E e1.vpy
else
    encodeAll
fi
