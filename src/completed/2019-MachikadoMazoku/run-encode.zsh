#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
encodeAll() {
    # ${vsx} --staticName   --L   {op,ed}_aa.py
    ${vsx} --rcloneUpload --EVL {op,ed}.py e{1..12}.py
    ${vsx} --rcloneUpload --EVL --keyint 700 --psy-rdoq 1 s{1..4}.py pv{1..4}.py m{1..4}.py
}
if [[ ${part} == '1' ]]; then
    # ${vsx} --rcloneUpload --EVL e{1..6}.py
    ${vsx} --unlinkMode e1.py
    ${vsx} --rcloneUpload --EVL e{2..6}.py

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --EVL --keyint 700 --psy-rdoq 1 s{2..3}.py pv{2..3}.py m{2..3}.py
    ${vsx} --rcloneUpload --EVL e{7..9}.py
    # ${vsx} --rcloneUpload --EVL --keyint 700 --psy-rdoq 1 {op,ed}.py s{1..3}.py pv{1..3}.py m{1..3}.py

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --EVL --keyint 700 --psy-rdoq 1 s4.py pv4.py m4.py
    ${vsx} --rcloneUpload --EVL e{10..12}.py

elif [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.py
    ${vsx} --rcloneUpload --staticName --L e1.py
    ${vsx} --rcloneUpload --E e1.py
else
    encodeAll
fi
