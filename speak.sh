status=`ps aux| grep espeak|  awk '{print $2}'`

echo $status
salut=`echo $status | sed 's@^[^0-9]*\([0-9]\+\).*@\1@'`
echo $salut
ok=`kill -9 $salut`

exit 0

