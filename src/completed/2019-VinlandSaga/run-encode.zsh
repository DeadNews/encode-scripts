#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
encodeAll() {
    ${vsx} --staticName --L op{1,2}_aa.py
    ${vsx} --rcloneUpload --EVL {op,ed}{1,2}.py e{1..24}.py
}
if [[ ${part} == 'test' ]]; then
    ${vsx} --unlinkMode e1.py
    ${vsx} --rcloneUpload --staticName --L e1.py
    ${vsx} --rcloneUpload --E --fast_mode e1.py

elif [[ ${part} == '1' ]]; then
    ${vsx} --unlinkMode e1.py
    ${vsx} --staticName --L op1_aa.py
    ${vsx} --rcloneUpload --EVL op1.py e{1..6}.py

elif [[ ${part} == '2' ]]; then
    ${vsx} --staticName --L op1_aa.py
    ${vsx} --rcloneUpload --EVL ed1.py e{7..12}.py

elif [[ ${part} == '3' ]]; then
    ${vsx} --staticName --L op2_aa.py
    ${vsx} --rcloneUpload --EVL op2.py e{13..18}.py

elif [[ ${part} == '4' ]]; then
    ${vsx} --staticName --L op2_aa.py
    ${vsx} --rcloneUpload --EVL ed2.py e{19..24}.py

elif [[ ${part} == 'e1' ]]; then
    ${vsx} --rcloneUpload --EVL e1.py

else
    encodeAll
fi
