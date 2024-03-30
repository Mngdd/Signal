#pragma once



class Maffler
{
public:
    double noise_percent = 5.0;

    Maffler(double noise_percent);

    void noise_mc(double& power);

};

extern Maffler mafflerenok;