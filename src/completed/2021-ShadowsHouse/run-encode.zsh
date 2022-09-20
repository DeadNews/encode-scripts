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
    ${vsx} --rcloneUpload --EVL --fast_mode op.vpy ed.vpy e1.vpy

elif [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --E e{1..3}.vpy {op,ed}.vpy

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --E e{4..7}.vpy
    ${vsx} --rcloneUpload --E --keyint 700 --aq-strength 0.7 --crf 17.5 m{1..6}.vpy

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --E e{8..10}.vpy pv.vpy

elif [[ ${part} == '4' ]]; then
    ${vsx} --rcloneUpload --E e{11..13}.vpy

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
