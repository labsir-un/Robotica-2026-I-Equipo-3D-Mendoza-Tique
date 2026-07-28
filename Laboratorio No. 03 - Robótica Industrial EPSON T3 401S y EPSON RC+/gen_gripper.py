import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import matplotlib.patheffects as pe

fig, ax = plt.subplots(figsize=(14, 7))
ax.set_xlim(0, 14)
ax.set_ylim(0, 7)
ax.axis('off')
fig.patch.set_facecolor('#F8F9FA')

# ── helpers ──────────────────────────────────────────────────────────────────
def box(ax, x, y, w, h, title, subtitle='', color='#D6EAF8',
        title_size=9, sub_size=8, bold=True):
    b = FancyBboxPatch((x - w/2, y - h/2), w, h,
                       boxstyle="round,pad=0.18",
                       linewidth=1.5, edgecolor='#2C3E50', facecolor=color, zorder=3)
    ax.add_patch(b)
    ty = y + 0.15 if subtitle else y
    ax.text(x, ty, title, ha='center', va='center',
            fontsize=title_size, fontweight='bold' if bold else 'normal',
            fontfamily='DejaVu Sans', zorder=4, multialignment='center')
    if subtitle:
        ax.text(x, y - 0.2, subtitle, ha='center', va='center',
                fontsize=sub_size, fontfamily='DejaVu Sans',
                color='#555', zorder=4, multialignment='center')

def oval(ax, x, y, w, h, text, color='#D5F5E3', fontsize=9):
    ell = mpatches.Ellipse((x, y), w, h, linewidth=1.5,
                            edgecolor='#1E8449', facecolor=color, zorder=3)
    ax.add_patch(ell)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            fontfamily='DejaVu Sans', zorder=4, multialignment='center',
            fontweight='bold')

def arr(ax, x1, y1, x2, y2, label='', color='#2C3E50',
        lx=None, ly=None, lw=1.5, style='->', ls='solid'):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle=style, color=color, lw=lw,
                                linestyle=ls), zorder=2)
    if label:
        lx = lx if lx is not None else (x1+x2)/2
        ly = ly if ly is not None else (y1+y2)/2 + 0.22
        ax.text(lx, ly, label, fontsize=8, color=color,
                ha='center', fontfamily='DejaVu Sans',
                fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.15', fc='white', ec='none', alpha=0.8))

def group(ax, x, y, w, h, label, color='#EBF5FB', ec='#85929E'):
    b = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.15",
                       linewidth=1.2, edgecolor=ec,
                       facecolor=color, zorder=1, linestyle='--', alpha=0.6)
    ax.add_patch(b)
    ax.text(x + 0.2, y + h - 0.12, label, fontsize=8.5, color='#34495E',
            fontfamily='DejaVu Sans', va='top', fontweight='bold')

# ── grupos de fondo ───────────────────────────────────────────────────────────
group(ax, 0.15, 0.4, 2.9,  6.2, 'Fuente neumática',  color='#EAFAF1', ec='#1E8449')
group(ax, 3.2,  0.4, 7.4,  6.2, 'Circuito neumático', color='#EBF5FB', ec='#2980B9')
group(ax, 10.8, 0.4, 3.0,  6.2, 'Control eléctrico',  color='#FEF9E7', ec='#D4AC0D')

# ── nodos ─────────────────────────────────────────────────────────────────────
# Compresor
oval(ax, 1.6, 3.5, 2.2, 1.1, 'Compresor\n4–6 bar', color='#A9DFBF')

# Válvula solenoide
box(ax, 5.2, 5.2, 2.8, 1.1, 'Válvula solenoide 5/2',
    '24 VDC  |  1/8" NPT', color='#AED6F1')

# Eyector Venturi
box(ax, 8.8, 5.2, 2.8, 1.1, 'Eyector Venturi',
    'Generador de vacío', color='#AED6F1')

# Ventosa
oval(ax, 5.2, 2.0, 2.6, 1.1, 'Ventosa silicona\nØ 35 mm', color='#FAD7A0')

# Sensor de vacío
box(ax, 8.8, 2.0, 2.8, 1.1, 'Sensor de vacío',
    '0 a −100 kPa  |  DI_01', color='#F1948A')

# Controlador RC700
box(ax, 12.3, 5.2, 2.4, 1.1, 'Controlador RC700',
    'Salida D0_09\n24 VDC', color='#F9E79F')

# Entrada DI_01 (dentro del controlador — solo label)
box(ax, 12.3, 2.0, 2.4, 1.1, 'Controlador RC700',
    'Entrada DI_01\nConfirm. agarre', color='#F9E79F')

# ── flechas ───────────────────────────────────────────────────────────────────
# Compresor → Válvula
arr(ax, 2.7, 3.5, 3.8, 5.2, 'aire\ncomprimido', color='#1E8449',
    lx=2.9, ly=4.6)

# Válvula → Eyector  (flujo neumático)
arr(ax, 6.6, 5.2, 7.4, 5.2, color='#2980B9')

# Eyector → Ventosa  (vacío)
ax.plot([8.8, 8.8], [4.65, 3.2], color='#2980B9', lw=1.5)
ax.plot([8.8, 5.2], [3.2, 3.2], color='#2980B9', lw=1.5)
ax.annotate('', xy=(5.2, 2.55), xytext=(5.2, 3.2),
            arrowprops=dict(arrowstyle='->', color='#2980B9', lw=1.5))
ax.text(7.0, 3.42, 'vacío', fontsize=8, color='#2980B9', ha='center',
        fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.15', fc='white', ec='none', alpha=0.8))

# Eyector → Sensor
arr(ax, 8.8, 4.65, 8.8, 2.55, color='#2980B9')

# RC700 → Válvula  (señal D0_09, control)
ax.annotate('', xy=(6.6, 5.2), xytext=(11.1, 5.2),
            arrowprops=dict(arrowstyle='->', color='#C0392B', lw=1.8,
                            linestyle='dashed'))
ax.text(8.85, 5.62, 'D0_09  |  ON = agarra  /  OFF = suelta',
        fontsize=8, color='#C0392B', ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.18', fc='#FDEDEC', ec='#C0392B', alpha=0.9))

# Sensor → RC700  (retroalimentación DI_01)
ax.annotate('', xy=(11.1, 2.0), xytext=(10.2, 2.0),
            arrowprops=dict(arrowstyle='->', color='#1E8449', lw=1.8,
                            linestyle='dashed'))
ax.text(10.65, 2.38, 'DI_01  |  señal de vacío',
        fontsize=8, color='#1E8449', ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.18', fc='#EAFAF1', ec='#1E8449', alpha=0.9))

# línea interna RC700 (D0_09 ↔ DI_01)
ax.plot([12.3, 12.3], [4.65, 2.55], color='#85929E', lw=1.0, linestyle=':')

plt.tight_layout(pad=0.5)
plt.savefig('diagrama_gripper.png', dpi=160, bbox_inches='tight', facecolor='#F8F9FA')
print('Gripper OK')
