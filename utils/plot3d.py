from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d.proj3d import proj_transform

###############################################################
## For plotting weight and root diagrams
###############################################################

class Arrow3D(FancyArrowPatch):
    def __init__(self, x, y, z, dx, dy, dz, *args, **kwargs):
        super().__init__((0,0), (0,0), *args, **kwargs)
        self._xyz = (x,y,z)
        self._dxdydz = (dx,dy,dz)

    def draw(self, renderer):
        x1,y1,z1 = self._xyz
        dx,dy,dz = self._dxdydz
        x2,y2,z2 = (x1+dx,y1+dy,z1+dz)

        xs, ys, zs = proj_transform((x1,x2),(y1,y2),(z1,z2), renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        super().draw(renderer)
        
def _arrow3D(ax, *args, **kwargs):
    '''Add an 3d arrow to an `Axes3D` instance.'''
    for r in args:
        if len(r)<3:
            r = r.tolist()+[0]*(3-len(r))
        elif len(r)>3:
            r = r.tolist()[:3]
        else:
            r = r.tolist()
        arrow = Arrow3D(0, 0, 0, *r, **kwargs)
        ax.add_artist(arrow)
        
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_xlim(-1.5,1.5)
    ax.set_ylim(-1.5,1.5)
    ax.set_zlim(-1.5,1.5)