#pragma once


#include <vector>


class Vector3D;
class Signal;


class Radiator
{
    public:
        Radiator(double energy_, Vector3D coordinates_, Vector3D direction_vector_);
        void emit_signal(std::vector<Signal>& signal_vector);

    private:
        double energy;
        double wave_length;
        Vector3D coordinates;
        Vector3D direction_vector;
};