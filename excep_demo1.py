def div(ina,inb):
	try:
		val=ina/inb
		return val
	except:
		print "deno can't be 0"
		return -9999

	finally:
		print "final block"

print "val is :%d"%div(10,0)
