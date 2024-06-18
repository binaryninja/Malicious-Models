cmake_minimum_required(VERSION 3.10)
project(MaliciousModels)

set(CMAKE_CXX_STANDARD 14)

# Path to ONNXRuntime
set(ONNXRUNTIME_ROOT "${CMAKE_SOURCE_DIR}/include/onnxruntime-linux-x64-gpu-1.18.0")

# Include directories
include_directories(${ONNXRUNTIME_ROOT}/include)

# Link directories
link_directories(${ONNXRUNTIME_ROOT}/lib)

# Add source files
set(SOURCES
    add_custom_operator.cpp
    custom_op.cpp
    load_model.cpp
)

# Add executable
add_executable(MaliciousModels ${SOURCES})

# Link ONNXRuntime libraries
target_link_libraries(MaliciousModels
    ${ONNXRUNTIME_ROOT}/lib/libonnxruntime.so
    ${ONNXRUNTIME_ROOT}/lib/libonnxruntime_providers_cuda.so
    ${ONNXRUNTIME_ROOT}/lib/libonnxruntime_providers_shared.so
    ${ONNXRUNTIME_ROOT}/lib/libonnxruntime_providers_tensorrt.so
)
