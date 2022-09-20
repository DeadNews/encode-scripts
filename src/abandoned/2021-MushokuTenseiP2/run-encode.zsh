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
    ${vsx} --rcloneUpload --E --fast_mode e1.vpy

elif [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --E e1.vpy ed.vpy

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --E e2.vpy

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --E e{3..4}.vpy

elif [[ ${part} == '4' ]]; then
    ${vsx} --rcloneUpload --E e{5..6}.vpy
    ${vsx} --rcloneUpload --E --keyint 700 --aq-strength 0.7 --crf 16 m1.vpy

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
