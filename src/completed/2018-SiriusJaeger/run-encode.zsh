#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
encodeAll() {
    ${vsx} --rcloneUpload --EVL e{1..12}.py {op,ed}.py
}
if [[ ${part} == '1' ]]; then
    ${vsx} --unlinkMode e1.py
    ${vsx} --staticName --L ed_aa.py
    ${vsx} --rcloneUpload --EVL {op,ed}.py e{1..6}.py

elif [[ ${part} == '2' ]]; then
    ${vsx} --unlinkMode ed_aa.py
    ${vsx} --staticName --L ed_aa.py
    ${vsx} --rcloneUpload --EVL ed.py e{7..12}.py pv{1..3}.py

elif [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.py
    ${vsx} --rcloneUpload --staticName --L e1.py
    ${vsx} --rcloneUpload --E e1.py
    # ${vsx} --rcloneUpload --EVL e1.py
else
    encodeAll
fi
