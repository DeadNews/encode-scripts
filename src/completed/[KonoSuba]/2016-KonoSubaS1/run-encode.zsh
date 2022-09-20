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
    ${vsx} --rcloneUpload --EVL --keyint 1100 pv.vpy
    ${vsx} --rcloneUpload --EVL {op,ed}.vpy e{1..11}.vpy
}
if [[ ${part} == 'test_s3' ]]; then
    # ${vsx} --staticName --L {op,ed}_aa.vpy
    ${vsx} --unlinkMode e8.vpy
    ${vsx} --rcloneUpload --staticName --L e8.vpy
    ${vsx} --rcloneUpload --E e8.vpy

elif [[ ${part} == 'e8' ]]; then
    ${vsx} --rcloneUpload --EVL e8.vpy

else
    encodeAll
fi
