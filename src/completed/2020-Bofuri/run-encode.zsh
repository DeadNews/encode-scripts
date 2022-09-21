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
    ${vsx} --rcloneUpload --EVL {op,ed}.py e{1..12}.py
}
if [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.py
    ${vsx} --rcloneUpload --staticName --L e1.py
    ${vsx} --rcloneUpload --E e1.py

elif [[ ${part} == '1' ]]; then
    ${vsx} --staticName --L {op,ed}_aa.py
    ${vsx} --rcloneUpload --EVL {op,ed}.py e{1..4}.py

elif [[ ${part} == '2' ]]; then
    ${vsx} --staticName --L {op,ed}_aa.py
    ${vsx} --rcloneUpload --EVL e{5..8}.py

elif [[ ${part} == '3' ]]; then
    ${vsx} --staticName --L {op,ed}_aa.py
    ${vsx} --rcloneUpload --EVL e{9..12}.py

else
    encodeAll
fi
