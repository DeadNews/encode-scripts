#!/usr/bin/env zsh

# import
cd "${0:h}"
source ./funcs.zsh

# default
prepare

# encode
make_log 'start'

if [[ ${part} == 'test' ]]; then
    # ${vsx} --rcloneUpload --staticName --L {ed,op}.py
    # ${vsx} --rcloneUpload --E --fast_mode {ed,op}.py
    # ${vsx} --rcloneUpload --E --fast_mode --zones '0,2208,b=0.80' ed.py
    # ${vsx} --rcloneUpload --E --fast_mode --zones '0,2208,b=0.70' ed.py
    # ${vsx} --rcloneUpload --E --fast_mode --zones '0,2208,b=0.90' op.py
    # ${vsx} --rcloneUpload --E --fast_mode --zones '0,2208,b=0.80' op.py
    # ${vsx} --unlinkMode {ed,op}.py
    ${vsx} --rcloneUpload --E --fast_mode --zones '0,2208,b=0.70' op.py
    ${vsx} --rcloneUpload --E --fast_mode e1.py

elif [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --EVL e{1..4}.py {op,ed}.py

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --EVL e{5..8}.py
    ${vsx} --rcloneUpload --E --keyint 700 m{1..3}.py

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --EVL e{9..10}.py

elif [[ ${part} == '4' ]]; then
    ${vsx} --rcloneUpload --EVL e{11..12}.py

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
