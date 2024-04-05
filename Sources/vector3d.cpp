#include "../Headers/vector3d.h"


Vector3D::Vector3D() : x{0}, y{0}, z{0} {}

Vector3D::Vector3D(double x_, double y_, double z_) : x{x_}, y{y_}, z{z_} {}

void Vector3D::reverse() {x = -x; y = -y; z = -z;}

double Vector3D::abs() { return pow(x*x + y*y + z*z, 0.5); }

Vector3D operator+(Vector3D v1, Vector3D v2)
{
    return {v1.x + v2.x, v1.y + v2.y, v1.z + v2.z};
}

Vector3D operator-(Vector3D v)
{
    return {-v.x, -v.y, -v.z};
}

Vector3D operator-(Vector3D v1, Vector3D v2)
{
    return v1 + (-v2);
}

bool can_collide(Vector3D v1, Vector3D v2)
{
    if((v1.x == 0) && (v1.y == 0) && (v1.z == 0))
        throw std::runtime_error("object and RLS are at the same place");
    else if((v2.x == 0) && (v2.y == 0) && (v2.z == 0))
        throw std::runtime_error("signal has a null-vector direction");

    return (((v2.x != 0 && v2.y != 0 && v2.z != 0) && (v1.x/v2.x == v1.y/v2.y && v1.y/v2.y == v1.z/v2.z) && (v1.x/v2.x >= 0)) ||
            ((v1.x == v2.x && v1.x == 0 && v2.y != 0 && v2.z != 0) && (v1.y/v2.y == v1.z/v2.z) && (v1.y/v2.y >= 0)) ||
            ((v1.y == v2.y && v1.y == 0 && v2.x != 0 && v2.z != 0) && (v1.x/v2.x == v1.z/v2.z) && (v1.x/v2.x >= 0)) ||
            ((v1.z == v2.z && v1.z == 0 && v2.x != 0 && v2.y != 0) && (v1.x/v2.x == v1.y/v2.y) && (v1.x/v2.x >= 0)) ||
            ((v1.x == v2.x && v1.x == 0 && v1.y == v2.y && v1.y == 0 && v2.z != 0)) ||
            ((v1.x == v2.x && v1.x == 0 && v1.z == v2.z && v1.z == 0 && v2.y != 0)) ||
            ((v1.y == v2.y && v1.y == 0 && v1.z == v2.z && v1.z == 0 && v2.x != 0)));
}

//g++ -Og -Wall -Wextra -pedantic -Ilib -o Signal_ Sources/object.cpp Sources/radiator.cpp Sources/receiver.cpp Sources/signal.cpp Sources/vector3d.cpp Sources/muffler.cpp main.cpp