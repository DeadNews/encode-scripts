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
    ${vsx} --staticName --L {op,ed}2_aa.py op1_aa.py
    ${vsx} --rcloneUpload --EVL e{1..22}.py {op,ed}{1,2}.py ed3.py m{1..8}.py
}
if [[ ${part} == '1' ]]; then
    ${vsx} --staticName --L op1_aa.py ed2_aa.py
    ${vsx} --rcloneUpload --EVL e{1..11}.py {op,ed}1.py ed2.py m{1..8}.py
elif [[ ${part} == '2' ]]; then
    ${vsx} --staticName --L op2_aa.py
    ${vsx} --rcloneUpload --EVL e{12..22}.py op2.py ed3.py
elif [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.py
    ${vsx} --rcloneUpload --staticName --L e1.py
    ${vsx} --rcloneUpload --E e1.py
else
    encodeAll
fi
