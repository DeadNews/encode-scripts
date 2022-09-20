#!/usr/bin/env zsh

# import
cd "${0:h}"
source ./funcs.zsh

# default
prepare

# encode
make_log 'start'

if [[ ${part} == 'test' ]]; then
    #     ${vsx} --unlinkMode e1.vpy
    #     ${vsx} --rcloneUpload --staticName --L e1.vpy
    #     ${vsx} --rcloneUpload --E --fast_mode e1.vpy
    ${vsx} --rcloneUpload --E e1.vpy

elif [[ ${part} == 'test2' ]]; then
    # ${vsx} --unlinkMode e1.vpy
    ${vsx} --rcloneUpload --staticName --L e5.vpy
    ${vsx} --rcloneUpload --E --fast_mode e5.vpy

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --E e{1..3}.vpy op.vpy

elif [[ ${part} == '4' ]]; then
    ${vsx} --rcloneUpload --E e{4..6}.vpy

elif [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --E e{7..9}.vpy

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --E e{10..12}.vpy ed.vpy

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
