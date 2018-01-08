#!/usr/bin/python
from sys import argv
import zbar
from backend import productExists, addToShoppingList

# create a Processor
proc = zbar.Processor()

# configure the Processor
proc.parse_config('enable')

# initialize the Processor and Grocery list
device = '/dev/video0'
grocery_list_id = '2'
if len(argv) == 3:
	device = argv[1]
	grocery_list_id = argv[2]
else:
	print "Usage:\r\nprocessor.py [video dev source] [grocery list id]\r\n\r\nTest: processor.py /dev/video0 2\r\n-h\t This help :)"
	quit()

proc.init(device)

# setup a callback
def my_handler(proc, image, closure):
    # extract results
    for symbol in image.symbols:
        # do something useful with results
		print 'Looking up product with stripecode '"%s"'' % symbol.data
		product = productExists( symbol.data )
		if product != False:
			print 'Found product \''"%s"'\'' % product
			print 'Adding \''"%s"'\' to your shopping list' % product
			addToShoppingList( grocery_list_id, symbol.data, 1 )
		else:
			print 'Unknown product'

proc.set_data_handler(my_handler)

# enable the preview window
proc.visible = True

# initiate scanning
proc.active = True
try:
    # keep scanning until user provides key/mouse input
    proc.user_wait()
except zbar.WindowClosed, e:
    pass
