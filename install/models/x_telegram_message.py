from config import odoo

from core.odoorpc import OdooRPC

from core.crud.model import crud_create_model, crud_search_model, crud_delete_model
from core.crud.model_field import crud_create_model_field, crud_update_model_field, crud_search_model_fields, crud_get_model_fields
from core.crud.model_access import crud_create_model_access

from core.models import Model, ModelField, ModelAccess


def install_x_telegram_message():
    x_telegram_message_model = Model(
        name="Telegram Message",
        model="x_telegram_message",
    )

    model_id = crud_create_model(odoo, x_telegram_message_model)

    # x_name_field = crud_get_model_fields(
    #     odoo, [["name", "=", "x_name"], ["model_id", "=", model_id]])[0]

    # x_name_field.field_description = "Name"
    # x_name_field.required = True
    # x_name_field.model_id = model_id
    # x_name_field.readonly = True

    # crud_update_model_field(odoo, x_name_field.id, x_name_field)

    x_telegram_message_fields = [
        ModelField(
            model_id=model_id,
            name="x_message_id",
            field_description="Message ID",
            ttype="char",
            readonly=True,
            index=True,
        ),
        ModelField(
            model_id=model_id,
            name="x_text",
            field_description="Message Text",
            ttype="text",
            readonly=True,
        ),
        ModelField(
            model_id=model_id,
            name="x_chat_id",
            field_description="Chat ID",
            ttype="char",
            readonly=True,
        ),
        ModelField(
            model_id=model_id,
            name="x_from_id",
            field_description="From ID",
            ttype="char",
            readonly=True,
        ),
        ModelField(
            model_id=model_id,
            name="x_date",
            field_description="Date",
            ttype="datetime",
            readonly=True,
        )
    ]

    for field in x_telegram_message_fields:
        crud_create_model_field(odoo, field)

    x_telegram_message_access = ModelAccess(
        model_id=model_id,
        name="x_telegram_message_access"
    )

    crud_create_model_access(odoo, x_telegram_message_access)


def uninstall_x_telegram_message():
    model_id = crud_search_model(odoo, [["model", "=", "x_telegram_message"]])[0]

    crud_delete_model(odoo, model_id)
