#pragma once


// Muffler - model class for muffling signal
class Muffler
{
public:
    Muffler(double noise_percent_);

    // muffle the signal
    void noise_mc(double& power);

private:
    double noise_percent;
};