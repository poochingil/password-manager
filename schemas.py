<<<<<<< HEAD
from marshmallow import Schema, fields


class PlainAddWebsiteSchema(Schema):
    username = fields.Str(required=True)
    website = fields.Str(required=True)
    password = fields.Str(required=True)
    modified_date = fields.Str(required=False)


class AddWebsiteSchema(PlainAddWebsiteSchema):
    id = fields.List(fields.Nested(lambda: PlainAddWebsiteSchema(), dump_only=True))


class PlainSignUpSchema(Schema):
    username = fields.Str(required=True, unique=True)
    password = fields.Str(required=True)
    email = fields.Str(required=True)
    phone_number = fields.Str(required=True, unique=False)


class SignUpSchema(PlainSignUpSchema):
    id = fields.List(fields.Nested(lambda: PlainSignUpSchema(), dump_only=True))


class LoginSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str()
    password = fields.Str(required=True)


class MakeAdminSchema(Schema):
    username = fields.Str()


class DeleteUserSchema(Schema):
    username = fields.Str()
# class ItemSchema(PlainItemSchema):
#     store_id = fields.Int(required=True, load_only=True)
#     store = fields.Nested(PlainStoreSchema(), dump_only=True)
#
#
# class ItemUpdateSchema(Schema):
#     name = fields.Str()
#     price = fields.Float()
#
#
# class StoreSchema(PlainStoreSchema):
#     items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
=======
from marshmallow import Schema, fields


class PlainAddWebsiteSchema(Schema):
    username = fields.Str(required=True)
    website = fields.Str(required=True)
    password = fields.Str(required=True)
    modified_date = fields.Str(required=False)


class AddWebsiteSchema(PlainAddWebsiteSchema):
    id = fields.List(fields.Nested(lambda: PlainAddWebsiteSchema(), dump_only=True))


class PlainSignUpSchema(Schema):
    username = fields.Str(required=True, unique=True)
    password = fields.Str(required=True)
    email = fields.Str(required=True)
    phone_number = fields.Str(required=True, unique=False)


class SignUpSchema(PlainSignUpSchema):
    id = fields.List(fields.Nested(lambda: PlainSignUpSchema(), dump_only=True))


class LoginSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str()
    password = fields.Str(required=True)


class MakeAdminSchema(Schema):
    username = fields.Str()


class DeleteUserSchema(Schema):
    username = fields.Str()
# class ItemSchema(PlainItemSchema):
#     store_id = fields.Int(required=True, load_only=True)
#     store = fields.Nested(PlainStoreSchema(), dump_only=True)
#
#
# class ItemUpdateSchema(Schema):
#     name = fields.Str()
#     price = fields.Float()
#
#
# class StoreSchema(PlainStoreSchema):
#     items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
>>>>>>> origin/main
