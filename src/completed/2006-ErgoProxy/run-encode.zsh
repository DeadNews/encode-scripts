#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
encodeAll() {
    ${vsx} --staticName --L
    ${vsx} --rcloneUpload --EVL
}
if [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.py
    ${vsx} --rcloneUpload --staticName --L e1.py
    ${vsx} --rcloneUpload --E --fast_mode e1.py
    ${vsx} --rcloneUpload --E --fast_mode --aq-mode 2 --aq-strength 1.25 e1.py

elif [[ ${part} == '1' ]]; then
    # ${vsx} --unlinkMode e1.py
    ${vsx} --rcloneUpload --EVL e{1..6}.py

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --EVL e{7..12}.py

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --EVL e{13..18}.py

elif [[ ${part} == '4' ]]; then
    ${vsx} --rcloneUpload --EVL op.py e{19..23}.py pv{1..3}.py
    ${vsx} --rcloneUpload --EVL --keyint -1 --psy-rdoq 1 m{1..4}.py

else
    encodeAll
fi
