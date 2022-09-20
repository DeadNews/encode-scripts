#!/usr/bin/env zsh

# import
cd "${0:h}"
source ./funcs.zsh

# default
prepare

# encode
make_log 'start'

if [[ ${part} == 'test' ]]; then
    ${vsx} --rcloneUpload --staticName --L e1.vpy
    ${vsx} --rcloneUpload --E --fast_mode e1.vpy
    ${vsx} --rcloneUpload --E --fast_mode --cutree --aq-strength 1.15 e1.vpy
    ${vsx} --unlinkMode e1.vpy
    ${vsx} --rcloneUpload --E --fast_mode s{1..2}.vpy
    ${vsx} --rcloneUpload --E --fast_mode --keyint 700 m{1..4}.vpy

elif [[ ${part} == 'all' ]]; then
    ${vsx} --rcloneUpload --E e1.vpy s{1..3}.vpy
    ${vsx} --rcloneUpload --E --keyint 700 m{1..4}.vpy

else
    echo "part: ${part}, nothing to do"
fi

make_log 'end'
