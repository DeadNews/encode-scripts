#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
encodeAll() {
    ${vsx} --staticName --L op_aa.py
    ${vsx} --rcloneUpload --EVL {op,ed}.py e{1..12}.py
}
if [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.py
    ${vsx} --rcloneUpload --staticName --L e1.py
    ${vsx} --rcloneUpload --E --fast_mode e1.py
    ${vsx} --rcloneUpload --E --fast_mode --cutree --aq-strength 1.15 e1.py

elif [[ ${part} == '1' ]]; then
    # ${vsx} --unlinkMode e1.py
    ${vsx} --staticName --L op_aa.py
    ${vsx} --rcloneUpload --EVL {op,ed}.py e{1..6}.py

elif [[ ${part} == '2' ]]; then
    ${vsx} --staticName --L op_aa.py
    ${vsx} --rcloneUpload --EVL e{7..12}.py

elif [[ ${part} == 'e11' ]]; then
    ${vsx} --rcloneUpload --EVL e11.py

else
    encodeAll
fi
