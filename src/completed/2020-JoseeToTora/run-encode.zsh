#!/usr/bin/env zsh

# import
cd "${0:h}"
source ./funcs.zsh

# default
prepare

# encode
make_log 'start'

if [[ ${part} == 'all' ]]; then
    ${vsx} --rcloneUpload --staticName --L e1.py
    ${vsx} --rcloneUpload --E e1.py
    ${vsx} --rcloneUpload --EVL --keyint 700 m1.py

else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
