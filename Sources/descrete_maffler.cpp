#include "../Headers/vector3d.h"
#include "../Headers/signal.h"
#include "../Headers/receiver.h"
#include "../Headers/object.h"
#include "../Headers/descrete_maffler.h"


Discrete_Maffler::Discrete_Maffler(Signal& signal_, double noise_coeff_, double temperature_, double width_signal_) : 
    noise_coeff{noise_coeff_}, temperature{temperature_}, width_signal{width_signal_}, signal{signal_} {}

Signal& Discrete_Maffler::noise_mc(){
    double noise = 1.38 * noise_coeff * temperature * width_signal * std::pow(10, -23);
    signal.coordinates.x += noise;
    signal.coordinates.y += noise;
    signal.coordinates.z += noise;
    return signal;
}