#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# rm -R ./temp

# encode
encodeAll() {
    ${vsx} --staticName --L op1_aa.py
    ${vsx} --rcloneUpload --EVL s{1..3}.py e{1..11}.py {op,ed}1.py ed2.py
}
if [[ ${part} == '1' ]]; then
    ${vsx} --staticName --L op1_aa.py
    ${vsx} --rcloneUpload --EVL op1.py e{1..4}.py
    # ${vsx} --rcloneUpload --staticName --L e1.py
    # ${vsx} --rcloneUpload --E e1_lossless.py
elif [[ ${part} == '2' ]]; then
    ${vsx} --staticName --L op1_aa.py
    ${vsx} --rcloneUpload --EVL ed1.py e{5..8}.py
elif [[ ${part} == '3' ]]; then
    ${vsx} --staticName --L op1_aa.py
    ${vsx} --rcloneUpload --EVL ed2.py s{1..3}.py e{9..11}.py
else
    encodeAll
fi
