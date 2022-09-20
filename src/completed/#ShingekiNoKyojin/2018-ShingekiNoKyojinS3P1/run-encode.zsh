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
    ${vsx} --rcloneUpload --E --fast_mode op.py ed.py e3.py

elif [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --E e{1..3}.py op.py
    ${vsx} --rcloneUpload --E --keyint 350 --aq-strength 0.95 s1.py

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --E e{4..6}.py
    ${vsx} --rcloneUpload --E --keyint 350 --aq-strength 0.95 s2.py

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --E e{7..9}.py
    ${vsx} --rcloneUpload --E --keyint 350 --aq-strength 0.95 s3.py

elif [[ ${part} == '4' ]]; then
    ${vsx} --rcloneUpload --E e{10..12}.py ed.py
    ${vsx} --rcloneUpload --E --keyint 350 --aq-strength 0.95 s4.py

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
