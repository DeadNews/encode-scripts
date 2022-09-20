#!/usr/bin/env zsh

# import
cd "${0:h}"
source ./funcs.zsh

# default
prepare

# encode
make_log 'start'

if [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.py
    ${vsx} --rcloneUpload --staticName --L e1.py
    ${vsx} --rcloneUpload --E e1.py

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --E e{1..7}.py

elif [[ ${part} == '4' ]]; then
    ${vsx} --rcloneUpload --E e{8..13}.py {op,ed}1.py
    ${vsx} --rcloneUpload --E --aq-strength 0.95 s{1..2}.py

elif [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --E e{14..19}.py {op,ed}2.py
    ${vsx} --rcloneUpload --E --aq-strength 0.95 s{3..4}.py

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --E e{20..25}.py
    ${vsx} --rcloneUpload --E --aq-strength 0.95 s{5..9}.py

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
