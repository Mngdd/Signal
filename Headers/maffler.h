#pragma once


#include <vector>


class Vector3D;
class Signal;

class Maffler
{
public:
    double noise_coeff = 0.0;
    double temperature = 273.0;
    double width_signal = 0.0;

    Maffler(Signal& signal,
            double noise_coeff, 
            double temperature, 
            double width_signal);

    Signal& noise_mc();
    
};