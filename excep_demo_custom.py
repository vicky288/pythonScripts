def div(ina,inb):
	try:
		val=ina/inb
		return val
	except ZeroDivisionError:
		print "deno can't be zero"
		return -99999

	except:
		print "unknown excep"
		return -9999

	finally:
		print "final block"

print "val is :%d"%div(10,0)
