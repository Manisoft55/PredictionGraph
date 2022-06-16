def translate_text(target, text):
    import six
    from google.cloud import translate_v2 as translate
    import os

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:\\Users\\manik\\Downloads\\hashin55\\hashin55\\my-translation-sa-key.json"
    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    result = translate_client.translate(text, target_language=target)
    print("Text: {}".format(result["input"]))
    print("Translation: {}".format(result["translatedText"]))
    print("Detected source language: {}".format(
        result["detectedSourceLanguage"]))

translate_text("en", "மணிகண்டன் மென்பொருள் பொறியாளர்")


translate_text("en", "धर्म सिंह, कर्म सिंह, भरत सिंह पुत्रान व सुनीता देवी, अनीता देवी पुत्रियां व श्रीमति माया देवी बिधवा चमेला राम पुत्र जोत राम हर छः समभाग वासीदेह")
