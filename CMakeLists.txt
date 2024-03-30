cmake_minimum_required(VERSION 3.23)
project("Signal" VERSION 0.0.2 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 14)


set(SOURCES
        main.cpp
        Sources/object.cpp
        Sources/radiator.cpp
        Sources/receiver.cpp
        Sources/signal.cpp
        Sources/vector3d.cpp
        Sources/maffler.cpp
)

set(HEADERS
        Headers/object.h
        Headers/radiator.h
        Headers/receiver.h
        Headers/signal.h
        Headers/vector3d.h
        Headers/maffler.h
)

project(${TARGET} Signal)

add_executable(${PROJECT_NAME} ${SOURCES})
