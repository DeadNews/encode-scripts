#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(< './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
# rm -R ./temp/
if [[ ${part} == 1 ]]; then
    ${vsx} --rcloneUpload --EVL e1.py op1.py ed1.py
    ${vsx} --rcloneUpload --EVL --psy-rd 1 m1.py
elif [[ ${part} == 2 ]]; then
    ${vsx} --rcloneUpload --EVL e2.py
    ${vsx} --rcloneUpload --EVL --psy-rd 1 m2.py
elif [[ ${part} == 3 ]]; then
    ${vsx} --rcloneUpload --EVL e3.py op3.py ed3.py
    ${vsx} --rcloneUpload --EVL --psy-rd 1 m31.py m32.py
fi
