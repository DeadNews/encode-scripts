#!/usr/bin/env zsh

# import
cd "${0:h}"
source ./funcs.zsh

# default
prepare

# encode
make_log 'start'

if [[ ${part} == 'all' ]]; then
    ${vsx} --unlinkMode e1.vpy
    #     ${vsx} --rcloneUpload --staticName --L e1.vpy
    #     ${vsx} --rcloneUpload --E e1.vpy
    ${vsx} --rcloneUpload --EVL e1.vpy m1.vpy

else
    echo "part: ${part}, nothing to do"
fi

make_log 'end' $?
