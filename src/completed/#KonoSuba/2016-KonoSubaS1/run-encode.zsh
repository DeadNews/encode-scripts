#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
encodeAll() {
    ${vsx} --staticName --L {op,ed}_aa.py
    ${vsx} --rcloneUpload --EVL --keyint 1100 pv.py
    ${vsx} --rcloneUpload --EVL {op,ed}.py e{1..11}.py
}
if [[ ${part} == 'test_s3' ]]; then
    # ${vsx} --staticName --L {op,ed}_aa.py
    ${vsx} --unlinkMode e8.py
    ${vsx} --rcloneUpload --staticName --L e8.py
    ${vsx} --rcloneUpload --E e8.py

elif [[ ${part} == 'e8' ]]; then
    ${vsx} --rcloneUpload --EVL e8.py

else
    encodeAll
fi
