#pragma once


#include <cmath>
#include <stdexcept>


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