#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
encodeAll() {
    ${vsx} --rcloneUpload --EVL e{1..13}.py {op,ed}1.py ed2.py
    ${vsx} --rcloneUpload --EVL --keyint 700 --psy-rdoq 1 --crf 15 pv.py
}

if [[ ${part} == '1' ]]; then
    ${vsx} --unlinkMode e1.py
    ${vsx} --rcloneUpload --EVL {op,ed}1.py ed2.py e{1..8}.py

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --EVL e{9..13}.py

elif [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.py
    ${vsx} --rcloneUpload --staticName --L e1.py
    ${vsx} --rcloneUpload --E e1.py
    # ${vsx} --rcloneUpload --EVL e1.py

else
    encodeAll
fi
