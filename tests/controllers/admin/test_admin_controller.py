from src.models.history_model import HistoryModel
from src.models.user_model import UserModel


def test_history_delete(app_test):
    # criar no banco um user admin com token
    UserModel(
        {"name": "Peter", "level": "admin", "token": "token_secreto123"}
    ).save()
    # criar um registro no histórico para ser deletado
    HistoryModel(
        {
            "text_to_translate": "Hello, I like videogame",
            "translate_from": "en",
            "translate_to": "pt",
        }
    ).save()

    # busco o id de inserção do histórico para deleção
    history_registry_id = HistoryModel.find_one({"translate_from": "en"}).data[
        "_id"
    ]

    # fazer a requisição para deletar o registro
    response = app_test.delete(
        f"/admin/history/{history_registry_id}",
        headers={"Authorization": "token_secreto123", "User": "Peter"},
    )
    assert response.status_code == 204
