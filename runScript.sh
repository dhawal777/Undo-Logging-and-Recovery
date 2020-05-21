a=0
b=1
for var in "$@"
do
    a=`expr $a + $b`
done

if [ $a == 2 ]
then
	python2 UndoLogging.py $1 $2
else
	python2 UndoRecovery.py $1
fi