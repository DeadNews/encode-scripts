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
    # ${vsx} --rcloneUpload --staticName --L e1.vpy s{1..4}.vpy m.vpy pv.vpy
    # ${vsx} --rcloneUpload --E --fast_mode e1.vpy s{1..4}.vpy m.vpy pv.vpy
    ${vsx} --rcloneUpload --E --fast_mode e1.vpy

elif [[ ${part} == 'all' ]]; then
    ${vsx} --rcloneUpload --E e1.vpy s{1..4}.vpy
    ${vsx} --rcloneUpload --E --keyint 600 --psy-rdoq 1 --aq-strength 0.85 m.vpy pv.vpy

else
    echo "part: ${part}, nothing to do"
fi

make_log 'end'
