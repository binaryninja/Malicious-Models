import onnx
from onnx import helper, TensorProto

def embed_malicious_code():
    model = onnx.load("simple_model.onnx")

    # Add a new node that executes the malicious code
    malicious_node = helper.make_node(
        'PyCustomOp',
        inputs=['onnx::Gemm_0'],
        outputs=['output'],
        name='MaliciousNode',
        domain='custom_domain',
        attr={
            'script': "print('Malicious code executed!')"
        }
    )

    model.graph.node.append(malicious_node)
    onnx.save(model, "malicious_model.onnx")

if __name__ == "__main__":
    embed_malicious_code()
