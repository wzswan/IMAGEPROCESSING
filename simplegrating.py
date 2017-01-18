import psychopy.visual
import psychopy.event

win = psychopy.visual.Window(
    size = [300,300],
    units = "pix",
    fullscr = False
    )

grating = psychopy.visual.GratingStim(
    win = win,
    units = "pix",
    size =[250,250]
    )
grating.sf = 50.0/250
grating.draw()

win.flip()
psychopy.event.waitKeys()
win.close()