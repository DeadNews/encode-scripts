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
    ${vsx} --rcloneUpload --E e{1..3}.py

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --E e{4..6}.py

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --E e{7..9}.py

elif [[ ${part} == '4' ]]; then
    ${vsx} --rcloneUpload --E e{10..11}.py ed.py
    ${vsx} --rcloneUpload --E --keyint 300 --aq-strength 0.7 pv.py
    ${vsx} --rcloneUpload --E --keyint 700 --aq-strength 0.7 --crf 16 m{1..2}.py

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
