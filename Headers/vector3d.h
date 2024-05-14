#pragma once

#include <cmath>
#include <stdexcept>

constexpr double speed_of_light = 299792458;                 // meter / second
constexpr double plank_constant = 6.626 * std::pow(10, -34); // joule * second
constexpr double PI = 3.1415926535;

// Mathematical vector in three-dimensional space;
// x, y, z - coordinates
class Vector3D
{
    public:
        Vector3D();
        Vector3D(double x_, double y_, double z_);
        // reverse a vector
        void reverse();
        // returns length of a vector
        double abs();

        double x;
        double y;
        double z;
};

/////////////////////////////////////////
// Mathematical operations with vector //
/////////////////////////////////////////

// sum of two vectors
Vector3D operator+(Vector3D v1, Vector3D v2);
// reverse a vector
Vector3D operator-(Vector3D v);
// subtraction of two vectors
Vector3D operator-(Vector3D v1, Vector3D v2);
// multiply vector by a constant
Vector3D operator*(double coefficient, Vector3D v);
// multiply vector by a constant
Vector3D operator*(Vector3D v, double coefficient);
// divide vector by a constant
Vector3D operator/(Vector3D v, double coefficient);