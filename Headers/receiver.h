#pragma once


#include <vector>


class Vector3D;
class Signal;
class Radiator;
class Receiver;
class Maffler;

extern Maffler mafflerenok;

double distance(Object& object, Receiver& receiver);

// double speed_calculation(Radiator& radiator, Object& object, Receiver& receiver, double dt);

class Receiver
{
    public:
        Receiver(Vector3D coordinates_, double critical_energy_);

        double radiated_power;
        double received_power;
        double L;
        double wave_length;
        double sigma;
        double amplification_coefficient;

        friend double distance(Object& object, Receiver& receiver);

        void receive_signals(std::vector<Signal>& v_sign);

        double distance();
        double distance_using_power();
    private:
        Vector3D coordinates;
        double current_energy;
        double critical_energy;
        double average_delay;
        double delay_sum;
        double dist;
        int received_signals_count;
};

