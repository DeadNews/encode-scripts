#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
encodeAll() {
    ${vsx} --staticName --L {op,ed}1_aa.vpy op2_aa.vpy
    ${vsx} --rcloneUpload --EVL e{1..22}.vpy {op,ed}1.vpy {op,ed}2.vpy ed3.vpy m{1..8}.vpy
}
if [[ ${part} == '1' ]]; then
    ${vsx} --staticName --L {op,ed}1_aa.vpy
    ${vsx} --rcloneUpload --EVL e{1..11}.vpy {op,ed}1.vpy m{1..8}.vpy

elif [[ ${part} == '2' ]]; then
    ${vsx} --staticName --L op2_aa.vpy
    ${vsx} --rcloneUpload --EVL e{12..22}.vpy {op,ed}2.vpy ed3.vpy

elif [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.vpy
    ${vsx} --rcloneUpload --staticName --L e1.vpy
    ${vsx} --rcloneUpload --E e1.vpy

else
    encodeAll
fi
