#!/usr/bin/env zsh

# import
cd "${0:h}"
source ./funcs.zsh

# default
prepare

# encode
make_log 'start'

if [[ ${part} == 'test' ]]; then
    #     ${vsx} --unlinkMode e1.py
    #     ${vsx} --rcloneUpload --staticName --L e1.py
    #     ${vsx} --rcloneUpload --E --fast_mode e1.py
    ${vsx} --rcloneUpload --E e1.py

elif [[ ${part} == 'test2' ]]; then
    # ${vsx} --unlinkMode e1.py
    ${vsx} --rcloneUpload --staticName --L e5.py
    ${vsx} --rcloneUpload --E --fast_mode e5.py

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --E e{1..3}.py op.py

elif [[ ${part} == '4' ]]; then
    ${vsx} --rcloneUpload --E e{4..6}.py

elif [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --E e{7..9}.py

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --E e{10..12}.py ed.py

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
