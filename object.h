#pragma once


#include <vector>


class Vector3D;
class Signal;

class Object
{
    public:
        Object(Vector3D coordinates_, double radius_);
        void reflect(std::vector<Signal>& v_sign);
        Vector3D coordinates();

    private:
        Vector3D val_coordinates;
        double radius;
};