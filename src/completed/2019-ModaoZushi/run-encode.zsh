#!/usr/bin/env zsh

# import
cd "${0:h}"
source ./funcs.zsh

# default
prepare

# encode
make_log 'start'

if [[ ${part} == 'test' ]]; then
    ${vsx} --rcloneUpload --EVL --fast_mode {op1,ed}.py e1.py

elif [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --EVL e{1..2}.py {op1,ed}.py op2.py

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --EVL e{3..5}.py m{1..3}.py

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --EVL e{6..8}.py

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
