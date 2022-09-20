#!/usr/bin/env zsh

# import
cd "${0:h}"
source ./funcs.zsh

# default
prepare

# encode
make_log 'start'

if [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.vpy
    ${vsx} --rcloneUpload --staticName --L e1.vpy
    ${vsx} --rcloneUpload --E e1.vpy

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --E e{1..7}.vpy

elif [[ ${part} == '4' ]]; then
    ${vsx} --rcloneUpload --E e{8..13}.vpy {op,ed}1.vpy
    ${vsx} --rcloneUpload --E --aq-strength 0.95 s{1..2}.vpy

elif [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --E e{14..19}.vpy {op,ed}2.vpy
    ${vsx} --rcloneUpload --E --aq-strength 0.95 s{3..4}.vpy

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --E e{20..25}.vpy
    ${vsx} --rcloneUpload --E --aq-strength 0.95 s{5..9}.vpy

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
