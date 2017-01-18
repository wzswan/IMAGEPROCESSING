import psychopy.visual
import psychopy.event

win = psychopy.visual.Window(
    size=[255, 255],
    units="pix",
    fullscr=False,
    color=[1, 1, 1]
)

line = psychopy.visual.Line(
    win=win,
    units="pix",
    lineColor=[-1, -1, -1]
)
for i in range(-63,63):
    line.start = [i*2+1,-127]
    line.end = [i*2+1,127]
    line.lineColor = [-1, -1, 1]
    line.lineWidth = 1
    line.draw()

for j in range(-63,63):
    line.start = [-127,j*2+1]
    line.end = [127,j*2+1]
    line.lineColor = [-1, -1, 1]
    line.lineWidth = 1
    line.draw()

win.flip()

psychopy.event.waitKeys()

win.close()