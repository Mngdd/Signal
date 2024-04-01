#include "../Headers/maffler.h"
#include <random>

Maffler::Maffler(
            double noise_percent) 
            : 
            noise_percent{noise_percent} {}

void Maffler::noise_mc(double& power){
    double noise = (std::rand() % 1000) / 100000.0;
    int sign = std::rand() % 2;
    if(sign % 2 == 0){
        power += std::abs(noise);
    } else {
        power -= std::abs(noise);
    }
}

Maffler mafflerenok(5);