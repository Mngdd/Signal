#pragma once



class Muffler
{
public:
    Muffler(double noise_percent_);
    void noise_mc(double& power);

private:
    double noise_percent;
};