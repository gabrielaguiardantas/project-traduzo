from flask import Blueprint, render_template, request

from deep_translator import GoogleTranslator
from models.language_model import LanguageModel

from models.history_model import HistoryModel


translate_controller = Blueprint("translate_controller", __name__)


# Reqs. 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])
def index(translate_from="pt", translate_to="en"):
    if request.method == "POST":
        text_to_translate = request.form["text-to-translate"]
        translate_from = request.form["translate-from"]
        translate_to = request.form["translate-to"]
        translated = GoogleTranslator(
            source=translate_from, target=translate_to
        ).translate(text_to_translate)
        HistoryModel(
            {
                "text_to_translate": text_to_translate,
                "translate_from": translate_from,
                "translate_to": translate_to,
            }
        ).save()
        return render_template(
            "index.html",
            languages=LanguageModel.list_dicts(),
            text_to_translate=text_to_translate,
            translated_from=translate_from,
            translated_to=translate_to,
            translated=translated,
        )
    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        translated_from=translate_from,
        translated_to=translate_to,
    )


# Req. 6
@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    text_to_translate = request.form["text-to-translate"]
    translate_from = request.form["translate-from"]
    translate_to = request.form["translate-to"]
    translated = GoogleTranslator(
        source=translate_from, target=translate_to
    ).translate(text_to_translate)
    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate=text_to_translate,
        translated_from=translate_to,
        translated_to=translate_from,
        translated=translated,
    )


@translate_controller.route("/aqui", methods=["GET"])
def aqui():
    return "aqui"
