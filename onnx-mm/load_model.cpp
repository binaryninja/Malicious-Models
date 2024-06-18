#include <onnxruntime/core/providers/cpu/cpu_provider_factory.h>
#include <onnxruntime/core/session/onnxruntime_cxx_api.h>

int main() {
    const OrtApi& api = Ort::GetApi();
    Ort::Env env(ORT_LOGGING_LEVEL_WARNING, "test");

    Ort::SessionOptions session_options;
    session_options.AppendExecutionProvider_CPU(1);

    // Load the modified ONNX model
    Ort::Session session(env, "malicious_model.onnx", session_options);

    // Run the model
    Ort::AllocatorWithDefaultOptions allocator;
    auto input_name = session.GetInputName(0, allocator);
    std::vector<int64_t> input_dims = {1, 10};
    std::vector<float> input_data(10, 0.5f);

    Ort::Value input_tensor = Ort::Value::CreateTensor<float>(allocator, input_data.data(), input_data.size(), input_dims.data(), input_dims.size());
    const char* input_names[] = {input_name};

    auto output_tensors = session.Run(Ort::RunOptions{nullptr}, input_names, &input_tensor, 1, session.GetOutputNames(), session.GetOutputCount());

    return 0;
}
