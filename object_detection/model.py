import torch
ssd_model = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_ssd')
utils = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_ssd_processing_utils')

THRESHOLD = 0.4


def detect_objects(tensor, threshold=THRESHOLD):
    ssd_model.to('cuda')
    ssd_model.eval()
    tensor = tensor.to('cuda')

    with torch.no_grad():
        detections_batch = ssd_model(tensor)

    results_per_input = utils.decode_results(detections_batch)
    best_results_per_input = [utils.pick_best(results, threshold) for results in results_per_input]

    return best_results_per_input
