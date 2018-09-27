from dolfin import Point, plot, ALE, Mesh
import mshr
from matplotlib import pyplot as plt
import numpy as np


def move_mesh(mesh, displacement):

    new_mesh = Mesh(mesh)

    for c in new_mesh.coordinates():
        c[0] += displacement.x()
        c[1] += displacement.y()

    return new_mesh


midpoint = Point(.5, .5)
p0 = Point(0, 0)
p1 = Point(1, 1)
nx = 100
ny = 100
radius = .1
dist = .1
n_vertices = 60
resolution = 5
whole_domain = mshr.Rectangle(p0, p1)
circular_domain = mshr.Circle(midpoint, radius, n_vertices)
circle_mesh = mshr.generate_mesh(circular_domain, resolution, "cgal")

for i in range(100):
    dmidpoint = Point(dist * np.cos(np.pi * 2/100 * i), dist * np.sin(np.pi * 2/100 * i))
    moved_midpoint = midpoint + dmidpoint
    circular_domain = mshr.Circle(moved_midpoint, radius, n_vertices)
    # todo what about ALE.move?
    new_circle_mesh = move_mesh(circle_mesh, dmidpoint)
    remaining_mesh = mshr.generate_mesh(whole_domain - circular_domain, 1, "cgal")
    plt.clf()
    plot(new_circle_mesh)
    plot(remaining_mesh)
    plt.pause(.1)
