#!/usr/bin/env zsh

# import
cd "${0:h}"
source ./funcs.zsh

# default
prepare

# encode
make_log 'start'

if [[ ${part} == 'test' ]]; then
    ${vsx} --unlinkMode e1.vpy
    ${vsx} --rcloneUpload --staticName --L e1.vpy
    ${vsx} --rcloneUpload --E --fast_mode e1.vpy

elif [[ ${part} == '1' ]]; then
    rclone_copy ${part}
    ${vsx} --unlinkMode e1.vpy
    ${vsx} --rcloneUpload --EVL s{1..3}.vpy e{1..3}.vpy

elif [[ ${part} == '2' ]]; then
    rclone_copy ${part}
    ${vsx} --rcloneUpload --EVL s{4..6}.vpy e{4..6}.vpy

elif [[ ${part} == '3' ]]; then
    rclone_copy ${part}
    ${vsx} --rcloneUpload --EVL ed{1..4}.vpy mv.vpy e{7..9}.vpy

elif [[ ${part} == '4' ]]; then
    rclone_copy ${part}
    ${vsx} --rcloneUpload --EVL ed{5..9}.vpy m{1..3}.vpy e{10..12}.vpy

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end'
