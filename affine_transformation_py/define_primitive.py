import math
import numpy as np



class DefinePrimitive():


    def create_axis(self, scalar):

        ### XYZ-Arrow

        xx = [[0, 1 * scalar], [0,0], [0, 0]]
        yy = [[0, 0], [0, 1 * scalar], [0, 0]]
        zz = [[0, 0], [0, 0], [0, 1 * scalar]]

        return xx, yy, zz
    

    def create_grid(self, span, count):

        ### Create Grid

        xx = []
        yy = []
        zz = []

        for i in range(1, count):

            ### X
            ### X-Positive
            xx.append(span * i)
            yy.append(0)
            zz.append(0)

            ### X-Negative
            xx.append(span * i * (-1))
            yy.append(0)
            zz.append(0)

            ### Y
            ### Y-Positive
            xx.append(0)
            yy.append(span * i)
            zz.append(0)

            ### Y-Negative
            xx.append(0)
            yy.append(span * i * (-1))
            zz.append(0)

            ### Z
            ### Z-Positive
            xx.append(0)
            yy.append(0)
            zz.append(span * i)

            ### Z-Negative
            xx.append(0)
            yy.append(0)
            zz.append(span * i * (-1))

        return xx, yy, zz


    def create_cylinder(self, rad, h, seg_rad=16, seg_h=8):

        ### Create Cylinder

        xx = []
        yy = []
        zz = []

        a_unit = (math.pi * 2) / float(seg_rad)
        h_unit = float(h) / float(seg_h)

        for i in range(seg_rad + 1):

            ta = a_unit * i
            tx = math.cos(ta) * rad
            ty = math.sin(ta) * rad

            for j in range(seg_h + 1):
                tz = h_unit * j

                xx.append(tx)
                yy.append(ty)
                zz.append(tz)

        return xx, yy, zz
