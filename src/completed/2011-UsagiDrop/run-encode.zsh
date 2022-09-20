#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
encodeAll() {
    ${vsx} --rcloneUpload --EVL e{1..11}.py s{1..4}.py op{1..4}.py ed{1..11}.py
}
if [[ ${part} == '1' ]]; then
    ${vsx} --unlinkMode e1.py
    ${vsx} --rcloneUpload --EVL e{1..6}.py s{1..4}.py ed{1..6}.py
elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --EVL e{7..11}.py op{1..4}.py ed{7..11}.py
elif [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.py
    ${vsx} --rcloneUpload --staticName --L e1.py
    ${vsx} --rcloneUpload --E e1.py
else
    encodeAll
fi
