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
    ${vsx} --rcloneUpload --E --fast_mode op.py ed.py e1.py
    ${vsx} --rcloneUpload --E --fast_mode --zones '0,2208,b=0.90' op.py ed.py

elif [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --E e{1..2}.py {op,ed}.py

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --EVL e{3..4}.py
    ${vsx} --rcloneUpload --EVL --keyint 700 m{1..2}.py

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --E e{5..7}.py

elif [[ ${part} == '4' ]]; then
    ${vsx} --rcloneUpload --E e{8..10}.py

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
