from flask import abort
from flask_login import current_user
from flask_admin.contrib.sqla import ModelView


class ModelViewControl(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated and current_user.role == 'admin':
            return current_user.is_authenticated
        else:
            return abort(403)
