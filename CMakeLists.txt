cmake_minimum_required(VERSION 2.8.11)

if (CMAKE_C_COMPILER_ID STREQUAL "GNU")
  set (CMAKE_C_FLAGS "--std=c99 -g ${CMAKE_C_FLAGS}")
endif()

include_directories(
    "."
    "/usr/include/.")

add_executable(
    swissless
    main.c)

if (CMAKE_SYSTEM_PROCESSOR MATCHES "^arm")
  target_link_libraries(
    swissless
    wiringPi)
else()
  target_link_libraries(
    swissless)
endif()