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
    ${vsx} --rcloneUpload --E --fast_mode op.py ed1.py ed2.py e1.py
    ${vsx} --rcloneUpload --E --fast_mode --zones '0,2208,b=0.90' op.py ed1.py ed2.py

elif [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --E e{1..3}.py op.py ed1.py ed2.py

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --E e{4..6}.py

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --E e{7..9}.py

elif [[ ${part} == '4' ]]; then
    ${vsx} --rcloneUpload --E e{10..12}.py

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
