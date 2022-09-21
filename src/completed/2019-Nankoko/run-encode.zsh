#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
encodeAll() {
    ${vsx} --staticName --L {op,ed}{1..4}_aa.py ed5_aa.py
    ${vsx} --rcloneUpload --EVL e{1..13}.py
}
if [[ ${part} == '1' ]]; then
    ${vsx} --staticName --L {op,ed}{1..2}_aa.py
    # ${vsx} --rcloneUpload --EVL {op,ed}{1..2}.py e{1..6}.py
    ${vsx} --rcloneUpload --EVL e{1..6}.py
elif [[ ${part} == '2' ]]; then
    ${vsx} --staticName --L {op,ed}{3..4}_aa.py ed5_aa.py
    # ${vsx} --rcloneUpload --EVL {op,ed}{3..4}.py ed5.py e{7..13}.py
    ${vsx} --rcloneUpload --EVL e{7..13}.py
elif [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.py
    # ${vsx} --rcloneUpload --staticName --L e1.py
    # ${vsx} --rcloneUpload --E e1.py
    ${vsx} --rcloneUpload --EVL e1.py
else
    encodeAll
fi
