from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    response = HistoryModel.list_as_json()
    str1_line1 = '"text_to_translate": "Hello, I like videogame", '
    str1_line2 = '"translate_from": "en", "translate_to": "pt"'
    str1 = str1_line1 + str1_line2
    assert str1 in response

    str2_line1 = '"text_to_translate": "Do you love music?", '
    str2_line2 = '"translate_from": "en", "translate_to": "pt"'
    str2 = str2_line1 + str2_line2
    assert str2 in response
