#!/usr/bin/env zsh

# import
cd "${0:h}"
source ./funcs.zsh

# default
prepare

# encode
make_log 'start'

if [[ ${part} == 'test' ]]; then
    ${vsx} --unlinkMode e1.py
    ${vsx} --rcloneUpload --staticName --L e1.py
    ${vsx} --rcloneUpload --E --fast_mode e1.py

elif [[ ${part} == 'test2' ]]; then
    # ${vsx} --unlinkMode e4.py
    ${vsx} --rcloneUpload --staticName --L e4.py
    ${vsx} --rcloneUpload --E --fast_mode e4.py

elif [[ ${part} == '1' ]]; then
    rclone_copy ${part}
    ${vsx} --unlinkMode e1.py
    ${vsx} --rcloneUpload --EVL op.py e{1..3}.py

elif [[ ${part} == '2' ]]; then
    rclone_copy ${part}
    ${vsx} --rcloneUpload --EVL ed.py e{4..6}.py

elif [[ ${part} == '3' ]]; then
    rclone_copy ${part}
    ${vsx} --rcloneUpload --EVL m{1..2}.py e{7..9}.py

elif [[ ${part} == '4' ]]; then
    rclone_copy ${part}
    ${vsx} --rcloneUpload --EVL pv.py e{10..12}.py

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end'
