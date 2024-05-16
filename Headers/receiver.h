#pragma once


#include <vector>


class Vector3D;
class Object;
class Signal;
class Radiator;
class Receiver;
class Muffler;

// function to calculate initial distance between object and radiolocation station
double distance(Object& object, Receiver& receiver);


// Receiver - model class of a receiver in radiolocation station
class Receiver
{
    public:
        // base constructor
        Receiver(Vector3D coordinates_, double critical_energy_);

        // function to calculate initial distance between object and radiolocation station
        friend double distance(Object& object, Receiver& receiver);

        // function to calculate initial direction vector to object
        friend Vector3D dir_to_obj(Object& object, Receiver& receiver);

        // function to transfer parameters from radiator
        void receive_signals(double radiated_power_, double received_power_, double L_,
                             double wave_length_, double sigma_, double amplification_coefficient_);

        // calculate distance between object and radiolocation station,
        // using receiver power, radiated power, fix coefficient (L), amplification coefficient,
        // wave length, effective reflective surface, considering muffling effects
        double distance_using_power(Radiator& radiator, Object& object, Muffler& muffler);

        // calculate coordinates of an object using
        // receiver power, radiated power, fix coefficient (L), amplification coefficient,
        // wave length, effective reflective surface, considering muffling effects
        Vector3D coordinates_using_power(Radiator& radiator, Object& object, Vector3D direction_vector, Muffler& muffler);

        // calculate mean coordinates, and mean square error of coordinates of an object using
        // the same parameters as "coordinates_using_power", considering muffling effects
        std::pair<Vector3D, Vector3D> coordinates_with_mse(Radiator& radiator, Object& object, Vector3D direction_vector, Muffler& muffler);

        // calculate speed vector of an object, using least squares method
        Vector3D speed_vector_with_mse(Radiator& rad, Object& object, Muffler& muffler, Vector3D direction_vector, double dt);
        
        // getter for private parameter
        double get_sigma() { return sigma; }

        // getter got private parameter
        double get_wave_length() { return wave_length; }

        // mean square error
        std::pair<double, double> mse(std::vector<double> arr);

        // least squares method
        std::pair<double, double> mnk(std::vector<double> time, std::vector<double> coord);


    private:
        Vector3D coordinates;
        double current_energy;
        double critical_energy;
        int number_of_measurements = 25;
        int speed_measurements_amount = 10;

        double radiated_power;
        double received_power;
        double L;
        double wave_length;
        double sigma;
        double amplification_coefficient;
};

