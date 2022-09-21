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
    ${vsx} --rcloneUpload --EVL {op,ed}.py

elif [[ ${part} == '1' ]]; then
    ${vsx} --unlinkMode e1.py
    ${vsx} --rcloneUpload --EVL e{1..4}.py {op,ed}.py

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --EVL e{5..8}.py

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --EVL e{9..12}.py

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
