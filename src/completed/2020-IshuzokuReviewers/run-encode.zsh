#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
encodeAll() {
    # ${vsx} --staticName --L {op,ed}_aa.py
    # ${vsx} --rcloneUpload --EVL {op,ed}.py e{1..12}.py
}
if [[ ${part} == 'test' ]]; then
    ${vsx} --unlinkMode e1.py
    ${vsx} --rcloneUpload --staticName --L e1.py
    ${vsx} --rcloneUpload --E e1.py

elif [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --EVL op.py e{1..3}.py

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --EVL ed.py e{4..6}.py

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --EVL m{1..3}.py e{7..9}.py

elif [[ ${part} == '4' ]]; then
    ${vsx} --rcloneUpload --EVL ed_e12.py e{10..12}.py

else
    encodeAll
fi
