#!/usr/bin/env zsh

# import
cd "${0:h}"
source ./funcs.zsh

# default
prepare

# encode
make_log 'start'

if [[ ${part} == 'test' ]]; then
    ${vsx} --rcloneUpload --E --fast_mode {op,ed}.py e1.py
    # ${vsx} --rcloneUpload --staticName --L {op,ed}.py e1.py
    # ${vsx} --rcloneUpload --E --fast_mode --aq-strength 0.97 --cutree {op,ed}.py e1.py
    # ${vsx} --rcloneUpload --E --fast_mode --crf 16 {op,ed}.py e1.py
    # ${vsx} --unlinkMode {op,ed}.py e1.py

elif [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --E e{1..3}.py {op,ed}.py ed_e3.py

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --E e{4..6}.py
    ${vsx} --rcloneUpload --E --keyint 700 m{1..4}.py f{1..24}.py
    ${vsx} --rcloneUpload --E --keyint 350 pv{1..4}.py

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --E e{7..9}.py s{1..4}.py

elif [[ ${part} == '4' ]]; then
    ${vsx} --rcloneUpload --E e{10..12}.py

elif [[ ${part} == '5' ]]; then
    ${vsx} --rcloneUpload --E e13.py s5.py i{1..16}.py
    ${vsx} --rcloneUpload --E --keyint 700 m5.py f{25..26}.py

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
