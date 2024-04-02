import numpy as np
from matplotlib.path import Path
from matplotlib.markers import MarkerStyle
from matplotlib.transforms import Affine2D

class Along:
    def __get_aspect(self, ax):
        if ax.get_aspect()=="auto":
            axw = ax.get_window_extent().width
            axh = ax.get_window_extent().height
            dataw = np.diff(ax.get_xlim())
            datah = np.diff(ax.get_ylim())
            xscale = axw / dataw
            yscale = axh / datah
            return yscale / xscale
        else:
            return ax.get_aspect()
    def get_half_arrow(self, headlength=0.4, headangle=30, pad=0.5):
        r = np.deg2rad(headangle)
        verts=[(-1,pad),(1,pad),(1-headlength*np.cos(r), pad+headlength*np.sin(r))]
        codes=[Path.MOVETO, Path.LINETO, Path.LINETO]
        return Path(verts, codes)
    def get_half_arrow_double(self, headlength=0.4, headangle=30, pad=0.5):
        r = np.deg2rad(headangle)
        verts=[(-1, pad),( 1, pad),( 1-headlength*np.cos(r),  pad+headlength*np.sin(r)),
               ( 1,-pad),(-1,-pad),(-1+headlength*np.cos(r), -pad-headlength*np.sin(r))]
        codes=[Path.MOVETO, Path.LINETO, Path.LINETO, Path.MOVETO, Path.LINETO, Path.LINETO]
        return Path(verts, codes)
    def plot(self, line, loc, marker, fillstyle, rotate=0, reflect=False, margin=0, kw={}):
        ax = line.axes
        xdata = line.get_xdata()
        ydata = line.get_ydata()
        xfig = xdata
        yfig = ydata * self.__get_aspect(ax)
        xyfig = np.array([xfig,yfig])
        segment_lengths = np.linalg.norm(np.diff(xyfig,axis=1), axis=0)
        segment_lengths /= np.sum(segment_lengths)
        seg_rate = np.array([0]+[np.sum(segment_lengths[:k+1]) for k in range(segment_lengths.size)])
        
        xp = seg_rate
        fp = np.arange(seg_rate.size)
        idxs = np.interp(loc, xp, fp)
        for idx in idxs:
            i = int(idx)
            if i<xdata.size-1:
                r = idx - i
            else:
                i -= 1
                r = 1
            if r < margin or r > 1 - margin:
                continue
            xr = (1 - r) * xdata[i] + r * xdata[i+1]
            yr = (1 - r) * ydata[i] + r * ydata[i+1]
            rot = np.rad2deg(np.arctan2(yfig[i+1]-yfig[i],xfig[i+1]-xfig[i]))
            a = np.eye(3)
            if reflect:
                a[0,0]=-1
            t = Affine2D(a) + Affine2D().rotate_deg(rot+rotate)
            if not "zorder" in kw: 
                kw["zorder"]=0
            ax.plot(xr,yr,lw=0,marker=MarkerStyle(marker,fillstyle,t), **kw)