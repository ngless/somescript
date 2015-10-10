

with open('1301358.txt', 'w') as f:
	for i in range(1, 10000):
		#f.write('微信',i,',',i,')
		#f.write(str(i))
		if i<10:
			i0 = '000'+str(i)
		elif i>=10 and i<100:
			i0 = '00' + str(i)
		elif i>=100 and i<1000:
			i0 = '0' + str(i)
		else:
			i0 = str(i)
			
		vcard='BEGIN:VCARD\n' + 'VERSION:3.0\n' + 'N:;微信1301358'+i0+';;;\n' + 'FN:微信'+ i0 +'\n' + 'TEL;TYPE=CELL:1301358'+ i0 +'\n' + 'ORG:XX\n' + 'TITLE:CEO\n' + 'END:VCARD\n'
		f.write(vcard)
		#f.write('1300163' +i0 +'\n')
		#f.write('BEGIN:VCARD\n')
		#f.write('VERSION:3.0\n')
		#f.write('N:;微信;;;'+str(i)+'\n' )
		#f.write('FN:微信'+str(i)+'\n')
		#f.write('TEL;TYPE=CELL:'+str(i)+'\n')
		#f.write('ORG:XX\n')
		#f.write('TITLE:CEO\n')
		#f.write('END:VCARD\n')