# mplx
matplotlib extension package

## Install
```sh
pip install git+https://github.com/tomographyyy/mplx.git
```

## Sample code
```python
import numpy as np
import mplx
import matplotlib.pyplot as plt
import matplotlib.markers as markers

along = mplx.Along()
fig, ax = plt.subplots(figsize=(12,8),dpi=100)
x = np.linspace(0,3, num=23)
y = np.sin(x * 10)
line0, = ax.plot(x,y+1, c="k", zorder=1, lw=1)
line1, = ax.plot(x,y  , c="k", zorder=1, lw=1)
line2, = ax.plot(x,y-1, c="k", zorder=1, lw=1)
ax.set_xlim(0,3)
ax.set_ylim(-2.1,2.1)
ax.set_aspect(0.4)
loc = np.arange(0,1.01,0.02)
arrow2 = along.get_half_arrow_double(headlength=0.7, headangle=20, pad=0.4)

along.plot(line0, loc, marker=markers.CARETDOWNBASE, fillstyle="full", rotate=180, reflect=False, margin=0,
　　　　　　kw=dict(zorder=0, markerfacecolor="k", markeredgecolor="none", markersize=8))
along.plot(line1, loc, marker="o", fillstyle="top", rotate=0  , reflect=True, margin=0,
　　　　　　kw=dict(zorder=0, markerfacecolor="k", markeredgecolor="none", markersize=8))
along.plot(line2, loc, marker=arrow2, fillstyle="none", rotate=0  , reflect=False, margin=0.1,
　　　　　　kw=dict(zorder=0, markerfacecolor="none", markeredgecolor="k", markersize=15))
```
<p align="center" width="100%">
    <img width="60%" src="https://github.com/tomographyyy/mplx/assets/34155315/2a9eabc9-600d-4f44-89cb-39a966aaecd0"> 
</p>
