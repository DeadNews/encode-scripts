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
    ${vsx} --rcloneUpload --E --fast_mode --zones '0,2688,b=0.90' op.vpy
    ${vsx} --rcloneUpload --E --fast_mode --zones '0,2424,b=0.90' ed.vpy
    ${vsx} --rcloneUpload --E --fast_mode --zones '0,2688,b=0.80' op.vpy
    ${vsx} --rcloneUpload --E --fast_mode --zones '0,2424,b=0.80' ed.vpy
    ${vsx} --rcloneUpload --E --fast_mode --zones '0,2688,b=0.70' op.vpy
    ${vsx} --rcloneUpload --E --fast_mode --zones '0,2424,b=0.70' ed.vpy

elif [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --E e{1..3}.vpy {op,ed}.vpy

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --E e{4..6}.vpy

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --E e{7..9}.vpy
    ${vsx} --rcloneUpload --E --keyint 700 --aq-strength 0.8 m{1..4}.vpy

elif [[ ${part} == '4' ]]; then
    ${vsx} --rcloneUpload --E e{10..12}.vpy
    ${vsx} --rcloneUpload --E --keyint 700 --aq-strength 0.8 pv{1..3}.vpy

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
