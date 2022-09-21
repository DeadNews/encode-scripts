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
    ${vsx} --rcloneUpload --E --fast_mode e1.py

elif [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --E e1.py ed.py

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --E e2.py

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --E e{3..4}.py

elif [[ ${part} == '4' ]]; then
    ${vsx} --rcloneUpload --E e{5..6}.py
    ${vsx} --rcloneUpload --E --keyint 700 --aq-strength 0.7 --crf 16 m1.py

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
