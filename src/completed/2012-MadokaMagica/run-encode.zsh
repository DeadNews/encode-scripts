#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(<'./part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
# rm -R ./temp/
if [[ ${part} == 1 ]]; then
    ${vsx} --rcloneUpload --EVL e1.vpy op1.vpy ed1.vpy
    ${vsx} --rcloneUpload --EVL --psy-rd 1 m1.vpy
elif [[ ${part} == 2 ]]; then
    ${vsx} --rcloneUpload --EVL e2.vpy
    ${vsx} --rcloneUpload --EVL --psy-rd 1 m2.vpy
elif [[ ${part} == 3 ]]; then
    ${vsx} --rcloneUpload --EVL e3.vpy op3.vpy ed3.vpy
    ${vsx} --rcloneUpload --EVL --psy-rd 1 m31.vpy m32.vpy
fi
