#pragma once


constexpr double speed_of_light = 299792458; // meter / second
constexpr double plank_constant = 6.626 * std::pow(10, -34); // joule * second


class Vector3D;
class Object;

class Signal
{
    public:
        Signal(Vector3D coordinates_, Vector3D starting_direction_vector_, double energy_);

        void change_direction(Object& obj);

        Vector3D coordinates;
        Vector3D direction_vector;
        double passed_time;
        double energy;
};