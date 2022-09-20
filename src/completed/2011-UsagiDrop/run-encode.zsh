#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# encode
encodeAll() {
    ${vsx} --rcloneUpload --EVL e{1..11}.vpy s{1..4}.vpy op{1..4}.vpy ed{1..11}.vpy
}
if [[ ${part} == '1' ]]; then
    ${vsx} --unlinkMode e1.vpy
    ${vsx} --rcloneUpload --EVL e{1..6}.vpy s{1..4}.vpy ed{1..6}.vpy
elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --EVL e{7..11}.vpy op{1..4}.vpy ed{7..11}.vpy
elif [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.vpy
    ${vsx} --rcloneUpload --staticName --L e1.vpy
    ${vsx} --rcloneUpload --E e1.vpy
else
    encodeAll
fi
