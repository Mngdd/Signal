#pragma once



class Maffler
{
public:
    Maffler(double noise_percent);
    void noise_mc(double& power);

private:
    double noise_percent;
};