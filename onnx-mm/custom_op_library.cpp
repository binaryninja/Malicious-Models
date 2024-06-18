#include <onnxruntime_cxx_api.h>
#include "custom_op.cpp" // Include your custom operator implementation

extern "C" {
    OrtStatus* ORT_API_CALL RegisterCustomOps(OrtSessionOptions* options, const OrtApiBase* api) {
        const OrtApi* ort_api = api->GetApi(ORT_API_VERSION);
        Ort::CustomOpDomain custom_domain("custom_domain");
        CustomOpMaliciousOp custom_op;
        custom_domain.Add(&custom_op);
        return ort_api->AddCustomOpDomain(options, custom_domain);
    }
}
