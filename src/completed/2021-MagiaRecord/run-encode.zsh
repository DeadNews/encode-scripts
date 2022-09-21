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
    ${vsx} --rcloneUpload --staticName --L {op,ed}.py e1.py
    ${vsx} --rcloneUpload --E --fast_mode --aq-strength 1 --cutree {op,ed}.py e1.py
    ${vsx} --rcloneUpload --E --fast_mode {op,ed}.py e1.py
    ${vsx} --unlinkMode {op,ed}.py e1.py

elif [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --E e{1..2}.py {op,ed}.py

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --E e{3..4}.py
    ${vsx} --rcloneUpload --E --keyint 700 --aq-strength 0.75 --cutree m{1..3}.py

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --E e{5..6}.py

elif [[ ${part} == '4' ]]; then
    ${vsx} --rcloneUpload --E e{7..8}.py

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
