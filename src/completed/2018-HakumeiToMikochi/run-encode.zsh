#!/usr/bin/env zsh

# default
if [[ -f './part' ]]; then
    part=$(cat './part')
fi
vsx='./run-vspipe-x265.zsh'
chmod u+x ${vsx}

# rm -R ./temp
# encode
encodeAll() {
    ${vsx} --rcloneUpload --EVL e{1..13}.vpy op{1..2}.vpy m{1..4}.vpy ed{1..13}.vpy
}
if [[ ${part} == '1' ]]; then
    ${vsx} --rcloneUpload --EVL e{2..5}.vpy e1.vpy
elif [[ ${part} == '2' ]]; then
    ${vsx} --rcloneUpload --EVL e{6..9}.vpy ed{1..11}.vpy
elif [[ ${part} == '3' ]]; then
    ${vsx} --rcloneUpload --EVL e{10..13}.vpy op{1..2}.vpy ed{12..13}.vpy
    ${vsx} --rcloneUpload --EVL --keyint 700 m{1..4}.vpy
elif [[ ${part} == 'test' ]]; then
    # ${vsx} --unlinkMode e1.vpy
    ${vsx} --rcloneUpload --staticName --L e1.vpy
    ${vsx} --rcloneUpload --E e1.vpy
else
    encodeAll
fi
