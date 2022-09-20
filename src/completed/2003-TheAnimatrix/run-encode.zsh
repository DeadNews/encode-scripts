#!/usr/bin/env zsh

# import
cd "${0:h}"
source ./funcs.zsh

# default
prepare

# encode
make_log 'start'

if [[ ${part} == 'test' ]]; then
    ${vsx} --rcloneUpload --staticName --L e{1..9}.vpy
    ${vsx} --rcloneUpload --E --fast_mode e{1..9}.vpy

elif [[ ${part} == 'all' ]]; then
    ${vsx} --unlinkMode e{1..9}.vpy
    ${vsx} --rcloneUpload --staticName --L e{1..9}.vpy
    ${vsx} --rcloneUpload --E e{1..9}.vpy

else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
