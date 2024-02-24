// make poopoo here <- fuck the one who wrote it
#include <iostream>
#include "vector3d.h"
#include "object.h"
#include "radiator.h"
#include "receiver.h"
#include "signal.h"


void simulate()
{
    Radiator rad{0, {1, 1, 1}, {1, 1, 1}};
    Object obj{{4, 4, 4}, 1};
    Receiver rec{{1, 1, 1}, 0};

    std::vector<Signal> vector_of_signals{};

    rad.emit_signal(vector_of_signals);
    obj.reflect(vector_of_signals);
    rec.receive_signals(vector_of_signals);

    double distance = rec.distance();

    std::cout << "Distance = " << distance;
}


int main()
{
    simulate();
    return 0;
}