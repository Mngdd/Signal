#pragma once

#include <cmath>
#include <stdexcept>

constexpr double speed_of_light = 299792458;                 // meter / second
constexpr double plank_constant = 6.626 * std::pow(10, -34); // joule * second
constexpr double PI = 3.1415926535;

class Vector3D
{
    public:
        Vector3D();
        Vector3D(double x_, double y_, double z_);
        void reverse();
        double abs();

        double x;
        double y;
        double z;
};

Vector3D operator+(Vector3D v1, Vector3D v2);
Vector3D operator-(Vector3D v);
Vector3D operator-(Vector3D v1, Vector3D v2);
Vector3D operator*(double coefficient, Vector3D v);
Vector3D operator*(Vector3D v, double coefficient);
Vector3D operator/(Vector3D v, double coefficient);