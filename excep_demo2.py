def div(ina,inb):
	try:
		val=ina/inb
		return val
	except Exception as ex:
		print ex
		return -9999

	finally:
		print "final block"

print "val is :%d"%div(10,0)
