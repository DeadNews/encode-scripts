#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# rm -R ./temp

# encode
encodeAll() {
    ${vsx} --staticName --L op1_aa.vpy
    ${vsx} --rcloneUpload --EVL s{1..3}.vpy e{1..11}.vpy {op,ed}1.vpy ed2.vpy
}
if [[ ${part} == '1' ]]; then
    ${vsx} --staticName --L op1_aa.vpy
    ${vsx} --rcloneUpload --EVL op1.vpy e{1..4}.vpy
    # ${vsx} --rcloneUpload --staticName --L e1.vpy
    # ${vsx} --rcloneUpload --E e1_lossless.vpy
elif [[ ${part} == '2' ]]; then
    ${vsx} --staticName --L op1_aa.vpy
    ${vsx} --rcloneUpload --EVL ed1.vpy e{5..8}.vpy
elif [[ ${part} == '3' ]]; then
    ${vsx} --staticName --L op1_aa.vpy
    ${vsx} --rcloneUpload --EVL ed2.vpy s{1..3}.vpy e{9..11}.vpy
else
    encodeAll
fi
