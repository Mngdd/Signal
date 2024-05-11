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
        void emit_signal(Receiver& receiver, Object& object);
        void reset_energy();

        static constexpr int base_distribution_percent = 100;
        static constexpr int base_number_of_measurements = 25;

    private:
        double current_energy;
        double base_energy;
        double wave_length;
        double L;
        double amplification_coefficient;
        int distribution = base_distribution_percent;
        int number_of_measurements = base_number_of_measurements;
        int current_percent = 0;

        Vector3D coordinates;
        Vector3D direction_vector;
};