#pragma once


#include <vector>


class Vector3D;
class Signal;
class Radiator;
class Receiver;
class Muffler;


double distance(Object& object, Receiver& receiver);

class Receiver
{
    public:
        Receiver(Vector3D coordinates_, double critical_energy_);


        friend double distance(Object& object, Receiver& receiver);
        friend Vector3D dir_to_obj(Object& object, Receiver& receiver);

        void receive_signals(std::vector<Signal>& v_sign);
        void receive_signals(double radiated_power_, double received_power_, double L_,
                             double wave_length_, double sigma_, double amplification_coefficient_);

        double distance();
        double distance_using_power();
        double distance_using_power(Muffler& muffler);
        Vector3D coordinates_using_power(Vector3D direction_vector, Muffler& muffler);

        double speed_calculation(Radiator& rad, Object& object, Muffler& muffler, double dt);
        
        double get_sigma() { return sigma; }
        double get_wave_length() { return wave_length; }

        std::pair<double, double> mse(std::vector<double> arr);

        std::pair<double, double> mnk(std::vector<double> time, std::vector<double> coord);


    private:
        Vector3D coordinates;
        double current_energy;
        double critical_energy;
        double average_delay;
        double delay_sum;
        double dist;
        int received_signals_count;

        double radiated_power;
        double received_power;
        double L;
        double wave_length;
        double sigma;
        double amplification_coefficient;
};

