import ui

def button_tapped(sender):
	# Get the button's title for the following logic:
	t = sender.title
	global shows_result
	# Get the labels:
	label = sender.superview['viewer_main']
	if label.text_color == (1.0, 0.0, 0.0, 1.0) and label.text == 'ERROR':
		label.text_color = "#311a91"
		label.text = ''
	if t in '0123456789':
		if label.text == '0':
			# Replace 0 or last result with number:
			label.text = t
		else:
			# Append number:
			label.text += t
	elif t == '.' and label.text[-1] != '.':
		# Append decimal point (if not already there)
		label.text += t
	elif t in '+-÷×':
		if label.text[-1] in '+-÷×':
			# Replace current operator
			label.text = label.text[:-1] + t
		else:
			# Append operator
			label.text += t
	elif t == 'AC':
		# Clear All
		label.text = '0'
	elif t == 'del':
		_text = label.text
		if len(_text) == 1 :
			label.text = "0"
		elif len(_text) > 0 and _text != "0":
			label.text = label.text[:-1]
	elif t == '=':
		# Evaluate the result:
		try:
			expr = label.text.replace('÷', '/').replace('×', '*')
			label.text = str(eval(expr))
		except (SyntaxError, ZeroDivisionError):
			label.text = 'ERROR'
			label.text_color = "#ff0000"

v = ui.load_view()
"""
bkgd = ui.ImageView(image=ui.Image("bkgd.png"))
bkgd.send_to_back()
bkgd.height = 160
bkgd.width = 356
bkgd.alpha = 0.5
v.add_subview(bkgd)
"""
viewer = ui.Label()
viewer.font = ('Montserrat Bold', 26)
viewer.text_color = "#212121"
v.add_subview(viewer)
v.present('sheet')
