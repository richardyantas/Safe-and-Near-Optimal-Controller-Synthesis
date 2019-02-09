# g++ -frounding-math -ffloat-store -I/usr/local/include -I/usr/local/include/ibex  -O3 -DNDEBUG -Wno-deprecated -frounding-math  -o 4_rooms 4_rooms.cpp -L/usr/local/lib -libex -lprim -lClp -lCoinUtils

cmake_minimum_required(VERSION 3.5)
set(CMAKE_CXX_STANDARD 11)
#set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
project(main)

#-I/usr/local/include/ibex
# g++  -I/usr/local/include/ibex  -o main main.cpp -libex -lprim

if(UNIX)
    message("This is a ${CMAKE_SYSTEM_NAME} system")
elseif(WIN32)
    message("This is a Windows Systems")
endif()

include_directories( app/include /include/ibex/)

set(HEADERS app/include/utils.h app/include/sss.h)

set(SOURCES app/src/main.cpp)

add_executable(main ${HEADERS} ${SOURCES})
target_link_libraries(main ibex prim)