#include "../Headers/vector3d.h"
#include "../Headers/signal.h"
#include "../Headers/receiver.h"
#include "../Headers/object.h"
#include "../Headers/descrete_maffler.h"


Discrete_Maffler::Discrete_Maffler(
            Signal::Signal& signal,
            double noise_coeff, 
            double temperature, 
            double width_signal) 
            : 
            noise_coeff{noise_coeff},
            temperature{temperature},
            width_signal{width_signal} {}

Signal::Signal& Discrete_Maffler::noise_mc(){
    double noise = 1.38 * noise_coeff * temperature * width_signal * std::pow(10, -23);
    signal.coordinates.x += noise;
    signal.coordinates.y += noise;
    signal.coordinates.z += noise;
    return signal;
}