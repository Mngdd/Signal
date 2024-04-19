#pragma once


constexpr double speed_of_light = 299792458; // meter / second
constexpr double plank_constant = 6.626 * std::pow(10, -34); // joule * second
constexpr double PI = 3.1415926535;


class Vector3D;
class Object;

class Signal
{
    public:
        Signal(Vector3D coordinates_, Vector3D starting_direction_vector_, double energy_);

        void change_direction(Object& obj);
        double power() { return energy*energy; }

        Vector3D coordinates;
        Vector3D direction_vector;
        double passed_time;
        double energy;
        double wave_length;
};