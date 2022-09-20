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
    ${vsx} --rcloneUpload --E --fast_mode op.vpy ed.vpy e1.vpy
    ${vsx} --rcloneUpload --E --fast_mode --zones '0,2208,b=0.90' op.vpy ed.vpy

elif [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --E e{1..2}.vpy {op,ed}.vpy

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --EVL e{3..4}.vpy
    ${vsx} --rcloneUpload --EVL --keyint 700 m{1..2}.vpy

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --E e{5..7}.vpy

elif [[ ${part} == '4' ]]; then
    ${vsx} --rcloneUpload --E e{8..10}.vpy

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
