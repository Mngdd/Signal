#include "../Headers/vector3d.h"


Vector3D::Vector3D() : x{0}, y{0}, z{0} {}

Vector3D::Vector3D(double x_, double y_, double z_) : x{x_}, y{y_}, z{z_} {}

// reverse a vector
void Vector3D::reverse() {x = -x; y = -y; z = -z;}

// returns length of a vector
double Vector3D::abs() { return pow(x*x + y*y + z*z, 0.5); }

/////////////////////////////////////////
// Mathematical operations with vector //
/////////////////////////////////////////

// sum of two vectors
Vector3D operator+(Vector3D v1, Vector3D v2)
{
    return {v1.x + v2.x, v1.y + v2.y, v1.z + v2.z};
}

// reverse a vector
Vector3D operator-(Vector3D v)
{
    return {-v.x, -v.y, -v.z};
}

// subtraction of two vectors
Vector3D operator-(Vector3D v1, Vector3D v2)
{
    return v1 + (-v2);
}

// multiply vector by a constant
Vector3D operator*(double coefficient, Vector3D v)
{
    return {v.x*coefficient, v.y*coefficient, v.z*coefficient};
}

// multiply vector by a constant
Vector3D operator*(Vector3D v, double coefficient)
{
    return coefficient*v;
}

// divide vector by a constant
Vector3D operator/(Vector3D v, double coefficient)
{
    if(coefficient == 0)
        throw std::runtime_error("division by zero");
    return (1/coefficient)*v;
}

//g++ -Og -Wall -Wextra -pedantic -Ilib -o Signal Sources/object.cpp Sources/radiator.cpp Sources/receiver.cpp Sources/vector3d.cpp Sources/muffler.cpp main.cpp