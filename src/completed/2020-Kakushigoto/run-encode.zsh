#!/usr/bin/env zsh

# import
cd "${0:h}"
source ./funcs.zsh

# default
prepare

# encode
make_log 'start'

if [[ ${part} == 'test' ]]; then
    # ${vsx} --rcloneUpload --staticName --L {ed,op}.vpy
    # ${vsx} --rcloneUpload --E --fast_mode {ed,op}.vpy
    # ${vsx} --rcloneUpload --E --fast_mode --zones '0,2208,b=0.80' ed.vpy
    # ${vsx} --rcloneUpload --E --fast_mode --zones '0,2208,b=0.70' ed.vpy
    # ${vsx} --rcloneUpload --E --fast_mode --zones '0,2208,b=0.90' op.vpy
    # ${vsx} --rcloneUpload --E --fast_mode --zones '0,2208,b=0.80' op.vpy
    # ${vsx} --unlinkMode {ed,op}.vpy
    ${vsx} --rcloneUpload --E --fast_mode --zones '0,2208,b=0.70' op.vpy
    ${vsx} --rcloneUpload --E --fast_mode e1.vpy

elif [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --EVL e{1..4}.vpy {op,ed}.vpy

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --EVL e{5..8}.vpy
    ${vsx} --rcloneUpload --E --keyint 700 m{1..3}.vpy

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --EVL e{9..10}.vpy

elif [[ ${part} == '4' ]]; then
    ${vsx} --rcloneUpload --EVL e{11..12}.vpy

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
