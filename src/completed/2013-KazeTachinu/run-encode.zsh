#!/usr/bin/env zsh

# import
cd "${0:h}"
source ./funcs.zsh

# default
prepare

# encode
make_log 'start'

if [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.py
    ${vsx} --rcloneUpload --staticName --L e1.py
    ${vsx} --rcloneUpload --E --fast_mode e1.py

elif [[ ${part} == 'all' ]]; then
    # ${vsx} --unlinkMode e1.py
    ${vsx} --rcloneUpload --E e1.py
    ${vsx} --rcloneUpload --EVL m1.py ed.py

else
    echo "part: ${part}, nothing to do"
fi

make_log 'end'