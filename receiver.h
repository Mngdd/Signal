#pragma once


#include <vector>


class Vector3D;
class Signal;


class Receiver
{
    public:
        Receiver(Vector3D coordinates_, double critical_energy_, double L_);

        void receive_signals(std::vector<Signal>& v_sign);
        double distance();
    private:
        Vector3D coordinates;
        double current_energy;
        double critical_energy;
        double average_delay;
        double delay_sum;
        double dist;
        double L;
        int received_signals_count;
};