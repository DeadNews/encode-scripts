#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
encodeAll() {
    ${vsx} --rcloneUpload --EVL e{1..13}.vpy {op,ed}1.vpy ed2.vpy
    ${vsx} --rcloneUpload --EVL --keyint 700 --psy-rdoq 1 --crf 15 pv.vpy
}
if [[ ${part} == '1' ]]; then
    ${vsx} --unlinkMode e1.vpy
    ${vsx} --rcloneUpload --EVL {op,ed}1.vpy ed2.vpy e{1..8}.vpy

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --EVL e{9..13}.vpy

elif [[ ${part} == 'test' ]]; then
    ${vsx} --unlinkMode e1.vpy
    ${vsx} --rcloneUpload --staticName --L e1.vpy
    ${vsx} --rcloneUpload --E e1.vpy
    # ${vsx} --rcloneUpload --EVL e1.vpy

else
    encodeAll
fi
