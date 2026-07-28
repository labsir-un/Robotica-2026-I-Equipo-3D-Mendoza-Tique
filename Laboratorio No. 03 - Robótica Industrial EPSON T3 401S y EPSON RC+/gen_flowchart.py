import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(figsize=(10, 18))
ax.set_xlim(0, 10)
ax.set_ylim(0, 18)
ax.axis('off')
fig.patch.set_facecolor('#FAFAFA')

def rect(ax, x, y, w, h, text, color='#D6EAF8', fontsize=9):
    box = FancyBboxPatch((x - w/2, y - h/2), w, h,
                         boxstyle="round,pad=0.15",
                         linewidth=1.2, edgecolor='#2C3E50', facecolor=color, zorder=3)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            fontfamily='monospace', zorder=4, multialignment='center')

def diamond(ax, x, y, w, h, text, color='#FDEBD0', fontsize=8.5):
    dx, dy = w/2, h/2
    xs = [x, x+dx, x, x-dx, x]
    ys = [y+dy, y, y-dy, y, y+dy]
    ax.fill(xs, ys, color=color, zorder=3)
    ax.plot(xs, ys, color='#2C3E50', linewidth=1.2, zorder=4)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            fontfamily='monospace', zorder=5, multialignment='center')

def oval(ax, x, y, w, h, text, color='#D5F5E3', fontsize=9):
    ell = mpatches.Ellipse((x, y), w, h, linewidth=1.2,
                            edgecolor='#2C3E50', facecolor=color, zorder=3)
    ax.add_patch(ell)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            fontfamily='monospace', zorder=4)

def arrow(ax, x1, y1, x2, y2, label='', lx=None, ly=None):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color='#2C3E50', lw=1.3), zorder=2)
    if label:
        lx = lx if lx else (x1+x2)/2 + 0.15
        ly = ly if ly else (y1+y2)/2
        ax.text(lx, ly, label, fontsize=7.5, color='#1A5276', fontfamily='monospace')

# INICIO
oval(ax, 5, 17.2, 2.2, 0.7, 'INICIO')
arrow(ax, 5, 16.85, 5, 16.3)

# Motor ON
rect(ax, 5, 15.9, 7.0, 0.7, 'Motor ON  |  Power High  |  Accel 50/50  |  Speed 30')
arrow(ax, 5, 15.55, 5, 15.0)

# Pallet
rect(ax, 5, 14.6, 6.5, 0.7, 'Pallet 1 (Origin, PuntoX, PuntoY, 6x5)')
arrow(ax, 5, 14.25, 5, 13.7)

# InitTour
rect(ax, 5, 13.3, 6.5, 0.7, 'InitTour()  ->  secuencia 30 posiciones (patron caballo)')
arrow(ax, 5, 12.95, 5, 12.4)

# InitOcc
rect(ax, 5, 12.0, 6.5, 0.7, 'InitOcc()  ->  Huevo A: pos 1  |  Huevo B: pos 30')
arrow(ax, 5, 11.65, 5, 11.1)

# Decision impar
diamond(ax, 5, 10.5, 4.0, 0.9, 'sIndex impar?')

# rama SI (izquierda)
ax.annotate('', xy=(2.2, 10.5), xytext=(3.0, 10.5),
            arrowprops=dict(arrowstyle='->', color='#2C3E50', lw=1.3))
ax.text(2.45, 10.65, 'Si', fontsize=7.5, color='#1A5276', fontfamily='monospace')
rect(ax, 1.5, 10.5, 2.2, 0.65, 'MoveEgg\n(A, tour(sIndex))', color='#D6EAF8')

# rama NO (derecha)
ax.annotate('', xy=(7.8, 10.5), xytext=(7.0, 10.5),
            arrowprops=dict(arrowstyle='->', color='#2C3E50', lw=1.3))
ax.text(7.1, 10.65, 'No', fontsize=7.5, color='#1A5276', fontfamily='monospace')
rect(ax, 8.5, 10.5, 2.2, 0.65, 'MoveEgg\n(B, tour(sIndex))', color='#FADBD8')

# ambas ramas bajan y convergen
arrow(ax, 1.5, 10.17, 1.5, 9.3)
arrow(ax, 8.5, 10.17, 8.5, 9.3)
ax.plot([1.5, 5], [9.3, 9.3], color='#2C3E50', lw=1.3)
ax.plot([8.5, 5], [9.3, 9.3], color='#2C3E50', lw=1.3)
ax.annotate('', xy=(5, 8.95), xytext=(5, 9.3),
            arrowprops=dict(arrowstyle='->', color='#2C3E50', lw=1.3))

# PickAndPlace
rect(ax, 5, 8.6, 7.0, 0.65,
     'PickAndPlace: Off D0_09  ->  Jump Pallet(1,dest)  ->  On D0_09',
     color='#EBF5FB')
arrow(ax, 5, 8.27, 5, 7.75)

# UpdateOcc
rect(ax, 5, 7.4, 5.5, 0.65, 'UpdateOcc()  ->  actualizar posicion del huevo')
arrow(ax, 5, 7.07, 5, 6.55)

# Decision fin loop
diamond(ax, 5, 6.0, 3.5, 0.85, 'sIndex > 30?')

# flecha de vuelta (No - lado izquierdo)
ax.plot([3.25, 0.7], [6.0, 6.0], color='#7F8C8D', lw=1.1)
ax.plot([0.7, 0.7], [6.0, 10.5], color='#7F8C8D', lw=1.1)
ax.annotate('', xy=(1.0, 10.5), xytext=(0.7, 10.5),
            arrowprops=dict(arrowstyle='->', color='#7F8C8D', lw=1.1))
ax.text(0.1, 8.2, 'No\n(sig.\nsIndex)', fontsize=7, color='#7F8C8D',
        ha='center', fontfamily='monospace')

# Si -> Home
arrow(ax, 5, 5.57, 5, 5.05, label='Si', lx=5.15, ly=5.3)

# Home
rect(ax, 5, 4.7, 2.5, 0.6, 'Home', color='#D5F5E3')
arrow(ax, 5, 4.4, 5, 3.85)

# Motor OFF
rect(ax, 5, 3.5, 2.5, 0.6, 'Motor OFF', color='#FADBD8')
arrow(ax, 5, 3.2, 5, 2.65)

# FIN
oval(ax, 5, 2.3, 2.2, 0.65, 'FIN', color='#D5F5E3')

plt.tight_layout()
plt.savefig('diagrama_flujo.png', dpi=150, bbox_inches='tight', facecolor='#FAFAFA')
print('Flowchart OK')
