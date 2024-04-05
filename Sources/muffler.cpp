#include "../Headers/muffler.h"
#include <random>

Muffler::muffler(
            double noise_percent) 
            : 
            noise_percent{noise_percent} {}

void Muffler::noise_mc(double& power){
    double noise = ((std::rand() % 1000) / 1000.0*100.0) * noise_percent;
    int sign = std::rand() % 2;
    if(sign % 2 == 0){
        power += std::abs(noise);
    } else {
        power -= std::abs(noise);
    }
}