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
    ${vsx} --rcloneUpload --EVL --fast_mode op.py ed.py e1.py

elif [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --E e{1..3}.py {op,ed}.py

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --E e{4..7}.py
    ${vsx} --rcloneUpload --E --keyint 700 --aq-strength 0.7 --crf 17.5 m{1..6}.py

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --E e{8..10}.py pv.py

elif [[ ${part} == '4' ]]; then
    ${vsx} --rcloneUpload --E e{11..13}.py

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
