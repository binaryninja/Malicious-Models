#include <iostream>
#include "onnxruntime_cxx_api.h"

// Define the custom operator's kernel
struct CustomOpKernel {
    CustomOpKernel(const OrtApi& api) : api_(api) {}

    void Compute(OrtKernelContext* context) {
        std::cout << "Malicious code executed!" << std::endl;
    }

    const OrtApi& api_;
};

// Define the custom operator
struct CustomOp : Ort::CustomOpBase<CustomOp, CustomOpKernel> {
    void* CreateKernel(OrtApi api, const OrtKernelInfo* info) const override {
        return new CustomOpKernel(api);
    }

    const char* GetName() const override {
        return "CustomOp";
    }

    const char* GetExecutionProviderType() const override {
        return "CPUExecutionProvider";
    }

    size_t GetInputTypeCount() const override {
        return 1;
    }

    ONNXTensorElementDataType GetInputType(size_t index) const override {
        return ONNX_TENSOR_ELEMENT_DATA_TYPE_FLOAT;
    }

    size_t GetOutputTypeCount() const override {
        return 1;
    }

    ONNXTensorElementDataType GetOutputType(size_t index) const override {
        return ONNX_TENSOR_ELEMENT_DATA_TYPE_FLOAT;
    }

    OrtCustomOpInputOutputCharacteristic GetInputCharacteristic(size_t /*index*/) const override {
        return OrtCustomOpInputOutputCharacteristic::ORT_INPUT_OUTPUT_REQUIRED;
    }

    OrtCustomOpInputOutputCharacteristic GetOutputCharacteristic(size_t /*index*/) const override {
        return OrtCustomOpInputOutputCharacteristic::ORT_INPUT_OUTPUT_REQUIRED;
    }
};

// Register the custom operator
OrtStatus* ORT_API_CALL RegisterCustomOps(OrtSessionOptions* options, const OrtApiBase* api_base) {
    const OrtApi* api = api_base->GetApi(ORT_API_VERSION);
    OrtCustomOpDomain* custom_op_domain = nullptr;
    OrtStatus* status = api->CreateCustomOpDomain("", &custom_op_domain);
    if (status != nullptr) return status;

    static CustomOp custom_op;
    status = api->CustomOpDomain_Add(custom_op_domain, &custom_op);
    if (status != nullptr) return status;

    status = api->AddCustomOpDomain(options, custom_op_domain);
    return status;
}

int main() {
    Ort::Env env(ORT_LOGGING_LEVEL_WARNING, "CustomOpExample");

    Ort::SessionOptions session_options;
    RegisterCustomOps(&session_options, OrtGetApiBase());

    // Replace "path/to/your/model.onnx" with the actual model path
    const char* model_path = "path/to/your/model.onnx";
    Ort::Session session(env, model_path, session_options);

    std::cout << "Custom operator registered and session created." << std::endl;

    return 0;
}
