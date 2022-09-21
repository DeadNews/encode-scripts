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
    ${vsx} --rcloneUpload --E --fast_mode e1.py
    ${vsx} --rcloneUpload --E --fast_mode --aq-strength 1.05 --cutree e1.py

elif [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --EVL e{1..3}.py {op,ed}1.py
    ${vsx} --rcloneUpload --EVL --aq-strength 0.85 t1.py

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --EVL {op,ed}2.py e{4..6}.py

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --EVL {op,ed}3.py e{7..9}.py

elif [[ ${part} == '4' ]]; then
    ${vsx} --unlinkMode e1.py
    ${vsx} --rcloneUpload --EVL e{10..12}.py

else
    encodeAll
fi
