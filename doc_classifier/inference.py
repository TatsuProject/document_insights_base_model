from PIL import Image
import torch
import re
from transformers import DonutProcessor, VisionEncoderDecoderModel
#loading image from

def doc_classifier_predict(image):

    model_path = "naver-clova-ix/donut-base-finetuned-rvlcdip"
    processor = DonutProcessor.from_pretrained(model_path)
    model = VisionEncoderDecoderModel.from_pretrained(model_path)


    pixel_values = processor(image, return_tensors="pt").pixel_values

    task_prompt = "<s_rvlcdip>"

    decoder_input_ids = processor.tokenizer(task_prompt, add_special_tokens=False, return_tensors="pt")["input_ids"]

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)

    # generate response

    outputs = model.generate(
        pixel_values.to(device),
        decoder_input_ids=decoder_input_ids.to(device),
        max_length=model.decoder.config.max_position_embeddings,
        early_stopping=True,
        pad_token_id=processor.tokenizer.pad_token_id,
        eos_token_id=processor.tokenizer.eos_token_id,
        use_cache=True,
        num_beams=1,
        bad_words_ids=[[processor.tokenizer.unk_token_id]],
        return_dict_in_generate=True,
        output_scores=True
    )


    # cleaning responses

    seq = processor.batch_decode(outputs.sequences)[0]
    seq = seq.replace(processor.tokenizer.eos_token, "").replace(processor.tokenizer.pad_token, "")
    seq = re.sub(r"<.*?>", "", seq, count=1).strip()

    # convert response to json

    result = processor.token2json(seq)
    return result["class"]


if __name__ == '__main__':
    image = Image.open("").convert("RGB")
    prediction = doc_classifier_predict(image)
    print("document class: ", prediction)

