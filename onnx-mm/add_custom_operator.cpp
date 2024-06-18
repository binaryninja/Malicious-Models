#ifndef CUSTOM_OP_H
#define CUSTOM_OP_H

#include <iostream>
#include "onnxruntime_c_api.h"
#include "onnxruntime_cxx_api.h"  // Add this line to include the ONNX Runtime C++ API


struct CustomOp {
    explicit CustomOp(const OrtApi& api) : api_(api) {}

    void Compute(OrtKernelContext* context) {
        std::cout << "Malicious code executed!" << std::endl;
    }

    const OrtApi& api_;
};

struct CustomOpKernel : Ort::CustomOpBase<CustomOpKernel, CustomOp> {
    void* CreateKernel(OrtApi api, const OrtKernelInfo* info) const {
        return new CustomOp(api);
    }

    void Compute(void* op_kernel, OrtKernelContext* context) const {
        CustomOp* op = reinterpret_cast<CustomOp*>(op_kernel);
        op->Compute(context);
    }

    const char* GetName() const {
        return "CustomOp";
    }

    size_t GetInputTypeCount() const {
        return 1;
    }

    ONNXTensorElementDataType GetInputType(size_t index) const {
        return ONNX_TENSOR_ELEMENT_DATA_TYPE_FLOAT;
    }

    size_t GetOutputTypeCount() const {
        return 1;
    }

    ONNXTensorElementDataType GetOutputType(size_t index) const {
        return ONNX_TENSOR_ELEMENT_DATA_TYPE_FLOAT;
    }
};

#endif // CUSTOM_OP_H