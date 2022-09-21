#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
encodeAll() {
    ${vsx} --L --staticName op4_aa.py
    ${vsx} --rcloneUpload --EVL e{1..12}.py {op,ed}{1..3}.py op4.py
}
if [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --EVL op{1,2}.py ed1.py e{1..3}.py

elif [[ ${part} == '2' ]]; then
    ${vsx} --L --staticName op4_aa.py ed2_aa.py
    ${vsx} --rcloneUpload --EVL op{3,4}.py ed{2,3}.py e{4..12}.py

elif [[ ${part} == 'test' ]]; then
    ${vsx} --unlinkMode e1.py
    ${vsx} --rcloneUpload --staticName --L e1.py
    ${vsx} --rcloneUpload --E e1.py
    # ${vsx} --rcloneUpload --EVL e1.py

else
    encodeAll
fi
