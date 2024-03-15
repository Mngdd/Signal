#pragma once


#include <vector>


class Vector3D;
class Signal;
class Receiver;
class Object;


class Radiator
{
    public:
        Radiator(double energy_, Vector3D coordinates_, Vector3D direction_vector_, double L_, double amplification_coefficient_);
        void emit_signal(std::vector<Signal>& signal_vector);
        void emit_signal(Receiver& receiver, Object& object);

    private:
        double energy;
        double wave_length;
        double L;
        double amplification_coefficient;
        Vector3D coordinates;
        Vector3D direction_vector;
};