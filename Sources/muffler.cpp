#include "../Headers/muffler.h"
#include <random>

Muffler::Muffler(
            double noise_percent_) 
            : 
            noise_percent{noise_percent_} {}

void Muffler::noise_mc(double& power){

    std::random_device dev;
    std::mt19937 rng(dev());
    std::uniform_int_distribution<std::mt19937::result_type> distr(1,1000);
    std::uniform_int_distribution<std::mt19937::result_type> distr_bool(0,1);

    double fraction = distr(rng) / 1000.0;

    double noise = power*fraction*(noise_percent/100.0);
    int sign = distr_bool(rng);
    if(sign % 2 == 0){
        power += std::abs(noise);
    } else {
        power -= std::abs(noise);
    }
}