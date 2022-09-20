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
    # ${vsx} --rcloneUpload --E --fast_mode e1.vpy
    ${vsx} --rcloneUpload --E e1.vpy

elif [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --EVL e{2..3}.vpy op.vpy

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --EVL e{4..6}.vpy pv.vpy

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --EVL e{7..9}.vpy ed3.vpy

elif [[ ${part} == '4' ]]; then
    ${vsx} --rcloneUpload --EVL e{10..12}.vpy ed4.vpy

elif [[ ${part} == 'e9' ]]; then
    ${vsx} --rcloneUpload --EVL e9.vpy

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
