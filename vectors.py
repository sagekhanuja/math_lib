import math
import os
import time
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def help():
 print("Welcome to the math_lib library! This library has many vector features and continues to be updated. These are a list of the current functionalities and how to access them: \n")
 print("-dot product (accessible through the function: dotproduct(vector1,vector2)) \n")
 print("-find the angle between 3 vector points (accessible through the function: angle3points(point1, point2, point3) ) \n")
 print("-crossproduct of two vectors (accessible through the function: crossproduct(vector1, vector2) ) \n")
 print("-plane equation of 3 points (accessible through the function: plane_equation(point1, point2, point3) \n")
 print("-determinant of a 2x2/3x3 matrix (accessible through the function: det(matrix) entered as a 1d list, either 4 or 9 elements long )\n")
 print("-visualize a 3d point (accessible through the function: visualize_vectors(vector))\n")
 print("-2x2 matrix transformations (accessible through the function: tbttransformation(transformation_matrix, point) both entered as a 1d array)\n")
 print("-3x3 matrix transformations (accessible through the function: threebythreetransformation(transformation, point) both enetered as 1d arrays)")


#this is the function for dot products of 3x3 matrices
def dotproduct3(vector1, vector2):
    dp = (vector1[0]*vector2[0])+ (vector1[1]*vector2[1]) + (vector1[2]*vector2[2])

    if dp == 0:
        print("The dot product is 0 so the vectors are orthogonal")
    else:
        dpfinal = str(dp)
        print("The dot product is %s" % dpfinal)




 #this is the function for dot products of 2x2 matrices
def dotproduct2(vector1, vector2):
#maybe something to illustrate the time it takes to

    dp2 = (vector1[0]*vector2[0])+ (vector1[1]*vector2[1])

    if dp2 == 0:
        print("The dot product is 0 so the vectors are orthogonal")
    else:
        dpfinal2 = str(dp2)
        print("The dot product is %s" % dpfinal2)


def dotproduct(vector1, vector2):
    if len(vector1) and len(vector2) == 2:
        dotproduct2(vector1, vector2)
    if len(vector1) and len(vector2) == 3:
        dotproduct3(vector1, vector2)
    else:
        print("Please re-enter matrices. They do not coresspond.")




def angle3points(point1, point2, point3):   # this has an errror- deal with it

    final_vector1 = []                        #creating p0 first position vector
    final_vector2 = []
    posxcoord = point2[0]-point1[0]
    final_vector1.append(posxcoord)
    posycoord = point2[1]-point1[1]
    final_vector1.append(posycoord)
    poszcoord = point2[2]-point1[2]
    final_vector1.append(poszcoord)

 #this is the p1 position vector

    posxcoord2 = point3[0]-point1[0]
    final_vector2.append(posxcoord2)
    posycoord2 = point3[1]-point1[1]
    final_vector2.append(posycoord2)
    poszcoord2 = point3[2]-point1[2]

    #now we have to take the dot product of these two vectors
    angledotproduct = (final_vector1[0]*final_vector2[0]) + (final_vector1[1]*final_vector2[1])

    anglemagnitudeproduct = (math.sqrt((final_vector1[0])**2 + (final_vector1[1])**2)) * (math.sqrt((final_vector2[0])**2 + (final_vector2[1])**2))

    angle = str(math.acos(angledotproduct/anglemagnitudeproduct))

    print("The angle is %s" % angle)


def crossproduct(vector1, vector2):
    crossproductarry = []

    #creating the x y and z coordinates

    crossxcoord = (vector1[1]*vector2[2])-(vector1[2]*vector2[1])

    crossycoord= (vector1[2]*vector2[0]) - (vector1[0]*vector2[2])

    crosszcoord = (vector1[0]*vector2[1]) - (vector1[1]*vector2[0])

    #now we have to append the coordinates to the crossproductarry list

    crossproductarry.append(crossxcoord)
    crossproductarry.append(crossycoord)
    crossproductarry.append(crosszcoord)
    print("the cross product is:")
    print(crossproductarry)

def plane_equation(point1, point2, point3):
    #first we need to create position vectors from point1
    p0 = []
    p1 = []
#this is the code for p0 the first position vector
    p0xcoord = point2[0]- point1[0]
    p0.append(p0xcoord)

    p0ycoord = point2[1]- point1[1]
    p0.append(p0ycoord)

    p0zcoord = point2[2]- point1[2]
    p0.append(p0zcoord)

#this is the code for the p1 the second position vector
    p1xcoord = point3[0]- point1[0]
    p1.append(p1xcoord)

    p1ycoord = point3[1]- point1[1]
    p1.append(p1ycoord)


    p1zcoord = point3[2]- point1[2]
    p1.append(p1zcoord)

#now we must take the cross product of p0 and p1
    plane_crossproduct = crossproduct(p0, p1)


    plane_crossproduct_xcoord = plane_crossproduct[0]
    plane_crossproduct_ycoord = plane_crossproduct[1]
    plane_crossproduct_zcoord = plane_crossproduct[2]

    position_pointx = point1[0]
    position_pointy = point1[1]
    position_pointz = point1[2]

    print("The cartesian equation of this plane is: (%ix - %i + %iy - %is + %iz - %i = 0" % plane_crossproduct_xcoord, position_pointx, plane_crossproduct_ycoord, position_pointy, plane_crossproduct_zcoord, position_pointz)


def det(matrix):
    if len(matrix) == 4:
        determinant = (matrix[0]*matrix[3])-(matrix[1]*matrix[2])
        final_determinant = str(determinant)
        print("The determinant of this 2x2 matrix is %s" % final_determinant)

    if len(matrix) == 9:
        determinant2 = (matrix[0]*((matrix[4]*matrix[8])-(matrix[5]*matrix[7]))) - (matrix[1]*((matrix[3]*matrix[8])-(matrix[5]*matrix[6]))) + (matrix[2]*((matrix[3]*matrix[7])-(matrix[4]*matrix[6])))
        final_determinant2 = str(determinant2)
        print("The determinant of this 3x3 matrix is %s" % final_determinant2)

def visualize_vectors(vector):

    fig = plt.figure()
    mpl.rcParams['legend.fontsize'] = 10
    ax = fig.add_subplot(111, projection = '3d')


    x1 = vector[0]
    #linex.append(x1)
    y1 = vector[1]
    #liney.append(y1)
    z1 = vector[2]
    #linez.append(z1)

    ax.scatter(x1, y1, z1, c='r', marker='o')

    ax.set_xlabel('x axis')
    ax.set_ylabel('y axis')
    ax.set_zlabel('z axis')


    #plt.quiver(x1, y1, z1)
    plt.show()


def tbttransformation(transformation, point):  # fix name it is really confusing
    transformationa = transformation[0]
    transformationb = transformation[1]
    transformationc = transformation[2]
    transformationd = transformation[3]

    pointx = point[0]
    pointy = point[1]

    newmatrix = []

    newx = (transformationa*pointx) + (transformationb*pointy)
    newmatrix.append(newx)

    newy = (transformationc*pointx) + (transformationd*pointy)

    newmatrix.append(newy)

    print("The transformed coordinates from this 2x2 transformation matrix are: ")
    print(newmatrix)

def threebythreetransformation(transformation, point):
    transformationa2 = transformation[0]
    transformationb2 = transformation[1]
    transformationc2 = transformation[2]
    transformationd2 = transformation[3]
    transformatione2 = transformation[4]
    transformationf2 = transformation[5]
    transformationg2 = transformation[6]
    transformationh2 = transformation[7]
    transformationi2 = transformation[8]


    pointx = point[0]
    pointy = point[1]
    pointz = point[2]



    newmatrix1 = []
    newmatrix2 = []
    newmatrix3 = []

    newx = (transformationa*pointx) + (transformationb*pointy)
    newmatrix.append(newx)

    newy = (transformationc*pointx) + (transformationd*pointy)

    newmatrix.append(newy)

    print("The transformed coordinates from this 2x2 transformation matrix are: ")
    print(newmatrix)
