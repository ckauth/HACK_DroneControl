cmake_minimum_required(VERSION 2.8.11)
project(swissless)
if (CMAKE_C_COMPILER_ID STREQUAL "GNU")
  set (CMAKE_C_FLAGS "--std=c99 -g ${CMAKE_C_FLAGS}")
endif()

include_directories(include
	)

add_executable(
    ${PROJECT_NAME}
    rpiToCc3d.c)

link_directories(
	/usr/local/lib
)

if (CMAKE_SYSTEM_PROCESSOR MATCHES "^arm")
  target_link_libraries(
    ${PROJECT_NAME}
    wiringPi
		pthread)
else()
  target_link_libraries(
    ${PROJECT_NAME})
endif()
