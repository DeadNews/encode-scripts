#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
encodeAll() {
    ${vsx} --staticName --L {op,ed}{1,2}_aa.py
    ${vsx} --rcloneUpload --EVL e{1..24}.py {op,ed}{1,2}.py pv{1,2}.py
}
if [[ ${part} == '1' ]]; then
    # ${vsx} --staticName   --L   {op,ed}1_aa.py
    # ${vsx} --rcloneUpload --EVL {op,ed}1.py e{1..8}.py pv{2,1}.py

    ${vsx} --rcloneUpload --EVL {op,ed}1.py e{1..8}.py

elif [[ ${part} == '2' ]]; then
    # ${vsx} --staticName   --L   {op,ed}{1,2}_aa.py
    # ${vsx} --rcloneUpload --EVL op2.py e{9..16}.py

    ${vsx} --unlinkMode e10.py
    ${vsx} --rcloneUpload --EVL e{9..16}.py

elif [[ ${part} == '3' ]]; then
    # ${vsx} --staticName   --L   {op,ed}2_aa.py
    # ${vsx} --rcloneUpload --EVL ed2.py e{17..24}.py

    ${vsx} --unlinkMode e18.py
    ${vsx} --rcloneUpload --EVL e{17..24}.py

elif [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.py
    ${vsx} --rcloneUpload --staticName --L e1.py
    ${vsx} --rcloneUpload --E e1.py
    # ${vsx} --rcloneUpload --EVL --crf 14.8  e1.py
    # ${vsx} --rcloneUpload --E --psy-rdoq 3  e1.py

else
    encodeAll
fi
