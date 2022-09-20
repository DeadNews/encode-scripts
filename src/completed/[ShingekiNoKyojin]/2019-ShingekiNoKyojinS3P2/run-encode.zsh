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
    #     ${vsx} --rcloneUpload --staticName --L e1.vpy
    #     ${vsx} --rcloneUpload --E --fast_mode e1.vpy
    ${vsx} --rcloneUpload --E --fast_mode op.vpy ed.vpy e1.vpy

elif [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --E e{1..3}.vpy

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --E --keyint 350 --aq-strength 0.95 s{1..3}.vpy
    ${vsx} --rcloneUpload --E e{4..5}.vpy

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --E e{6..7}.vpy op.vpy ed.vpy

elif [[ ${part} == '4' ]]; then
    ${vsx} --rcloneUpload --E e{8..10}.vpy

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
