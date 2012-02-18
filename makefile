
pyfiles=hcol.py hcut.py hjoin.py
dest=${HOME}/linux/orphan_script

a:
	echo "target??"

install:
	for i in ${pyfiles}; do cp -f $$i ${dest}/; done

uninstall:
	for i in ${pyfiles}; do rm -f ${dest}/$$i; done

