#!/usr/bin/env zsh

# import
cd "${0:h}"
source ./funcs.zsh

# default
prepare

# encode
make_log 'start'

if [[ ${part} == 'test' ]]; then
    #     ${vsx} --unlinkMode e4.py
    ${vsx} --rcloneUpload --staticName --L e4.py
    ${vsx} --rcloneUpload --E e4.py
    ${vsx} --rcloneUpload --EVL {op1,ed}.py
    ${vsx} --rcloneUpload --EVL m1.py

elif [[ ${part} == '1' ]]; then
    ${vsx} --unlinkMode e4.py
    ${vsx} --rcloneUpload --EVL e{1..5}.py

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --EVL e{6..10}.py {op1,ed}.py op2.py

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --EVL e{11..15}.py m{1..4}.py

elif
    [[ ${part} == 'all' ]]
then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
