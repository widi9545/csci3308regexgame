pygame.display.update()
resp = None
while 1:
    dispEnd = time.time()
    pygame.mouse.set_visible(True)    
    pygame.event.get()
    ms = pygame.mouse.get_pressed()            
    if ms[0] or ms[2]:
        rt = dispEnd - dispSt                
        if ms[0]:
            resp = 'Yes'
        else:
            resp = 'No'
        break
    if dispEnd - dispSt >= changeDuration:
        break
