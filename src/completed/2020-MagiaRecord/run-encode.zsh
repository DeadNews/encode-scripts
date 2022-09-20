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
    # ${vsx} --rcloneUpload --E --fast_mode --aq-strength 1.13 --cutree e1.vpy
    ${vsx} --rcloneUpload --E --fast_mode e1.vpy

elif [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --EVL e{1..4}.vpy

elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --E --keyint 1300 --crf 17 --psy-rdoq 1 --cutree m{1..5}.vpy
    ${vsx} --rcloneUpload --EVL e5.vpy
    ${vsx} --rcloneUpload --staticName --L e{6..7}.vpy
    ${vsx} --rcloneUpload --E --fast_mode e{6..7}.vpy

elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --E --cutree pv{1..3}.vpy
    ${vsx} --rcloneUpload --staticName --L e{8..10}.vpy
    ${vsx} --rcloneUpload --E --fast_mode e{8..10}.vpy

elif [[ ${part} == '4' ]]; then
    ${vsx} --rcloneUpload --EVL op{1,2}.vpy ed.vpy
    ${vsx} --rcloneUpload --staticName --L e{11..13}.vpy
    ${vsx} --rcloneUpload --E --fast_mode e{11..13}.vpy

elif [[ ${part} == '2+' ]]; then
    ${vsx} --unlinkMode e{6..7}.vpy
    ${vsx} --rcloneUpload --staticName --L e{6..7}.vpy
    ${vsx} --rcloneUpload --E e{6..7}.vpy

elif [[ ${part} == '3+' ]]; then
    # ${vsx} --unlinkMode e{8..10}.vpy
    rclone_copy_out
    ${vsx} --rcloneUpload --staticName --L e{8..10}.vpy
    # ${vsx} --rcloneUpload --E e{8..10}.vpy
    ${vsx} --rcloneUpload --E e{9..10}.vpy

elif [[ ${part} == '4+' ]]; then
    ${vsx} --unlinkMode e{11..13}.vpy
    ${vsx} --rcloneUpload --staticName --L e{11..13}.vpy
    ${vsx} --rcloneUpload --E e{11..13}.vpy

elif [[ ${part} == 'all' ]]; then
    echo "part: ${part}, nothing to do"
else
    echo "part: ${part}, nothing to do"
fi

make_log 'end'
