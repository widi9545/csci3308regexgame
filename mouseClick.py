import simplegui

click_pos = [] 

click = []

def draw(canvas):
	
	if len(click) > 0:
		pre = click[0]; 
		for i in click:
			canvas.draw_line(pre, i, 5, 'Blue')
			pre = i

def do_on_click(clicked_position):
	click.append(clicked_position)
	print "you clicked at ", clicked_position
	


frame = simplegui.create_frame("Mouse", 400,400)
frame.set_canvas_background("white")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(do_on_click)


frame.start()
