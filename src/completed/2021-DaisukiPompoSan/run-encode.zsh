#!/usr/bin/env zsh

# import
cd "${0:h}"
source ./funcs.zsh

# default
prepare

# encode
make_log 'start'

if [[ ${part} == 'all' ]]; then
    ${vsx} --rcloneUpload --E e1.vpy
    ${vsx} --unlinkMode e1.vpy

elif [[ ${part} == 'test' ]]; then
    ${vsx} --rcloneUpload --staticName --L e1.vpy
    ${vsx} --rcloneUpload --E --fast_mode e1.vpy

else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
