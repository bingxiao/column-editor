
pyfiles=hcut.py hjoin.py hhead.py
dest=${HOME}/linux/orphan_script

a:
	echo 'possible targets: install, uninstall'

install:
	for i in ${pyfiles}; do cp -f $$i ${dest}/; done

uninstall:
	for i in ${pyfiles}; do rm -f ${dest}/$$i; done

