"""Peewee migrations -- 003_Task scores.py.

Some examples (model - class or model name)::

    > Model = migrator.orm['model_name']            # Return model in current state by name

    > migrator.sql(sql)                             # Run custom SQL
    > migrator.python(func, *args, **kwargs)        # Run python code
    > migrator.create_model(Model)                  # Create a model (could be used as decorator)
    > migrator.remove_model(model, cascade=True)    # Remove a model
    > migrator.add_fields(model, **fields)          # Add fields to a model
    > migrator.change_fields(model, **fields)       # Change fields
    > migrator.remove_fields(model, *field_names, cascade=True)
    > migrator.rename_field(model, old_field_name, new_field_name)
    > migrator.rename_table(model, new_table_name)
    > migrator.add_index(model, *col_names, unique=False)
    > migrator.drop_index(model, *col_names)
    > migrator.add_not_null(model, *field_names)
    > migrator.drop_not_null(model, *field_names)
    > migrator.add_default(model, field_name, default)

"""

import peewee as pw
from peewee_migrate import Migrator
from decimal import ROUND_HALF_EVEN

try:
    import playhouse.postgres_ext as pw_pext
except ImportError:
    pass

SQL = pw.SQL


def migrate(migrator: Migrator, database: pw.Database, fake=False, **kwargs):
    """Write your migrations here."""
    
    migrator.add_fields(
        'users',

        task_3_scores=pw.IntegerField(constraints=[SQL("DEFAULT 0")], default=0, null=True),
        task_1_score=pw.IntegerField(constraints=[SQL("DEFAULT 0")], default=0, null=True),
        task_2_scores=pw.IntegerField(constraints=[SQL("DEFAULT 0")], default=0, null=True))

    migrator.remove_fields('users', 'task_1_best')


def rollback(migrator: Migrator, database: pw.Database, fake=False, **kwargs):
    """Write your rollback migrations here."""
    
    migrator.add_fields(
        'users',

        task_1_best=pw.IntegerField(constraints=[SQL("DEFAULT 0")], default=0, null=True))

    migrator.remove_fields('users', 'task_3_scores', 'task_1_score', 'task_2_scores')
